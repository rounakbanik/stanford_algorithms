def find_parent(ele_num):
	if ele_num% 2 == 1:
		return ele_num/2
	return ele_num/2 - 1

def find_children(ele_num):
	return 2*ele_num + 1, 2*ele_num + 2

def insertmax(hlow, num):
	hlow.append(num)
	ele_num = len(hlow) - 1

	while ele_num > 0:
		if num > hlow[find_parent(ele_num)]:
			hlow[ele_num], hlow[find_parent(ele_num)] = hlow[find_parent(ele_num)], hlow[ele_num]
			ele_num = find_parent(ele_num)
		else:
			return hlow
	return hlow

def insertmin(hhigh, num):
	hhigh.append(num)
	ele_num = len(hhigh) - 1

	while ele_num > 0:
		if num < hhigh[find_parent(ele_num)]:
			hhigh[ele_num], hhigh[find_parent(ele_num)] = hhigh[find_parent(ele_num)], hhigh[ele_num]
			ele_num = find_parent(ele_num)
		else:
			return hhigh
	return hhigh

def deletemax(hlow):
	index = len(hlow) - 1
	hlow[index], hlow[0] = hlow[0], hlow[index]
	hlow.pop()
	ele_num = 0

	while 2*ele_num +1 < index:
		c = find_children(ele_num)

		if c[1] > index-1:
			hlow.append(-1* float("inf"))
		if hlow[ele_num] < hlow[c[0]] or hlow[ele_num] < hlow[c[1]]:
			maxi_index = hlow.index(max(hlow[c[0]], hlow[c[1]]))
			hlow[ele_num], hlow[maxi_index] = hlow[maxi_index], hlow[ele_num]
			ele_num = maxi_index
		else:
			if hlow[-1] == -1*float("inf"):
				hlow.pop()
			return hlow
	if hlow[-1] == -1*float("inf"):
		hlow.pop()
	return hlow

def deletemin(hhigh):
	index = len(hhigh) - 1
	hhigh[index], hhigh[0] = hhigh[0], hhigh[index]
	hhigh.pop()
	ele_num = 0

	while 2*ele_num + 1 < index:
		c = find_children(ele_num)

		if c[1] > index-1:
			hhigh.append(float("inf"))
		if hhigh[ele_num] > hhigh[c[0]] or hhigh[ele_num] > hhigh[c[1]]:
			mini_index = hhigh.index(min(hhigh[c[0]], hhigh[c[1]]))
			hhigh[ele_num], hhigh[mini_index] = hhigh[mini_index], hhigh[ele_num]
			ele_num = mini_index
		else:
			if hlow[-1] == float("inf"):
				hhigh.pop()
			return hhigh
	if hhigh[-1] == float("inf"):
		hhigh.pop()
	return hhigh                     
					
median_sum = 0
hlow = []
hhigh = []
median_arr = []
vertices = []
with open("Median.txt") as f:
	for line in f:
		num = int(line)
		vertices.append(num)
		if len(hlow) == 0 and len(hhigh) == 0:
			hlow.append(num)
			median_sum = median_sum + hlow[0]
			median_arr.append(median_sum)
		else:
			if len(hlow) > 0:
				maxi = hlow[0]
			else:
				maxi = -1*float("inf")
			if len(hhigh) > 0:
				mini = hhigh[0]
			else:
				mini = float("inf")

			if num < maxi:
				hlow = insertmax(hlow, num)
			elif num > mini:
				hhigh = insertmin(hhigh, num)
			else:
				hlow = insertmax(hlow, num)

			if len(hlow) > len(hhigh) + 1:
				ele = hlow[0]
				hlow = deletemax(hlow)
				if -1*float("inf") in hlow:
					hlow.remove(-1*float("inf"))
				hhigh = insertmin(hhigh, ele)
			elif len(hhigh) > len(hlow) + 1:
				ele = hhigh[0]
				hhigh = deletemin(hhigh)
				if float("inf") in hhigh:
					hhigh.remove(float("inf"))
				hlow = insertmax(hlow, ele)

			if len(hlow)> len(hhigh):
				median_sum = median_sum + hlow[0]
				median_arr.append(median_sum)
			elif len(hhigh) > len(hlow):
				median_sum = median_sum + hhigh[0]
				median_arr.append(median_sum)
			else:
				median_sum = median_sum + hlow[0]
				median_arr.append(median_sum)
			
			
		


print median_sum%10000


