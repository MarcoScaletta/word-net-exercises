
class PairsReader:

    def __init__(self, filename):
        self.filename = filename
        self.pairs = list()
        self.read_pairs()

    def read_pairs(self):
        f = open(self.filename)
        line = f.readline()
        while line:
            self.pairs.append(tuple(line.replace("\n","").split("\t")))
            line = f.readline()
