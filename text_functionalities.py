import warnings
warnings.filterwarnings("ignore")

# Prevent unwanted message from KeyphraseVectorizers
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def text_slicer(text: str):
    """Split a paragraph after each dot in a list of sentences"""
    return text.split(". ")


def get_data_from_txt(file: str):
    """
    Returns a list of dicts from a .txt file:
        "theme" is the sentences' main idea
        "data" is the list of sentences/words related to the theme
        "score" is the word comparison score of the theme, it can have a base value to manually weight the theme
    File must follow this format:
        theme
        (base score if wanted)
        line of data
        ...
        line of data

        new theme
        ... 
    Surplus blank lines between themes are acknowledged and ignored
    """

    f = open("./"+file, "r")
    lines = f.readlines()
    f.close()

    result = [{"theme":"", "data":[], "score": 0}]

    for index in range(len(lines)):
        if lines[index].strip().isnumeric():
        # If the line is a number, it is recognised as the base score of the current theme
            result[-1]["score"]+=float(lines[index].strip())

        elif lines[index] == "\n":
            if index == 0 or index == len(lines)-1 or lines[index+1] == "\n":
                # Surplus blankline ignored
                continue

            else:
                # Blankline means new theme
                result.append({"theme":"", "data":[], "score": 0})

        elif index == 0 or lines[index-1] == "\n":
            # The first line of a data block is the theme
            result[-1]["theme"] = lines[index].strip()

        else:
            # Other lines are data ones
            result[-1]["data"].append(lines[index].strip())

    return result


def text_finisher(sentences: list):
    """Format a list of strings in one paragraph : capitalize each sentence,
    replace the i by upper-case ones and each proper noun by its correct spelling"""
    result = ""
    for sentence in sentences: 
        sentence = sentence.strip().capitalize()
        if sentence[-1] == ".":
            result += sentence + " "      
        else:
            result += sentence + ". "
    result = result.replace(" i ", " I ")
    result = result.replace(" i'm ", " I'm ")
    return result

