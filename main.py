from offer_extractor import offer_extractor
from text_functionalities import get_data_from_txt, text_finisher
from word_comparator import word_comparator
from pdf_creator import get_cover_letter

# Main file to create an AI powered cover letter writting algorithm

# Extract reference words from .txt file
ref_words = get_data_from_txt("word_list.txt")

# Extract keyphrases from offer
url = "https://www.linkedin.com/jobs/view/3420171862/?alternateChannel=search&refId=XLx67ex51zcXTlgb2eShbw%3D%3D&trackingId=0t1QwV3cg2qlhcAkaKGsTA%3D%3D"
data = offer_extractor(url)
offer_keywords = data["keyphrases"]
offer_title = data["title"]

# Allow score to reference words using word comparison with extracted keywords
for kw in offer_keywords:
    for theme in ref_words:
        for word in theme["data"]:
            score = word_comparator(kw, word)
            # Threshold to ensure a sufficient level of similarity
            if score > 0.7:
                theme["score"] += score

# Corresponding sentences are separated into two thematic sets
assets = get_data_from_txt("assets.txt")
experience = get_data_from_txt("experience.txt")

# Filtering out sentences without a corresponding theme among the reference words
assets = list(filter(lambda elt: elt["theme"] in [x["theme"] for x in ref_words], assets))
experience = list(filter(lambda elt: elt["theme"] in [x["theme"] for x in ref_words], experience))

# Each sentence set is given its corresponding word set's score
for sentence_theme in assets:
    for word_theme in  ref_words:
        if sentence_theme["theme"] == word_theme["theme"]:
            sentence_theme["score"] = word_theme["score"]
for sentence_theme in experience:
    for word_theme in  ref_words:
        if sentence_theme["theme"] == word_theme["theme"]:
            sentence_theme["score"] = word_theme["score"]

# Only the top four scores in each thematic set are retained
assets = sorted(assets, key = lambda elt : -elt["score"])[:4]
experience = sorted(experience, key = lambda elt : -elt["score"])[:4]

# One clean paragraph is created for each thematic set
assets = text_finisher([(" ").join(x["data"]) for x in assets])
experience = text_finisher([(" ").join(x["data"]) for x in experience])

# Development languages are considered separately but still tested with word comparison
languages = get_data_from_txt("languages.txt")[0]["data"]
languages = [{"language": x, "score": 0} for x in languages]
for kw in offer_keywords:
    for language in languages:
        score = word_comparator(kw, language["language"])
        if score > 0.7:
            # print(score, kw, language["language"])
            language["score"] += score

# Keeping only the languages with at least one positive match (score > 0)
languages = list(filter(lambda elt: elt["score"] > 0, languages))
languages = [x["language"] for x in languages]

# Structure the list of relatable languages in a sentence
languages_list = ""
for i in range(len(languages)):
    if i == 0:
        languages_list += languages[0]
    elif i == len(languages)-1:
        languages_list += " and " + languages[i]
    else:
        languages_list += ", " + languages[i]
language_sentence = f" I have experience in {languages_list} programming."

# Add it to the experience paragraph 
experience += language_sentence

# Generate the pdf file with the paraphrased paragraphs
paragraphs = [assets, experience]
get_cover_letter(paragraphs, offer_title)
