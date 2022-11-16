from parrot import Parrot
import torch
import random
import warnings
warnings.filterwarnings("ignore")

# Prevent unwanted message from KeyphraseVectorizers
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#Init models (make sure you init ONLY once if you integrate this to your code)
parrot = Parrot(model_tag="parrot_paraphraser_on_T5", use_gpu=False)


test = "Having followed an education with a strong emphasis on computer science, including many courses in humanities and business, I am naturally versatile and curious and know how to integrate efficiently and flexibly into a team. I speak fluent English (TOEIC 980) and I’m currently learning German. Therefore I would like to propose that we meet in order to convince you of my motivation and I am already enclosing my CV to that effect. I look forward to your reply and thank you in advance for your time and attention. I remain available for any information."

def text_slicer(text: str):
  # TODO handle . at the end of sentences and lign break
  return text.split(". ")


# TODO edit final text to capitalize and join sentences into one text


def paraphraser(sentences: list):
  selected_sentences = []
  for sentence in sentences:
    # paraphrase each sentence individually
    para_phrases = parrot.augment(input_phrase=sentence, use_gpu=False, do_diverse=True)
    # print(para_phrases)
    selected_sentences.append(random.choice(para_phrases)[0])
  return selected_sentences

print(paraphraser(text_slicer(test)))

