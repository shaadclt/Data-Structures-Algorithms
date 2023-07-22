def merge_sort(list):
    if len(list) > 1:
        
        mid = len(list)//2
        
        L = list[:mid]
        R = list[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i=j=k=0
        
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1
            
        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1


list = [8,2,6,3,9,4,1,5]
merge_sort(list)
print("Sorted List:")
for i in range(len(list)):
    print(list[i],end=" ")               