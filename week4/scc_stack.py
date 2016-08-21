graph = {}
reverse = {}

def DFSLoop(graph):
    global t
    t = 0
    global s
    s = None
    global explored
    explored = {}
    global leader
    leader = {}
    global f
    f = {}
    for i in range(875714, 0, -1):
        if i not in explored:
            s = i
            DFSStack(graph, i)

def DFSStack(graph, i):
    global t
    path = []
    stack = [i]
    while stack != []:
        #print stack
        #print path
        v= stack[-1]
        if v not in path:
            #print "explored: " + str(v)
            explored[v] = True
            if s not in leader:
                leader[s] = [v]
            else:
                leader[s].append(v)
            path.append(v)
        checker = False
        if v in graph:
            for w in reversed(graph[v]):
                if w not in path:
                    if w not in explored:
                        checker = True
                        stack.append(w)
        if not checker:
            t= t+ 1
            f[v] = t
            stack.pop()
            if t%1000 ==0:
                print "T state: " + str(t)
            #print "popped: " + str(temp)
            #print "v,t: " + str(v) + " " + str(t)
            

def Construct(graph, f):
    leader_graph = {}

    for key in reverse:
        if key in graph:
            if f[key] not in leader_graph:
                leader_graph[f[key]] = []
                for ele in graph[key]:
                    leader_graph[f[key]].append(f[ele])
            else:
                for ele in graph[key]:
                    leader_graph[f[key]].append(f[ele])
            
    return leader_graph  
            
    
print "Start program"
with open("SCC.txt") as f:
    for line in f:
        line = line.split()
        line = [int(i) for i in line]
        if line[1] not in graph:
            graph[line[1]] = [line[0]]
        else:
            graph[line[1]].append(line[0])

        if line[0] not in reverse:
            reverse[line[0]] = [line[1]]
        else:
            reverse[line[0]].append(line[1])
            

print "File loaded"
DFSLoop(reverse)
print "First loop completed"
reverse_graph= Construct(graph, f)
print "Reverse graph constructed"
DFSLoop(reverse_graph)
print "Second loop constructed"

board = [len(leader[x]) for x in leader]
board.sort(reverse= True)
print board[:5]

