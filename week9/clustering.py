line_counter = 1
graph = []
clusters = []

with open("clustering.txt") as f:
	for line in f:
		line = line.split()
		line = [int(i) for i in line]
		if line_counter == 1:
			size = line[0]
		else:
			graph.append(line)
		line_counter = line_counter + 1

graph = sorted(graph, key= lambda k:k[2])

for i in range(1,size+1):
	clusters.append([i])


while len(clusters) > 4:
	minimum_edge = graph[0]
	graph.pop(0)
	v1 = minimum_edge[0]
	v2 = minimum_edge[1]

	for cluster in clusters:
		if v1 in cluster:
			merger1 = clusters[clusters.index(cluster)]

		if v2 in cluster:
			merger2 = clusters[clusters.index(cluster)]

	if merger1 != merger2:
		merger = merger1 + merger2
		clusters.pop(clusters.index(merger1))
		clusters.pop(clusters.index(merger2))
		clusters.append(merger)
	
checker = True
while checker:
	minimum_edge = graph[0]
	v1 = minimum_edge[0]
	v2 = minimum_edge[1]

	for cluster in clusters:
		if v1 in cluster and v2 not in cluster:
			checker = False
			break
		elif v1 not in cluster and v2 in cluster:
			checker = False
			break
		elif v1 in cluster and v2 in cluster:
			graph.pop(0)


print graph[0][2]

	

