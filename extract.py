# import the necessary Python libraries and the dataset
from rake_nltk import Rake
rake_nltk_var = Rake()

# variable for text usign user input
text = """ I am a programmer from India, and I am here to guide you
with Data Science, Machine Learning, Python, and C++ for free.
I hope you will learn a lot in your journey towards Coding,
Machine Learning and Artificial Intelligence with me."""

# extract keywords from text
rake_nltk_var.extract_keywords_from_text(text)
keyword_extracted = rake_nltk_var.get_ranked_phrases()
print(keyword_extracted)
