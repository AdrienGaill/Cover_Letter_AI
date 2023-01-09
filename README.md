# Cover Letter AI
### by [Adrien Gaillard](https://www.linkedin.com/in/AdrienGaillard/)</br></br>

## History

<p align="justify">
I'm a French student in Centrale Nantes, a top French engineering school. Having followed an IT centered cursus, I discovered AI during my previous internship in Léonard, a company part of the VINCI group which plays a role of startup incubator in the AI and ConTech fields. To deepen my knowledge and discover new sides of AI development, I'm currently seeking an internship located in Berlin in the AI field. </br></br> Thus, I applied to several job offers and wrote a cover letter for each of them. Creating a relevant letter is an unintersting, tedious, time consuming but necessary process. Wanting to learn more about AI and especially NLP, I started a project willing to automatize the creating process by extracting data from the job offer. This humble project was also an occasion to show how I write code, as I can't publish the code from my last intership.
</p></br>

## How does it work?

<p align="justify">
The first step is to fetch the offer's data using <b>BeautifulSoup</b>. The goal was to work on LinkedIn job offers, because of the offer profiency and the recurrous template, allowing an easy treatment.</br></br>The offer's data is mainly the text, which will then be treated by the NLP part of the algorithm. Once extracted, the offer's text is curated and vectorized using <b>spaCy</b>. The next step is to excerpt the keywords from the vectorized text. More precisely, we fetch the keyphrases i.e. the nouns and noun groups (i.e. a sequence of adjectives followed by a noun) in order to sumarize efficiently the offer.</br></br>In order to analyse these keyphrases, I feed the program my custom list of keywords, grouped by 5 (in order to consider them equally) by theme to reflect the thematics carried by the offer</br></br>After being vectorized, each extracted keyphrase is compared to each of the custom keywords with a similarity test using a modified verion of the <b>spaCy</b> built-in comparator. A pair of keyphrase and keyword must have a score of similarity higher than a custom threshold to be considered relevant, which I chose to be <b>0.7</b>. The score of a theme is then the sum of the scores of each keyword linked to this theme while the score of each keyword is the sum of all the scores of the keyphrases and this keyword.</br></br>In order to reflect the offer, the themes with the higher scores are selected and their associated sentences are joined to create the core text of the cover letter.</br></br>Only a portion of the cover letter is actually dynamic, some basic information like my current cursus or basic structure need to be present whatever the offer is and constitute the template of the letter, which is then filled with the sentences from the selected themes.
</p></br>

## Possible improvments

<p align="justify">
- At first I wanted to paraphrase the custom sentences from the selected themes. I used <b> parrot </b> and a pretrained model made for it. The goal was to make the letters more unique and diverse. But the results weren't good enough : the new sentences were either the same than originals or slightly different but grammatically worst. Thus, in order to have sufficient results, I would have had to train my own model, which would have been too much time consuming for me at this time and not enough time-effective as the results with original custom sentences are good enough.</br></br>- This algorithm currently only accept url of a LinkedIn job offer. It would be interesting to make it accept a text. The changes would be easy to implement, I might work on this in a near future.</br></br>- The theme sorting system could be improved. For now, it is highly biaised because it is based on custom words reflecting my view of only a few themes. Only 5 words are chosen for each theme which means that the scores obtained could reflect badly the ideas carried by the offer. In addition, each theme is given a base score reflecting the importance I give it, resulting in even more bias. The best option would be to change the score system, which would result in the training of a better model.</br></br>- As my project is at a relatively low level of complexity and size, I chose not to implement tests and therefore not to follow the precepts of Test-Driven Development. Adding tests would have made my code more resilient but the development would have been more tedious.</br></br>- In the same vein as the previous point, time logs of every step of the whole process would allow me to improve the efficiency of this project and to identify potential errors. As the compute time for each cover letter is currently under 2 minutes, this feature is not a priority.</br></br>- The way reference words and corresponding sentences are currently handled could be improved. The present data structure is functional but quite unclear and needs precise formatting.</br></br>- Finally, adding more themes, with their corresponding reference words and sentences, would be an easy way to improve the accuracy of the cover letters produced. 
</p></br>

## Acknowledgements and contact

https://towardsdatascience.com/how-to-paraphrase-text-using-python-73b40a8b7e66  
https://www.geeksforgeeks.org/python-word-similarity-using-spacy/  
https://huggingface.co/prithivida/parrot_paraphraser_on_T5  

<p align="justify">
Don't hesitate to contact me if you need more information or if you have an opportunity to share!</br>
</p>

My mail : [adrien.gaillard.pro@gmail.com](mailto:adrien.gaillard.pro@gmail.com)</br>
My LinkedIn : [Adrien Gaillard](https://www.linkedin.com/in/AdrienGaillard/)