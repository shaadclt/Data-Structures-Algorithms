def partition(list,low,high):
    
    pivot = list[high]
    i = low - 1
    
    for j in range(low,high):
        if list[j] <= pivot:
            i = i + 1
            
            list[i],list[j] = list[j],list[i]
            
    list[i+1],list[high] = list[high],list[i+1]
    
    return i+1


def quick_sort(list,low,high):
    if low < high:
        pi = partition(list,low,high)
        quick_sort(list,low,pi-1)
        quick_sort(list,pi+1,high)
        

list = [6,3,8,4,7,1,5]
l = len(list)
quick_sort(list,0,l-1)    
print("Sorted List:")
for i in range(l):
    print(list[i],end=" ")    
    