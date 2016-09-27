import copy
from operator import itemgetter

def GetGraph(filename):
    line_counter = 1

    graph= {}
    lookup = {}
    indegree = {}

    with open(filename) as f:
        for line in f:
            line = [int(i) for i in line.split()]
            if line_counter == 1:
                n, m = line[0], line[1]

                for i in range(1, n+1):
                    graph[i] = {}
                    lookup[i] = []
                    indegree[i] = {}
            else:
                tail, head, cost = line[0], line[1], line[2]
                graph[tail][head] = cost
                lookup[tail].append(head)
                indegree[head][tail] = cost

            line_counter = line_counter + 1

    return graph, lookup, indegree, n

def AddS(graph, indegree, lookup, n, graph_dash, indegree_dash, lookup_dash):

    graph_dash[0] = {}
    lookup_dash[0]= []
    indegree_dash[0] = {}

    for node in graph:
        graph_dash[0][node] = 0
        lookup_dash[0].append(node)
        indegree_dash[node][0] = 0

    return graph_dash, lookup_dash, indegree_dash

def BellmanFord(graph_dash, indegree_dash, lookup_dash, n, graph,source=0):

    A={}

    A["0,"+str(source)] = 0

    for v in graph:
        A["0,"+str(v)] = float('inf')

    for i in range(1,n+1):
        for v in graph_dash:
            item1 = A[str(i-1)+","+str(v)]

            in_nodes = indegree_dash[v]
            in_array = []

            if len(in_nodes) > 0:
                for in_node in in_nodes:
                    in_array.append(A[str(i-1)+","+str(in_node)]+ in_nodes[in_node])
                item2 = min(in_array)

                item = min(item1, item2)
                A[str(i)+","+str(v)] = item
            else:
                A[str(i)+","+str(v)] = item1

    for v in graph:
       if A[str(n-1)+","+str(v)] != A[str(n)+","+str(v)]:
           return "Negative Cycle"

    p = {}
    for v in graph: 
        p[v] =A[str(n-1)+","+str(v)]

    return p

data = GetGraph("exam.txt")
graph, lookup, indegree, n = data[0], data[1], data[2], data[3]

graph_dash, lookup_dash, indegree_dash = copy.deepcopy(graph), copy.deepcopy(lookup), copy.deepcopy(indegree)

AddS(graph, indegree, lookup, n, graph_dash, indegree_dash, lookup_dash)
p= BellmanFord(graph_dash, indegree_dash, lookup_dash, n, graph,0)

if p != "Negative Cycle":
    print min(p.values())
else:
    print p




