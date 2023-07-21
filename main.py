import graph

def main(path):
    dolphinGraph = graph.DolphinGraph(path)

    print("Maximal Cliques without pivot:")
    for c in dolphinGraph.noPivotBK():
        print("Size: ", len(c), end=" Vertex: ")
        for v in sorted(c):
            print(v, end=" ")
        print("")

    print("\nMaximal Cliques with pivot:")
    for c in dolphinGraph.pivotBK():
        print("Size: ", len(c), end=" Vertex: ")
        for v in sorted(c):
            print(v, end=" ")
        print("")

    print("\n Clustering Coefficient:", dolphinGraph.clusteringCoefficient())



main("soc-dolphins.mtx")
