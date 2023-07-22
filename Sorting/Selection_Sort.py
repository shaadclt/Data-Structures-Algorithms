def selection_sort(list):
    
    l = len(list)
    for i in range(l):
        min_idx = i
        for j in range(i+1,l):
            if list[min_idx] > list[j]:
                min_idx = j
                
        list[i],list[min_idx] = list[min_idx],list[i]
        
        
list = [9,3,7,1,6,3,9]
selection_sort(list)

print("Sorted List:")
for i in range(len(list)):
    print(list[i],end=" ") 