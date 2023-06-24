def next_letter(arr,k):
    l=0
    r=len(arr)-1
    if(k<arr[0] or k>arr[r]):
        return arr[0]

    while(l+1<r):
        mid=l+(r-l)//2
        if(arr[mid]>k):
            r=mid
        else:
            l=mid
    return arr[(r)%(len(arr))]

print(next_letter(['a','c','f','h'],'f'))
print(next_letter(['a','c','f','h'],'b'))
print(next_letter(['a','c','f','h'],'m'))