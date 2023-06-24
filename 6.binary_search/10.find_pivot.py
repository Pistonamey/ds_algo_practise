def find_pivot(arr):
    l=0
    r=len(arr)-1

    while(l<r):
        mid=l+(r-l)//2
        if(mid<r and arr[mid]>arr[mid+1]):
            return mid+1
        if(mid>l and arr[mid-1]>arr[mid]):
            return mid
    
        if(arr[l]<arr[mid]):
            l=mid+1
        else:
            r=mid-1
    
    return 0

print(find_pivot([10, 15, 1, 3, 8]))
print(find_pivot([4, 5, 7, 9, 10, -1, 2]))
print(find_pivot([1, 3, 8, 10]))