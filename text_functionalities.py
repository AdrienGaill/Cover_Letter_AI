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
      if lines[index].strip().isnumeric():
        result[-1]["score"]+=float(lines[index].strip())

      elif lines[index] == "\n":
        if index == 0 or index == len(lines)-1 or lines[index+1] == "\n":
          # Surplus blankline ignored
          continue

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
        if index == 0 or index == len(lines)-1 or lines[index+1] == "\n":
          # Surplus blankline ignored
          continue

        else:
          result.append({"theme":"", "sentences":[]})

      elif index == 0 or lines[index-1] == "\n":
        result[-1]["theme"] = lines[index].strip()

      else:
        result[-1]["sentences"].append(lines[index].strip())
  
  return result


def text_finisher(sentences: list):
  """Format a list of strings in one paragraph : capitalize each sentence,
  replace the i by upper-case ones and each proper noun by its correct spelling"""
  result = ""
  for sentence in sentences: 
    sentence = sentence.capitalize()
    if sentence[-1] == ".":
      result += sentence + " "      
    else:
      result += sentence + ". "
  result = result.replace(" i ", " I ")
  result = result.replace(" i'm ", " I'm ")
  return result

