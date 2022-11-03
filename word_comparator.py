# Prevent unwanted message from KeyphraseVectorizers
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import spacy
nlp = spacy.load('en_core_web_lg')


def word_comparator(word1: str, word2: str):

    tokens = nlp(word1+" "+word2)

    for token in tokens:
        # Printing the following attributes of each token.
        # text: the word string, has_vector: if it contains
        # a vector representation in the model,
        # vector_norm: the algebraic norm of the vector,
        # is_oov: if the word is out of vocabulary.

        # print(token.text, token.has_vector, token.vector_norm, token.is_oov)

        if token.is_oov:
            print("This word is out of vocabulary")
            return 0
 
    token1, token2 = tokens[0], tokens[1]

    return token1.similarity(token2)

print(word_comparator("dog", "cat"))