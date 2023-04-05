# import the necessary Python libraries and the dataset
from rake_nltk import Rake
rake_nltk_var = Rake()

# variable for text usign user input
text = input("Enter a Text: ")

# extract keywords from text
rake_nltk_var.extract_keywords_from_text(text)
keyword_extracted = rake_nltk_var.get_ranked_phrases()
print(keyword_extracted)
