import random
import copy

graph = {}
stored = {}
filename = "kargerMinCut.txt"

def contract(graph, vertex, other_vertex):
    #remove the edge
    graph[vertex] = [x for x in graph[vertex] if x != other_vertex]
    graph[other_vertex] = [x for x in graph[other_vertex] if x != vertex]
    
    #merge the 2 vertices
    graph[vertex] = graph[vertex] + graph[other_vertex]
    graph.pop(other_vertex, None)

    for key in graph:
        for ind, value in enumerate(graph[key]):
            if value == other_vertex:
                graph[key][ind] = vertex
    return graph
    

def getgraph(filename):
    with open(filename) as f:
        for line in f:
            line = line.split()
            line = [int(i) for i in line]
            graph[line[0]] = line[1:]
    return graph


minimum = 0

def karger(filename):
    graph = getgraph(filename)
    

    while len(graph) > 2:
        vertex = random.choice(graph.keys())
        other_vertex = random.choice(graph[vertex])

        graph = contract(graph, vertex, other_vertex)
    length = len(graph.values()[0])
    return length

#Ideally, you should loop 100,000 times. But it's really slow. Looping 100 times
#almost always gets the answer.

for i in range(0,100):
    length = karger(filename)
    if length < minimum or minimum == 0:
        minimum = length
 

#print random.choice(graph.keys())
print minimum

#print contract(graph, 2, 5)
#print contract(graph, 1, 2)
#print contract(graph, 1, 3)
