
from nltk.corpus import wordnet as wn


def all_ancestors(synset):
    ancestors = list()
    while len(synset.hypernyms()) > 0:
        synset = synset.hypernyms()[0]
        ancestors.insert(0, synset)
    return ancestors


def cs(word1, word2):
    max_similarity = 0
    max_synset_pair = None

    if len(wn.synsets(word1)) == 0:
        print("/!\\", word1, "has no synsets")
    if len(wn.synsets(word2)) == 0:
        print("/!\\", word2, "has no synsets")

    for synset1 in wn.synsets(word1):
        for synset2 in wn.synsets(word2):

            similarity = cs_synset(synset1, synset2)

            if similarity > max_similarity:
                max_similarity = similarity
                max_synset_pair = (synset1, synset2)
    return max_similarity, max_synset_pair


def cs_synset(synset1, synset2):
    ancestors1 = all_ancestors(synset1)
    ancestors2 = all_ancestors(synset2)
    # print(synset1.name(), "has depth =", len(ancestors1)+1)
    # print(synset2.name(), "has depth =", len(ancestors2)+1)
    common_ancestors = [ancestor.name() for ancestor in ancestors1 if ancestor in ancestors2]
    # print([ancestor.name() for ancestor in ancestors1])
    # print([ancestor.name() for ancestor in ancestors2])
    # print(common_ancestors)
    cs_value = 2*len(common_ancestors)/(len(ancestors1)+1 + len(ancestors2)+1)
    return cs_value
