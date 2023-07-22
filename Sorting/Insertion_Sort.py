def insertion_sort(list):
    
    for i in range(1,len(list)):
        
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = key
        
        
list = [4,1,8,2,5,9,3]
insertion_sort(list)
print("Sorted List:")
for i in range(len(list)):
    print(list[i],end=" ")