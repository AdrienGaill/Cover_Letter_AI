from word_comparator import word_comparator
from offer_extractor import offer_extractor
from text_functionalities import get_data_from_txt
from word_comparator import word_comparator
from pdf_creator import get_cover_letter

"""Main file to create an AI powered cover letter writting algorithm"""

# Extract reference words from .txt file
ref_words = get_data_from_txt("word_list.txt", "words")

# Extract keyphrases from offer
url = "https://www.linkedin.com/jobs/view/3341568256/?alternateChannel=search&refId=QYh%2BjS4URfirSywQlvBYEQ%3D%3D&trackingId=OqKmUh10OQq6J1YAhsRL9g%3D%3D"
data = offer_extractor(url)
keyphrases = data["keyphrases"]

# Sort keyphrases extracted from offer using word comparison and a list of reference words
sorted_kp = [ [x, []] for x in ref_words]
for kp in keyphrases:
    max_score = 0
    best_index = -1
    for i  in range(len(ref_words)):
        score = word_comparator(kp, ref_words[i])
        # TODO finetune the threshold to select the best kw ?
        if score > max_score and score > 0.39:
            max_score = score
            best_index = i
    if best_index >= 0:
        sorted_kp[best_index][1].append(kp)

# TODO choose sentence allocation given the sorted kw
paragraphs = ["Dear Sir or Madam",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    ]

# Generate the pdf file with the paraphrased paragraphs
letter_generator(paragraphs)
