content = []

with open('QuickSort.txt') as f:
	content = f.read().splitlines()

content = [int(i) for i in content]

length = len(content)
num_com = 0

def quicksort(A, length):
    global num_com
    num_com = num_com + length - 1
    x = [], 0
    y =[], 0
    if length == 1:
        return A, num_com
    p = A[0]
    i = 1
    for j in range(1, length):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i = i + 1
    A[0], A[i-1] = A[i-1], A[0]
    m1 = len(A[:i-1])
    m2 = len(A[i:])
    if m1> 0:
        x =quicksort(A[:i-1], m1)
        #num_com = num_com + m1 - 1
    if m2 > 0:
        y=quicksort(A[i:], m2)
        #num_com = num_com + m2 -1
        
    return x[0] + [p] + y[0], num_com


print quicksort(content, length)[1]


