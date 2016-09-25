import sys
sys.setrecursionlimit(4000)

line_counter = 1
items = {}
items[0] = -1
A=[]
store = {}

def Calculate(A, i, x, store):
        if str(i)+","+str(x) in store:
                return store[str(i)+","+str(x)], store
        if i==0:
                return 0, store
        else:
                wi = items[i][1]
                vi = items[i][0]
                if wi > x:
                        item= Calculate(A,i-1,x, store)[0]
                        store[str(i)+","+str(x)] = item
                        return item, store
                else:
                        item1 = Calculate(A, i-1, x, store)[0]
                        item2 = Calculate(A, i-1, x-wi, store)[0] + vi
                        item = max(item1, item2)
                        store[str(i)+","+str(x)] = item
                        return item, store             
        

with open("knapsack_big.txt") as f:
	for line in f:
		line = line.split()
		line = [int(i) for i in line]
		if line_counter == 1:
			W = line[0]
			n = line[1]
		else:
			items[line_counter-1] =line
		line_counter = line_counter + 1

A.append([])
print Calculate(A,n,W, store)[0]
