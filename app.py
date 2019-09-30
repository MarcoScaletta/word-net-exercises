from nltk import WordNetLemmatizer
import string
from sentence_reader import SentenceReader
from preprocessor import Preprocessor
from stemmer import Stemmer
from nltk.stem.porter import PorterStemmer
from wsd import WSD
from nltk.corpus import wordnet as wn

preprocessor = Preprocessor("stop_words", lemming=True)

sr = SentenceReader("wsd.txt", preprocessor)
disambiguator = w = WSD(preprocessor)

for word in sr.words_dict:
    for bag_of_words in sr.words_dict[word]:
        overlap, index =disambiguator.disambiguate(word, bag_of_words)
        if index is not -1:
            print("for", bag_of_words, "meaning is", wn.synsets(word)[index])
            print()
    # exit()
ps = PorterStemmer()
print(ps.stem("wooden"))

# print(Preprocessor("stop_words").stop_words)

s1 = {3,4,5}
s2 = {1,2,3}

print(s1.intersection(s2))
print(s1.difference(s2))

# to_remove = set()
# to_remove += 'a'
# to_remove += string.punctuation
# print("a.sd,a./w.f,as.awfas.asd,a-a".translate(str.maketrans('', '', string.punctuation)))
