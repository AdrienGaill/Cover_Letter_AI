# Prevent unwanted message from KeyphraseVectorizers
from codecs import utf_8_encode
from re import sub
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from cgitb import reset
from turtle import title
import urllib.request as ul
from bs4 import BeautifulSoup as soup
from keyphrase_vectorizers import KeyphraseCountVectorizer
from keybert import KeyBERT
import spacy

nlp = spacy.load('en_core_web_lg')


def offer_extractor(url: str):
    """Fetch data from link and returns a dict with labelled data"""
    res = {}

    req = ul.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    client = ul.urlopen(req)
    htmldata = client.read()

    # Handle the unicode character \xe2\x80\x99 causing wrong encoding in UTF-8  
    htmldata = sub(b'\xe2\x80\x99', b"'", htmldata)
    client.close()
    pagesoup = soup(htmldata, features="html.parser")

    # Fetch offer's title 
    offer_title = pagesoup.findAll('h1', {"class": "top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title"})[0].text.strip()
    offer_title = sub("\(.*\)", "", offer_title)
    res.update({"title": offer_title})

    # Fetch and clean offer's text
    text = ""
    raw_text = pagesoup.find('div', {"class": "show-more-less-html__markup"})
    for elt in raw_text.stripped_strings:
        text += elt + " "
    text = text.replace("  ", " ").replace(" . ", ". ").replace(" , ", ", ").lower()
    res.update({"text": text})

    # Init default vectorizer.
    vectorizer = KeyphraseCountVectorizer(spacy_pipeline='en_core_web_lg')
    document_keyphrase_matrix = vectorizer.fit_transform([text]).toarray()
    keyphrases = vectorizer.get_feature_names_out()
    res.update({"keyphrases": keyphrases})

    # Init KeyBERT
    kw_model = KeyBERT()
    res.update({"refined_keyphrases": kw_model.extract_keywords(docs=[text], vectorizer=KeyphraseCountVectorizer())})

    # TODO handle emojis
    return res

