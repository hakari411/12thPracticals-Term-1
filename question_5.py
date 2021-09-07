#Linear search
def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

#Binary search (array must be a sorted one)
def binary_search(arr,l,r,x):
    if r>=l:
        mid = l + (r-l)//2
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr,l,mid-1,x)
        elif arr[mid] < x:
            return binary_search(arr,mid+1, r,x)
    return -1

