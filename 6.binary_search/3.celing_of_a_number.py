def ceiling(arr, k):
    l = 0
    r = len(arr)-1

    while l+1 < r:
        mid = l+(r-l)//2

        if(arr[mid] == k):
            return mid
        elif(arr[mid] > k):
            r = mid
        else:
            l = mid
    if(k>=0):
        if(abs(k-arr[l]) >= abs(k-arr[r]) and k-arr[l] <= 0):
            print("l")
            return l
        if(abs(k-arr[l]) <= abs(k-arr[r]) and k-arr[r] <= 0):
            print("r")
            return r
    else:
        if(k-arr[l] >= k-arr[r] and k-arr[l] <= 0):
            print("-l")
            return l
        if(k-arr[l] <= k-arr[r] and k-arr[r] <= 0):
            print("-r")
            return r
    return -1


print(ceiling([4, 6, 10], 6))
print(ceiling([1, 3, 8, 10, 15], 12))
print(ceiling([4, 6, 10], 17))
print(ceiling([4, 6, 10], -1))
