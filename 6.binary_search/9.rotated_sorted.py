def rotated_sorted(arr,k):
    l=0
    r=len(arr)-1

    while(l<=r):
        mid=l+(r-l)//2

        if(arr[mid]==k):
            return mid
        
        if(arr[l]<=arr[mid]):
            if(k<arr[mid] and k>=arr[l]):
                r=mid-1
            else:
                l=mid+1
        else:
            if(k>arr[mid] and k<=arr[r]):
                l=mid+1
            else:
                r=mid-1
    return -1


print(rotated_sorted([10, 15, 1, 3, 8],15))
print(rotated_sorted([4, 5, 7, 9, 10, -1, 2],10))
