import matrix

def main(path):
    dolphinGraph = matrix.DolphinGraph(path)
    print(list(dolphinGraph.noPivotBK()))



main("soc-dolphins.mtx")
