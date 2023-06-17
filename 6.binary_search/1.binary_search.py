#Find the index of the target in the sorted array

def binary_search(arr,k):
    l=0
    r=len(arr)-1
    while(l+1<r):
        mid=l+(r-l)//2
        if(arr[mid]==k):
            return mid
        elif(arr[mid]<k):
            l=mid
        else:
            r=mid
    
   
    return -1

print(binary_search([5,7,7,8,8,10],8))