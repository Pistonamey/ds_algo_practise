def min_diff(arr,key):
    l=0
    r=len(arr)-1

    while(l+1<r):
        mid=l+(r-l)//2
        if(arr[mid]==key):
            return key
        elif(arr[mid]>key):
            r=mid
        else:
            l=mid
    
    if(abs(key-arr[l])<abs(key-arr[r])):
        return arr[l]
    else:
        return arr[r]

print(min_diff([4,6,10],7))
print(min_diff([4,6,10],4))
print(min_diff([1,3,8,10,15],12))
print(min_diff([4,6,10],17))