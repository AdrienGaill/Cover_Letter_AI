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

test = "Having followed an education with a strong emphasis on computer science, including many courses in humanities and business, I am naturally versatile and curious and know how to integrate efficiently and flexibly into a team. I speak fluent English (TOEIC 980) and I am currently learning German. Therefore I would like to propose that we meet in order to convince you of my motivation and I am already enclosing my CV to that effect. I look forward to your reply and thank you in advance for your time and attention. I remain available for any information."

def text_slicer(text: str):
  """Split a paragraph after each dot in a list of sentences"""
  return text.split(". ")


# TODO Fix the case of special words 
def text_finisher(sentences: list):
  """Format a list of strings in one paragraph : capitalize each sentence,
  replace the i by upper-case ones and each proper noun by its correct spelling"""
  result = ""
  for sentence in sentences:
    sentence = sentence.capitalize()
    result += sentence + ". "
  result.replace(" i ", " I ")
  result.replace("react", "React")
  result.replace("python", "Python")

  return result


def paraphraser(sentences: list):
  selected_sentences = []
  # paraphrase each sentence individually
  for sentence in sentences:
    para_phrases = parrot.augment(input_phrase=sentence, use_gpu=False, do_diverse=True)
    # print(para_phrases)
    # TODO figure what the number is 
    # Select a random one among the results
    selected_sentences.append(random.choice(para_phrases)[0])
  return selected_sentences

print(text_finisher(paraphraser(text_slicer(test))))
# print(text_finisher(text_slicer(test)))
