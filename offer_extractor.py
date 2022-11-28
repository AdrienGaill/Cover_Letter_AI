# Prevent unwanted message from KeyphraseVectorizers
from codecs import utf_8_encode
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
    client.close()
    pagesoup = soup(htmldata, "html.parser")

    # TODO Format title correctly
    # Fetch offer's title 
    offerTitle = pagesoup.findAll('h1', {"class": "top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title"})[0].text.strip()
    res.update({"title": offerTitle})

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

    # TODO handle emojis and apostrophs
    return res


# print(offer_extractor("https://www.linkedin.com/jobs/view/3341568256/?alternateChannel=search&refId=QYh%2BjS4URfirSywQlvBYEQ%3D%3D&trackingId=OqKmUh10OQq6J1YAhsRL9g%3D%3D"))
