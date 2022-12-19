# Cover Letter Ai 
## by [Adrien Gaillard](https://www.linkedin.com/in/AdrienGaillard/)

### History

I'm a French student in Centrale Nantes, a top French engineering school. Having followed an IT centered cursus, I discovered AI during my previous internship in Léonard, a company part of the VINCI group which plays a role of startup incubator in the AI and ConTech fields. To deepen my knowledge and discover new sides of AI development, I'm currently seeking an internship located in Berlin in the AI field. 

Thus, I applied to several job offers and wrote a cover letter for each of them. Creating a relevant letter is an unintersting, tedious, time consuming but necessary process. Wanting to learn more about AI and especially NLP, I started a project willing to automatize the creating process by extracting data from the job offer. This project was also an occasion to show how I write code, as I can't publish the code from my last intership.

### How does it work?

The first step is to fetch the offer's data using **beautifulsoup**. The goal was to work on LinkedIn job offers, because of the offer profiency and the recurrous template, allowing an easy treatment.

The offer's data is mainly the text, which will then be treated by the NLP part of the algorithm. Once extracted, the offer's text is curated and vectorized using **spacy**. The next step is to excerpt the keywords from the vectorized text. More precisely, we fetch the keyphrases i.e. the nouns and noun groups (i.e. a sequence of adjectives followed by a noun) in order to sumarize efficiently the offer.

In order to analyse these keyphrases, I feed the program my custom list of keywords, grouped by 5 (in order to consider them equally) by theme to reflect the thematics carried by the offer 

After being vectorized, each extracted keyphrase is compared to each of the custom keywords with a similarity test using a modified verion of the **spacy** built-in comparator. A pair of keyphrase and keyword must have a score of similarity higher than a custom threshold to be considered relevant, which I chose to be **0.7**. The score of a theme is then the sum of the scores of each keyword linked to this theme while the score of each keyword is the sum of all the scores of the keyphrases and this keyword.

In order to reflect the offer, the themes with the higher scores are selected and their associated sentences are joined to create the core text of the cover letter.

Only a portion of the cover letter is actually dynamic, some basic information like my current cursus or basic structure need to be present whatever the offer is and constitute the template of the letter, which is then filled with the sentences from the selected themes.

### Possible improvments

At first I wanted to paraphrase the custom sentences from the selected themes. I used **parrot** and a pretrained model made for it. The goal was to make the letters more unique and diverse. But the results weren't good enough : the new sentences were either the same than originals or slightly different but grammatically worst. Thus, in order to have sufficient results, I would have had to train my own model, which would have been too much time consuming for me at this time and not enough time-effective as the results with original custom sentences are good enough.

This algorithm currently only accept url of a LinkedIn job offer. It would be interesting to make it accept a text. The changes would be easy to implement, I might work on this in a near future.

### Acknowledgements

[https://towardsdatascience.com/how-to-paraphrase-text-using-python-73b40a8b7e66]
[https://www.geeksforgeeks.org/python-word-similarity-using-spacy/]
[https://huggingface.co/prithivida/parrot_paraphraser_on_T5]
