from parrot import Parrot
import torch
import random
import warnings
warnings.filterwarnings("ignore")

# Prevent unwanted message from KeyphraseVectorizers
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def text_slicer(text: str):
  """Split a paragraph after each dot in a list of sentences"""
  return text.split(". ")


def get_data_from_txt(file: str, data: str):
  """
  Returns a list of dicts:
    'theme' is the sentences' main idea
    'sentences' or 'words' is the list of sentences/words related to the theme
    if data is 'words' then the dicts also have 'score' which is the word comparison score of the theme
  File must follow this format:
    theme
    sentences
    ...
    sentences

    theme
    sentences
    ... 
  Surplus blank lines are acknowledged and ignored
  """
  if data != "words" and data != "sentences":
    print("Wrong data argument.")
    return []

  f = open("./"+file, "r")
  lines = f.readlines()
  f.close()

  if data == "words":
    result = [{"theme":"", "words":[], "score": 0}]
    for index in range(len(lines)):
      if lines[index] == "\n":
        if index == 0 or lines[index-1] == "\n"  or index == len(lines)-1 or lines[index+1] == "\n":
          # Surplus blankline ignored
          pass

        else:
          result.append({"theme":"", "words":[], "score": 0})

      elif index == 0 or lines[index-1] == "\n":
        result[-1]["theme"] = lines[index].strip()

      else:
        result[-1]["words"].append(lines[index].strip())

  else:
    result = [{"theme":"", "sentences":[]}]
    for index in range(len(lines)):
      if lines[index] == "\n":
        if index == 0 or lines[index-1] == "\n":
          pass

        else:
          result.append({"theme":"", "sentences":[]})

      elif index == 0 or lines[index-1] == "\n":
        result[-1]["theme"] = lines[index].strip()

      else:
        result[-1]["sentences"].append(lines[index].strip())
  
  #TODO clean empty dicts ?
  return result
# print(get_data_from_txt("sentences.txt", "sentences"))
res = get_data_from_txt("word_list.txt", "words")
for elt in res:
  print(elt)


def paraphraser(sentences: list):
  
  #Init models (make sure you init ONLY once if you integrate this to your code)
  parrot = Parrot(model_tag="parrot_paraphraser_on_T5", use_gpu=False)

  selected_sentences = []
  # paraphrase each sentence individually
  for sentence in sentences:
    para_phrases = parrot.augment(input_phrase=sentence, use_gpu=False, do_diverse=True)
    # print(para_phrases)
    # TODO figure what the number is 
    # Select a random one among the results
    selected_sentences.append(random.choice(para_phrases)[0])
  return selected_sentences


# TODO Fix the case of special words ? issue of React/react
def text_finisher(sentences: list):
  """Format a list of strings in one paragraph : capitalize each sentence,
  replace the i by upper-case ones and each proper noun by its correct spelling"""
  result = ""
  for sentence in sentences:
    sentence = sentence.capitalize()
    result += sentence + ". "
  result.replace(" i ", " I ")
  # result.replace("react", "React")
  # result.replace("python", "Python")
  return result
