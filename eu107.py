#------------------------------------------------------ Minimal network ----------------------------------------------- #
#                                                                                                                       #
#       The following undirected network consists of seven vertices and twelve edges with a total weight of 243.        #
#                                                                                                                       #
#       The same network can be represented by the matrix below.                                                        #
#                                                                                                                       #
#                               	A	B	C	D	E	F	G                               #
#                               A	-	16	12	21	-	-	-                               #
#                               B	16	-	-	17	20	-	-                               #
#                               C	12	-	-	28	-	31	-                               #
#                               D	21	17	28	-	18	19	23                              #
#                               E	-	20	-	18	-	-	11                              #
#                               F	-	-	31	19	-	-	27                              #
#                               G	-	-	-	23	11	27	-                               #
#                                                                                                                       #
#       However, it is possible to optimise the network by removing some edges and still ensure that all points         #
#       on the network remain connected. The network which achieves the maximum saving is shown below.                  #
#       It has a weight of 93, representing a saving of 243 − 93 = 150 from the original network.                       #
#                                                                                                                       #
#       Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with          #
#       forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing             #
#       redundant edges whilst ensuring that the network remains connected.                                             #
# --------------------------------------------------------------------------------------------------------------------- #
import time

def MST_prim(edges, num_of_vertices):
    mst = []

    spanned_vertices = [0]

    for t in range(num_of_vertices - 1):
        min_edge = [e for e in edges if (e[0] in spanned_vertices or e[1] in spanned_vertices)][0]

        mst += [min_edge]

        if (min_edge[0] in spanned_vertices):
            spanned_vertices += [min_edge[1]]
        else:
            spanned_vertices += [min_edge[0]]

        removed_edges = [e for e in edges if (e[0] in spanned_vertices and e[1] in spanned_vertices)]
        edges = [e for e in edges if e not in removed_edges]

    return mst

def MST_kruskal(edges, num_of_vertices):
    pass

    spanned_vertices = [0]

    for t in range(num_of_vertices - 1):
        min_edge = [e for e in edges if (e[0] in spanned_vertices or e[1] in spanned_vertices)][0]

        mst += [min_edge]

        if (min_edge[0] in spanned_vertices):
            spanned_vertices += [min_edge[1]]
        else:
            spanned_vertices += [min_edge[0]]

        removed_edges = [e for e in edges if (e[0] in spanned_vertices and e[1] in spanned_vertices)]
        edges = [e for e in edges if e not in removed_edges]

    return mst

def eu107(graph):
    edges = []
    num_of_vertices = len(graph)


    for i in range(num_of_vertices):
        for j in range(i + 1, num_of_vertices):
            if (graph[i][j] != '-'):
                edges += [(int(graph[i][j]), i, j)]

    edges = sorted(edges)
    edges = [(i, j, w) for (w, i, j) in edges]

    tot_weight = sum([w for (i, j, w) in edges])
    mst = MST_prim(edges, num_of_vertices)
    mst_weight = sum([w for (i, j, w) in mst])

    return tot_weight - mst_weight
            
if __name__ == "__main__":
    startTime = time.clock()
    fsock = open("eu107.txt", "r")
    graph = fsock.readlines()
    fsock.close()
    graph = [n.replace("\n", "") for n in graph]
    graph = [l.split(",") for l in graph]
    print (eu107(graph))
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
