# Prevent unwanted message from KeyphraseVectorizers
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import spacy
nlp = spacy.load('en_core_web_lg')


def word_comparator(group1: str, group2: str):

    """Returns the similarity score of the two input words
       Initially made for words but seems to work on noun groups"""

    # Lower words to avert case related problems
    token1 = nlp(group1.lower())
    token2 = nlp(group2.lower())

    # Attributes of each token :
    # text: the word string
    # has_vector: if it contains a vector representation in the model
    # vector_norm: the algebraic norm of the vector
    # is_oov: if the word is out of vocabulary

    # TODO add a threshold to avert false similarity
    return token1.similarity(token2)

# print(word_comparator("I like green", "gren is the colour I prefer"))
