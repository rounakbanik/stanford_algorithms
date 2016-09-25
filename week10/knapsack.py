line_counter = 1
items =[[-1,-1]]
A=[]

with open("knapsack.txt") as f:
	for line in f:
		line = line.split()
		line = [int(i) for i in line]
		if line_counter == 1:
			W = line[0]
			n = line[1]
		else:
			items.append(line)
		line_counter = line_counter + 1

A.append([])
for i in range(0,W+1):
	A[0].append(0)

for i in range(1,n+1):
	#print i
	A.append([])
	wi = items[i][1]
	vi = items[i][0]
	for x in range(0,W+1):
		if wi > x:
			A[i].append(A[i-1][x])
		else:
			A[i].append(max(A[i-1][x], A[i-1][x-wi] + vi))

print A[n][W] 
