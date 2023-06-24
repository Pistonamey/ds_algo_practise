def bitonic_array(arr):
    l=0
    r=len(arr)-1

    while(l<r):
        mid=l+(r-l)//2
        if(arr[mid]>arr[mid+1]):
            r=mid
        else:
            l=mid+1
    
    return arr[l] 

print(bitonic_array([1,3,8,12,4,2]))
print(bitonic_array([3,8,3,1]))
print(bitonic_array([1,3,8,12]))
print(bitonic_array([10,9,8]))