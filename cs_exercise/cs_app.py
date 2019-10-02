from cs_exercise.pairs_reader import PairsReader
from nltk.corpus import wordnet as wn

from cs_exercise.wn_cs_utils import cs

p = PairsReader("100_pairs-updated.txt")
# print(p.pairs)

for p1, p2 in p.pairs:

    sim, max_pair = cs(p1, p2)
    print("cs(" + p1+","+p2+") =", sim)
    print()

sim, max_pair = cs("car", "bus")
print("cs(car,bus) =", sim)
print()


