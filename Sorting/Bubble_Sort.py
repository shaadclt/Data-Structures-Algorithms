def bubble_sort(list):
    
    l = len(list)
    for i in range(l):
        swapped = False
        for j in range(l-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1],list[j]
                swapped = True
        if swapped == False:
            break
        
        
list = [8,4,1,7,3,6]
bubble_sort(list)

print("Sorted list:")
for i in range(len(list)):
    print(list[i], end=' ')