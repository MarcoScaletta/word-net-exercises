
from porter_stemmer import PorterStemmer


class Stemmer:

    def __init__(self):
        self.porter_stemmer = PorterStemmer()

    def stem(self, word):
        return self.porter_stemmer.stem(word, 0, len(word))
