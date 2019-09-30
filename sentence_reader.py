import string
from preprocessor import Preprocessor


class SentenceReader:

    def __init__(self, filename, preprocessor):
        self.preprocessor = preprocessor
        self.filename = filename
        self.words_dict = dict()
        file = open(filename, newline=None)
        line = file.readline()
        while line:
            if line.startswith("- "):
                word = preprocessor.preprocess_word(line[2:])
                self.words_dict[word] = list()
            elif line.startswith("= "):
                bag_of_words = preprocessor.preprocess_sentence(line[2:])
                self.words_dict[word].append(bag_of_words)
            line = file.readline()

