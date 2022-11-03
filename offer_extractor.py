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


def offerExtractor(url: str):
    """Fetch data from link and returns a dict with labelled data"""
    res = {}

    req = ul.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    client = ul.urlopen(req)
    htmldata = client.read()
    client.close()
    pagesoup = soup(htmldata, "html.parser")

    # Fetch offer's title
    offerTitle = pagesoup.findAll('h1', {"class": "top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title"})[0].text.strip()
    res.update({"title": offerTitle})

    print(type(pagesoup))
    # Fetch offer's text
    raw_text = pagesoup.findAll('div', {"class": "show-more-less-html__markup"})
    text = ""
    for elt in raw_text:
        # print("Un elt", elt, type(elt))
        test = elt.findAll('li')
        for truc in test:
            # print(truc, type(truc))
            text += truc.text+"\n"
    # text = repr(text)
    # text.replace("\xe2\x80\x99", "'")
    print(type(text))
    print(text)
    # res.update({"text": text})
    # print("Original text: \n", text)

    # Init default vectorizer.
    vectorizer = KeyphraseCountVectorizer()

    # Print parameters
    # print(vectorizer.get_params())

    document_keyphrase_matrix = vectorizer.fit_transform([text]).toarray()
    # print(document_keyphrase_matrix)

    keyphrases = vectorizer.get_feature_names_out()
    res.update({"keyphrases": keyphrases})
    # print("Keyphrases before KeyBERT:\n\n", keyphrases)

    # Init KeyBERT
    kw_model = KeyBERT()
    res.update({"refined_keyphrases": kw_model.extract_keywords(docs=[text], vectorizer=KeyphraseCountVectorizer())})

    return res


print(offerExtractor("https://www.linkedin.com/jobs/view/3312551225/?alternateChannel=search&refId=DLl3pvTzJzCuMZfntlag%2FQ%3D%3D&trackingId=H14cMq68t4nN19PEVDEYbA%3D%3D&trk=d_flagship3_search_srp_jobs"))