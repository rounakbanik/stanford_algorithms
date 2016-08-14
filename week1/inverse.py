def sortandcount(l):
    if len(l) <= 1:
        return 0
    l1 = l[:len(l)/2]
    l2 = l[len(l)/2:]
    na = sortandcount(l1)
    nb = sortandcount(l2)
    nc = mergeandcount(l1, l2)

    return na + nb + nc

def mergeandcount(l1, l2):
    l1 = sorted(l1)
    l2 = sorted(l2)

    count = 0
    x=0
    y=0
    sort = []

    while x < len(l1) and y< len(l2):
        if l1[x] < l2[y]:
            sort.append(l1[x])
            x= x+1
        else:
            sort.append(l2[y])
            y= y+1
            count = count + len(l1) - x
    while x < len(l1):
        sort.append(l1[x])
        x=x+1
    while y < len(l2):
        sort.append(l2[y])
        y=y+1
    return count
            
        
                   
                   
    

content = []

with open('IntegerArray.txt') as f:
	content = f.read().splitlines()

content = [int(i) for i in content]

print sortandcount(content)




