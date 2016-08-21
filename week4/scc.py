import sys
graph = {}
reverse = {}

sys.setrecursionlimit(1500000)

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
            DFS(graph, i)
            
def DFS(graph, i):
    global t
    explored[i] = True
    if s not in leader:
        leader[s] = [i]
    else:
        leader[s].append(i)
    
    if i in graph:
        for j in graph[i]:
            if j not in explored:
                DFS(graph, j)

    
    t = t+1
    f[i] = t

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


DFSLoop(reverse)
reverse_graph= Construct(graph, f)
DFSLoop(reverse_graph)

board = [len(leader[x]) for x in leader]
board.sort(reverse= True)
print board[:5]

