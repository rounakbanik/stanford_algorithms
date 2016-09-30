from tarjan import tarjan

line_counter = 1
graph = {}

with open("s6.txt") as f:
    for line in f:
        line = [int(i) for i in line.split()]

        if line_counter == 1:
            size = line[0]
            for i in range(-size,size+1):
                if i != 0:
                    graph[i] = []
        else:
            v1 = line[0]
            v2 = line[1]

            graph[-1*v1].append(v2)
            graph[-1*v2].append(v1)

        line_counter = line_counter + 1

components = tarjan(graph)

checker = False

for component in components:
    if checker:
        break
    for ele in component:
        if -1*ele in component:
            print "Unsatisfiable"
            checker = True
            break

if not checker:
    print "Satisfiable"


