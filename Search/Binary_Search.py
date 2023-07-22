def binary_search(list,l,r,n):
    while l<=r:
        mid = (l+(r-1))//2
        
        if list[mid] == n:
            return mid
        elif list[mid] < n:
            l = mid + 1
        else:
            r = mid - 1
    return -1


list = [3,6,9,11,45,67,89,93]
n = 67

result = binary_search(list,0,len(list)-1,n)
if result != -1:
    print("Element found at index",result)
else:
    print("Element not found")
    