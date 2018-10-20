from nltk.stem import PorterStemmer
from  nltk.tokenize import word_tokenize


ps = PorterStemmer()

new_text = "It is very importent to be pythonly while you are pythoning with python. All pythoner have pythoned poorly at least once."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))