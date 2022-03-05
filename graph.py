import random

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

    def __noPivotBK(self, R = set(), P = None, X = set(), ):
        if P is None:
            P = set(self.network.keys())
        # Checks if there are no other possibilities or backtracks
        if not P and not X:
            yield R
            return
        #Iterates each vertex
        while P:
            #Remove vertex from possibilities
            v = P.pop()
            #Calls function with vertex on result, possibilities that are connected to the vertex, and processed vertex that are connected to vertex on focus
            yield from self.__noPivotBK(R=R.union({v}), P=P.intersection(self.network[v]), X=X.intersection(self.network[v]))
            #Add vertex to processed vertex set
            X.add(v)

    def noPivotBK(self):
        #Get all cliques from graph
        temp = list(self.__noPivotBK())
        # Remove non maximal cliques
        cliques = []
        for i in temp[:]:
            for c in cliques:
                if i.issubset(c) or i.union(c) == i.intersection(c):
                    continue
                elif c.issubset(i):
                    cliques.remove(c)
            cliques.append(i)
        return sorted(cliques, key=len)

    def __pivotBK(self, R = None, P = None, X = set(), ):
        R = set() if R is None else R
        if P is None:
            P = set(self.network.keys())
        #End recursion if possibilities and backtracks are empty
        if not P and not X:
            yield R
            return
        #Creates random pivot
        p = random.choice(list(P.union(X)))
        #Iterates each vertex
        for v in P.difference(self.network[p]):
            #Calls function with vertex on result, possibilities that are connected to the vertex, and backtracked vertex that are connected to vertex on focus
            yield from self.__pivotBK(R=R.union({v}), P=P.intersection(self.network[v]), X=X.intersection(self.network[v]))
            # Remove vertex from possibilities
            P.remove(v)
            #Add vertex to processed vertex set
            X.add(v)

    def pivotBK(self):
        return sorted(list(self.__pivotBK()), key=len)

    def clusteringCoefficient(self, trials=1000):
        #
        # Based on https://www.geeksforgeeks.org/clustering-coefficient-graph-theory/
        #
        n = len(self.network.keys())
        triangles = 0
        nodes = list(self.network.keys())
        for i in [int(random.random() * n) for i in range(trials)]:
            nbrs = list(self.network[nodes[i]])
            if len(nbrs) < 2:
                continue
            u, v = random.sample(nbrs, 2)
            if u in self.network[v]:
                triangles += 1
        return triangles / float(trials)