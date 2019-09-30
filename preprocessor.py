
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import string

class Preprocessor:

    def __init__(self, stop_words_filename, lemming=False):
        f = open(stop_words_filename)
        self.stop_words = set(f.read().splitlines())
        self.lemming = lemming
        lines = f.read().splitlines()

    def preprocess_sentence(self, sentence: str):
        cleaned_sentence = self.clean_string(sentence)
        bag_of_words = set(cleaned_sentence.lower().split())
        if not self.lemming:
            return set(map(lambda x: WordNetLemmatizer().lemmatize(x), bag_of_words.difference(self.stop_words)))
        else:
            return set(map(lambda x: PorterStemmer().stem(x), bag_of_words.difference(self.stop_words)))

    def preprocess_word(self, word: str, stem=False):
        cleaned_word = self.clean_string(word)
        if stem:
            return PorterStemmer().stem(cleaned_word)
        return cleaned_word

    @staticmethod
    def clean_string(raw_string):
        return raw_string.replace("\n", "").translate(str.maketrans('', '', string.punctuation))

