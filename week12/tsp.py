#Works only for upto 22 points on an Ubuntu 32 bit system with 4 GB RAM.
#Therefore, you'll have to run the program on a subset of 22 points. We have to examine the dataset closely.
#City 1 and 2 are extremely close. Remove City 1. Later, we can use combinatorics to calculate a minimum value
#Plot the points on a graph and remove the interior, insignificant points. This iteration is to detect the last city to be visited. 
#The last city the salesman visits in the subset of 24 points (excluding 1) is 6.
#From graph, it is clear that the traversing order is 2->5->...->6->2
#City 10 and 11 are close. City 10 points to City 6. Remove City 10 (We can remove 10->6 and add 11->6, 11->10 later)
#We now have a set of 22 cities. Run algorithm with City 6 as starting node.
#For the original data set, calculate all edge lengths.
#Subtract 11->6. Add 11->10 and 10->6
#Remove 6->5. 
#Add 1->2
#Add 2->5 and 6->1. Store as answer1
#Add 2->1 and 6->2. Store as answer2
#Return the smaller of the two answers (answer2)

from math import sqrt
from collections import defaultdict
import itertools
from copy import deepcopy
import resource

def Euclid(point1, point2):
	return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def printA(A):
	for key in A:
		print key


graph = {}
points = {}
line_counter = 1

with open("exam.txt") as f:
	for line in f:
		line = [float(i) for i in line.split()]

		if line_counter == 1:
			n = int(line[0])
		else:
			points[line_counter-1] = line
			graph[line_counter-1] = {}
		line_counter = line_counter + 1

for city1 in points:
	for city2 in points:
		if city1 != city2:
			distance = Euclid(points[city1], points[city2])
			graph[city1][city2] = distance
			graph[city2][city1] = distance


A= {}
A = defaultdict(lambda: float('inf'), A)
cities = set([int(i) for i in range(1,n+1)])
to_travel = set([int(i) for i in range(2,n+1)])

A[str({1})+","+str(1)] = 0
first_check = True

for m in range(2, n+1):
	
	subset_list = map(set, itertools.combinations(to_travel, m-1))
	B={}
	B = defaultdict(lambda: float('inf'), B)

	for subset in subset_list:
		subset.add(1)

		for j in subset:
			if j != 1:
				mini = float('inf')
				key = ""
				winner_array = []
				for k in subset:
					if k != j:
						temp = A[str(subset-{j})+","+str(k)] + graph[k][j]
						if mini > temp:
							mini = temp
							key = str(subset-{j})+","+str(k)

				B[str(subset)+","+str(j)] = mini

	reqd_set = eval(min(B, key=B.get)[:-2])
	A.clear()
	A = B

B = {}
cities = set([i for i in range(2,n+1)] + [1])

answer_array = []
answer = float('inf')
for j in range(2,n+1):
	answer_array.append(A[str(cities)+","+str(j)] + graph[j][1])
	if answer > A[str(cities)+","+str(j)] + graph[j][1]:
		answer = A[str(cities)+","+str(j)]+graph[j][1]
		ans_key = j

print min(answer_array)