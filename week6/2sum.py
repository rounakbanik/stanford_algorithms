#Extremely long program. 

content = {}

with open('2Sum.txt') as f:
    for line in f:
        integer = int(line)
        content[integer] = integer

checker = 0

for i in range(-10000, 10001):
	for num in content:
		if i-num in content:
			checker = checker + 1
			break

print checker



	
	


