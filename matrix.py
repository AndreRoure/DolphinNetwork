class DolphinGraph:
    def __init__(self, path):
        self.network = self.read(path)

    def read(self, path):
        network = {}
        with open(path,"r") as f:
            for l in f:
                if not l.startswith("%"):
                    relation = l.split()
                    if len(relation) == 2:
                        for dolphin in relation:
                            if dolphin not in network.keys():
                                network[dolphin] = set()
                        network[relation[1]].add(relation[0])
                        network[relation[0]].add(relation[1])
        return network

    def noPivotBK(self, R = set(), P = None, X = set(), ):
        if P is None:
            P = set(self.network.keys())
        if not P and not X:
            yield R
        while P:
            v = P.pop()
            yield from self.noPivotBK(R=R.union(v), P=P.intersection(self.network[v]), X=X.intersection(self.network[v]))
            X.add(v)
