def linear_search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            return i
    return -1

list = [4,2,6,3,7,8]
n = 3

result = linear_search(list,n)
if result == -1:
    print("Element not found")
else:
    print("Element found at index",result)