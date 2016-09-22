def Merge(a,b):
	m = len(a)
	n = len(b)
	i=0
	j=0
	c = []

	while i<m and j<n:
		if a[i][2] > b[j][2]:
			c.append(a[i])
			i = i+1
		elif a[i][2] == b[j][2]:
			if a[i][0] >= b[j][0]:
				c.append(a[i])
				i = i+1
			else:
				c.append(b[j])
				j = j+1
		else:
			c.append(b[j])
			j = j+1

	while i<m:
		c.append(a[i])
		i = i+1
	while j<n:
		c.append(b[j])
		j=j+1

	return c

def MergeSort(array):
	length = len(array)

	if length == 0:
		return []
	elif length == 1:
		return array
	else:
		mid = length/2
		a = array[:mid]
		b = array[mid:]
		a = MergeSort(a)
		b = MergeSort(b)
		c = Merge(a,b)
	return c


main = []
line_counter = 1

with open("jobs.txt") as f:
	for line in f:
		if line_counter > 1:
			line = line.split()
			line = [int(i) for i in line]
			line = line + [(line[0]+0.0)/line[1]]
			#line = line + [line[0] - line[1]]
			main.append(line)
		line_counter = line_counter + 1

sort_main = MergeSort(main)
length = 0
answer = 0

for arr in sort_main:
        length = length + arr[1]
        answer = answer + arr[0]*length

print answer
        


