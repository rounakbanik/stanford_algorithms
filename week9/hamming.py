def xor(a,b):
    y = int(a,2) ^ int(b,2)
    return  '{0:b}'.format(y)

graph1 = {}
graph2 = {}
clusters = []
line_counter = 1

with open("clustering_big.txt") as f:
    for line in f:
        line = line.split()
        if line_counter == 1:
            line = [int(i) for i in line]
            nodes_size = line[0]
            size = line[1]
        else:
            line = ''.join(line)
            if line in graph1:
                graph1[line].append(line_counter-1)
            else:
                graph1[line] = [line_counter-1]

            graph2[line_counter-1] = line

        line_counter = line_counter + 1

mask_0 = [["0" for i in range(0,size)]]
mask_1 = []
mask_2 = []

for i in range(0,size):
    dummy = ['0' for k in range(0,size)]
    dummy[i] = '1'
    dummy = ''.join(dummy)
    mask_1.append(dummy)

for i in range(0, size):
    for j in range(i+1, size):
        dummy = ['0' for k in range(0,size)]
        dummy[i] = '1'
        dummy[j] = '1'
        dummy = ''.join(dummy)
        mask_2.append(dummy)


for hamstring in graph1:
    if len(graph1[hamstring]) > 1:
        clusters.append(graph1[hamstring])


counter = 0

for node in graph2:
    print counter
    counter = counter + 1
    #print "Nodehr: " + str(node)
    for mask in mask_1:
        #print "Mask: " + str(mask)
        other_hamstring = xor(graph2[node], mask)
        if len(other_hamstring) != size:
            other_hamstring = (size- len(other_hamstring))*'0' + other_hamstring
        #print "Other hamstring: " + str(other_hamstring)
        if other_hamstring in graph1:
            other_nodes = graph1[other_hamstring]
            #print "Other hamstring: " + str(other_hamstring)
            #print "Other nodes: " + str(graph1[other_hamstring])
        else:
            continue

        for other_node in other_nodes:
            v1= node
            v2 = other_node

            found1= False
            found2 = False
            for cluster in clusters:
                if v1 in cluster:
                    merger1 = clusters[clusters.index(cluster)]
                    found1 = True
                if v2 in cluster:
                    merger2 = clusters[clusters.index(cluster)]
                    found2 = True

                if found1 and found2:
                    break

            if found1 and found2:
                if merger1 != merger2:
                    merger = merger1 + merger2
                    clusters.pop(clusters.index(merger1))
                    clusters.pop(clusters.index(merger2))
                    clusters.append(merger)
            elif not found1 and not found2:
                clusters.append([v1,v2])
            elif not found1 and found2:
                merger = [v1] + merger2
                clusters.pop(clusters.index(merger2))
                clusters.append(merger)
            elif found1 and not found2:
                merger = [v2] + merger1
                clusters.pop(clusters.index(merger1))
                clusters.append(merger)

#print clusters
counter = 0

for node in graph2:
    print counter
    counter = counter + 1
    for mask in mask_2:
        other_hamstring = xor(graph2[node], mask)
        if len(other_hamstring) != size:
            other_hamstring = (size- len(other_hamstring))*'0' + other_hamstring
        if other_hamstring in graph1:
            other_nodes = graph1[other_hamstring]
            #print "Node: " + str(node)
            #print "Other Nodes: " + str(other_nodes)
        else:
            continue

        for other_node in other_nodes:
            v1= node
            v2 = other_node

            found1= False
            found2 = False
            for cluster in clusters:
                if v1 in cluster:
                    merger1 = clusters[clusters.index(cluster)]
                    found1 = True
                if v2 in cluster:
                    merger2 = clusters[clusters.index(cluster)]
                    found2 = True

                if found1 and found2:
                    break

            if found1 and found2:
                if merger1 != merger2:
                    merger = merger1 + merger2
                    clusters.pop(clusters.index(merger1))
                    clusters.pop(clusters.index(merger2))
                    clusters.append(merger)
            elif not found1 and not found2:
                clusters.append([v1,v2])
            elif not found1 and found2:
                merger = [v1] + merger2
                clusters.pop(clusters.index(merger2))
                clusters.append(merger)
            elif found1 and not found2:
                merger = [v2] + merger1
                clusters.pop(clusters.index(merger1))
                clusters.append(merger)
        #print clusters

print len(clusters)
print clusters
x=0
for cluster in clusters:
    x = x+ len(cluster)

isolate = nodes_size - x
print len(clusters) + isolate
