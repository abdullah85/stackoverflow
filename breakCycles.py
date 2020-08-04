import networkx as nx

DG = nx.DiGraph()
DG.add_nodes_from(range(1,8))
DG.add_edges_from([(1,2), (2,3), (3,4), (3,5), (4,5), (5,1), (5,4), (5,7), (6,4), (7,6)]);

def getRemovableEdges(G, edgeLst, initNodes):
    import networkx as nx    
    removableEdgeLst = []
    for (u,v) in edgeLst:
        G.remove_edge(u, v)
        f = nx.floyd_warshall(G)
        addEdge = True
        for s in initNodes:
            if 'inf' in list(map(str, f[s].values())):
                G.add_edge(u,v)
                addEdge = False
                break
        if addEdge:
            removableEdgeLst.append((u,v))
    return removableEdgeLst
    
def combinations(edges, level):
    result = []
    for i in range(level):
        result.append((i, edges))
    return result

def breakCycles(g):
    edges = g.edges
    for level in range(2, len(edges)):
        stop = True
        edges2 = combinations(edges,level)
        for i, e in enumerate(edges2):
            g.remove_edges_from(e)

            test = True
            for node in orange_nodes:
                d = nx.algorithms.descendants(g, node)
                test = blue_nodes == d
                if not test:
                    break
            if test:
                stop = False
                cycles_count = len(list(nx.simple_cycles(g)))
                print(f'{i}\t{level}\t{cycles_count}\t{e}')

            g.add_edges_from(e)

        if stop:
            break
    return g

#breakCycles(DG)
