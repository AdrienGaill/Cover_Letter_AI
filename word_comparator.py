# Prevent unwanted message from KeyphraseVectorizers
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import spacy
nlp = spacy.load('en_core_web_lg')


def word_comparator(group1: str, group2: str):

    """Returns the similarity score of the two input words
       Initially made for words but seems to work on noun groups"""

    if group1 == group2:
        return 1
   
    # Lower words to avert case related problems
    token1 = nlp(group1.lower())
    if not token1.has_vector:
        # print (token1.text, "Pas de vecteur")
        return 0

    token2 = nlp(group2.lower())
    if not token2.has_vector:
        # print (token2.text, "Pas de vecteur")
        return 0

    # TODO add a threshold to avert false similarity
    return token1.similarity(token2)

# print(word_comparator("I like green", "gren is the colour I prefer"))
