graph = {}
line_counter = 1
V = []

with open("edges.txt") as f:
	for line in f:
		if line_counter == 1:
			line = line.split()
			for i in range(1,int(line[0]) +1):
				graph[i] = []
				V.append(i)

		if line_counter > 1:
			line = line.split()
			line = [int(i) for i in line]
			graph[line[0]].append([line[1], line[2]])
			graph[line[1]].append([line[0], line[2]])
		line_counter = line_counter + 1

X=[1]
T=[]

while sorted(X) != sorted(V):

        edge_array = []
        for ele in X:
                for node in graph[ele]:
                        if node[0] not in X:
                                edge_array.append([ele] + node)

        edge = min(edge_array, key= lambda k:k[2])
        T.append(edge)
        X.append(edge[1])

answer = 0

for ele in T:
        answer = answer + ele[2]
print answer                
                
        
