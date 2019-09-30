
from nltk.corpus import wordnet as wn


class WSD:

    def __init__(self, preprocessor):
        self.preprocessor = preprocessor

    def disambiguate(self, word, bag_of_words: set):
        corrected_bag = bag_of_words
        # corrected_bag.remove(self.preprocessor.preprocess_word(word, stem=True))
        synsets = wn.synsets(word)
        max_overlap = 0
        max_index = -1

        print("\t", word)
        for i in range(len(synsets)):
            # print("lemmas =",synsets[i].lemma_names())
            synset_bow = self.synset_bag_of_words(synsets[i])
            # print("\t", synset_bow)
            overlap = len(corrected_bag.intersection(synset_bow))
            if overlap > max_overlap:
                max_overlap = overlap
                max_index = i
        print("Max overlap =", max_overlap, "at index ", max_index)
        return max_index, max_overlap

    def synset_bag_of_words(self, synset):
        definition_bow = self.preprocessor.preprocess_sentence(synset.definition())
        # print("\tDEF", synset.definition())
        examples_bow = set()
        examples = synset.examples()
        # if len(examples) == 0:
        #     print("NO EXAMPLE FOR ", synset)
        for example in examples:
            examples_bow.union(self.preprocessor.preprocess_sentence(example))
        return examples_bow.union(definition_bow)
