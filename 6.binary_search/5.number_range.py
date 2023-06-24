def number_range(arr,k):
    l=0
    r=len(arr)-1

    #first occurence
    while(l+1<r):
        mid=l+(r-l)//2
        if(arr[mid]==k):
            r=mid
        elif(arr[mid]>k):
            r=mid
        else:
            l=mid
    first_occurence=-1
    if(arr[l]==k):
        first_occurence=l
    if(arr[r]==k):
        first_occurence=r
    
    l=0
    r=len(arr)-1

    #last occurence
    while(l+1<r):
        mid=l+(r-l)//2
        if(arr[mid]==k):
            l=mid
        elif(arr[mid]>k):
            r=mid
        else:
            l=mid
    
    last_occurence=-1
    if(arr[r]==k):
        last_occurence=r
    if(arr[l]==k):
        last_occurence=l
    
    return [first_occurence,last_occurence]

print(number_range([4,6,6,6,9],6))
print(number_range([1,3,8,10,15],10))
print(number_range([1,3,8,10,15],12))

    

        