from word_comparator import word_comparator
from offer_extractor import offer_extractor

"""Intent to create an AI powered cover letter writting algorithm"""

f = open("./word_list.txt", "r")
ref_words = [x.strip() for x in f.readlines()]
f.close()

url = "https://www.linkedin.com/jobs/view/3341568256/?alternateChannel=search&refId=QYh%2BjS4URfirSywQlvBYEQ%3D%3D&trackingId=OqKmUh10OQq6J1YAhsRL9g%3D%3D"
data = offer_extractor(url)
keyphrases = data["keyphrases"]
sorted_kp = [ [x, []] for x in ref_words]

# Sort keyphrases extracted from offer using word comparison and a list of reference words
for kp in keyphrases:
    max_score = 0
    best_index = -1
    for i  in range(len(ref_words)):
        score = word_comparator(kp, ref_words[i])
        if score > max_score:
            max_score = score
            best_index = i
    if best_index >= 0:
        sorted_kp[best_index][1].append(kp)

print(sorted_kp)