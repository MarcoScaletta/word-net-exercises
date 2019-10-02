
from nltk.corpus import wordnet as wn


class WSD:

    def __init__(self, preprocessor):
        self.preprocessor = preprocessor

    def disambiguate(self, word, bag_of_words: set):
        corrected_bag = bag_of_words
        synsets = wn.synsets(word)
        max_overlap = 0
        max_index = -1

        for i in range(len(synsets)):
            synset_bow = self.synset_bag_of_words(synsets[i])
            overlap = corrected_bag.intersection(synset_bow)
            if len(overlap) > max_overlap:
                max_overlap = len(overlap)
                max_index = i
        return max_overlap, max_index

    def synset_bag_of_words(self, synset):
        definition_bow = self.preprocessor.preprocess_sentence(synset.definition())
        examples_bow = set()
        examples = synset.examples()
        for example in examples:
            examples_bow.union(self.preprocessor.preprocess_sentence(example))
        return examples_bow.union(definition_bow)
