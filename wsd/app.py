from wsd.preprocessor import Preprocessor
from nltk.corpus import wordnet as wn
from wsd.sentence_reader import WSDFileReader
from wsd.wsd import WSD

methods = ["stemming", "lemming"]

print("[>] => [NOT EMPTY OVERLAP]")
print("[~] => [EMTPY OVERLAP == DEFAULT VALUE]")
print()

for method in methods:
    print("METHOD:", method)
    print()
    preprocessor = Preprocessor("stop_words", method)
    sr = WSDFileReader("wsd.json", preprocessor)
    disambiguator = w = WSD(preprocessor)
    sentences_num = 0
    default_num = 0
    for word in sr.words_dict:
        print("\t[" + word.upper() + "]")

        for sentence, bag_of_words in sr.words_dict[word]:
            sentences_num += 1
            overlap, index = disambiguator.disambiguate(word, bag_of_words)
            print_sentence: str = sentence.replace(word, "[" + word.upper() + "]")
            if index != -1:
                print("\t>", print_sentence, "-->", wn.synsets(word)[index].definition())
            else:
                default_num += 1
                print("\t~", print_sentence, "-->", wn.synsets(word)[0].definition())
        print()
    print("\tNumber of sentences: ", sentences_num)
    print("\tNumber of default meanings: ", default_num)
    print()

