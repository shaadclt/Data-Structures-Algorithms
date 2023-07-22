def heapify(list,n,i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    
    if l < n and list[largest] < list[l]:
        largest = l
        
    if r < n and list[largest] < list[r]:
        largest = r
    
    if largest != i:
        list[i],list[largest] = list[largest],list[i]
        heapify(list,n,largest)
        
def heap_sort(list):
    n = len(list)
    
    for i in range(n//2-1,-1,-1):
        heapify(list,n,i)
        
    for i in range(n-1,0,-1):
        list[i],list[0] = list[0],list[i]
        heapify(list,i,0)
        
        
        
list = [4,9,6,5,1,8,3,6]
heap_sort(list)
print("Sorted List:")
for i in range(len(list)):
    print(list[i],end=" ")
    