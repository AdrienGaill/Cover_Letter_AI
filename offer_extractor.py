# Prevent unwanted message from KeyphraseVectorizers
from re import sub
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import urllib.request as ul
from bs4 import BeautifulSoup as soup
from keyphrase_vectorizers import KeyphraseCountVectorizer
import spacy

nlp = spacy.load('en_core_web_lg')


def offer_extractor(source: str, data_type: str = "url"):
    """
    Fetch data from link or a .txt file and returns a dict with labelled data
        "source" has to be either the complete url or the .txt file name (with extension)
        "data_type" has to be "url" or ".txt", depending on the source you want to work with
    """
    res = {"title": "", "text": "", "keyphrases": []}
    text = ""

    # Fetch data from url using BeautifulSoup
    if data_type == "url":
        req = ul.Request(source, headers={'User-Agent': 'Mozilla/5.0'})
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

        # Fetch offer's text
        raw_text = pagesoup.find('div', {"class": "show-more-less-html__markup"})
        for elt in raw_text.stripped_strings:
            text += elt + " "

    # Fetch data by reading text file
    elif data_type == ".txt":
        f = open("./"+source, "r")
        lines = f.readlines()
        f.close()
        for line in lines:
            # Handle the unicode character \xe2\x80\x99 causing wrong encoding in UTF-8  
            line.replace('\xe2\x80\x99', "'")
            text  += line.strip() + " "

    # Clean offer's text
    text = text.replace("  ", " ").replace(" . ", ". ").replace(" , ", ", ").lower()
    res.update({"text": text})

    # Init default vectorizer.
    vectorizer = KeyphraseCountVectorizer(spacy_pipeline='en_core_web_lg')
    document_keyphrase_matrix = vectorizer.fit_transform([text]).toarray()
    keyphrases = vectorizer.get_feature_names_out()
    res.update({"keyphrases": keyphrases})

    # TODO handle emojis
    return res

