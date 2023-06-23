def heapify(data, n, i):
    max = i
    left = 2 *i + 1
    right = 2 *i + 2
    
    if left < n and data[left] > data[max]:
        max = left
    if right < n and data[right] > data[max]:
        max = right
    if max != i:
        data[i], data[max] = data[max], data[i]

        heapify(data,n,max)
 
def heapsort(data):
    n = len(data)

    for i in range(n//2, -1,-1):
        heapify(data,n-1,i)
    for i in range(n-1, -1,-1):
        data[i], data[0] = data[0], data[i]
        heapify(data,i-1, 0)




l = [2,3,4,33,4,5]
heapsort(l)
print(l)

import heapq

heapq.heapify(l)