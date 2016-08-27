graph = {}
A = {}

with open("dijkstraData.txt") as f:
    for line in f:
        line = line.split()
        key = int(line[0])
        values = [value.split(',') for value in line[1:]]
        for i in range(0, len(values)):
            values[i][0], values[i][1] = int(values[i][0]), int(values[i][1])
        graph[key] = values

X = [1]
A[1] = 0



while len(X) < len(graph):
    
    vertices = []
    distances = []
    for node in X:
        for tup in graph[node]:
            vertex = tup[0]
            distance = tup[1]
            if vertex not in X:
                vertices.append(vertex)
                distances.append(A[node] + distance)
    greedy_distance = min(distances)
    greedy_vertex = vertices[distances.index(greedy_distance)]
    X.append(greedy_vertex)
    A[greedy_vertex] = greedy_distance

print A[7], A[37], A[59], A[82], A[99], A[115], A[133], A[165], A[188], A[197]
                


    



            

