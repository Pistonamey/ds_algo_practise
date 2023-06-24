def search_in_bitonic(arr, k):
    l = 0
    r = len(arr)-1

    while(l < r):
        mid = l+(r-l)//2
        if(arr[mid] > arr[mid+1]):
            r = mid
        else:
            l = mid+1

    index = l

    l = 0
    r = index
    while(l+1 < r):
        mid = l+(r-l)//2

        if(arr[mid] == k):
            return mid
        elif(arr[mid] > k):
            r = mid
        else:
            l = mid

    if(arr[l] == k):
        return l
    if(arr[r] == k):
        return r

    l = index+1
    r = len(arr)-1
    while(l+1 < r):
        mid = l+(r-l)//2
        if(arr[mid] == k):
            return mid
        elif(arr[mid] > k):
            l = mid
        else:
            r = mid

    if(arr[l] == k):
        return l
    if(arr[r] == k):
        return r

    return -1


print(search_in_bitonic([1, 3, 8, 4, 3], 4))
print(search_in_bitonic([3, 8, 3, 1], 8))
print(search_in_bitonic([1, 3, 8, 12], 12))
print(search_in_bitonic([10, 9, 8], 10))
