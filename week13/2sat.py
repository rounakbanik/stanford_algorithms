def Tarjan(graph):

    global index_int
    index_int = 0
    global S
    S = []
    global onstack
    onstack = {}
    global index
    index = {}
    global lowlink
    lowlink = {}
    global components
    components = []

    for v in graph:
        if v not in index:
            strongconnect(v, graph)

    return components

def strongconnect(v, graph):
    global index_int
    index[v] = index_int
    lowlink[v] = index_int
    index_int = index_int + 1
    S.append(v)
    onstack[v] = True


    for w in graph[v]:
        if w not in index:
            strongconnect(w, graph)
            lowlink[v] = min(lowlink[v], lowlink[w])
        elif w in onstack:
            if onstack[w]:
                lowlink[v] = min(lowlink[v], index[w])

    if lowlink[v] == index[v]:
        component = []
        w = S.pop()
        onstack[w] = False
        component.append(w)
        while w != v:
            w = S.pop()
            onstack[w] = False
            component.append(w)

        components.append(component)



line_counter = 1
graph = {}

with open("s1.txt") as f:
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

components = Tarjan(graph)

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
