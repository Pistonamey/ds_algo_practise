#find the closest element to the target

def find_closest(nums,k):
    l,r=0,len(nums)-1
    while(l+1<r):
        mid=l+(r-l)//2
        if(nums[mid]==k):
            return k
        elif(nums[mid]>k):
            r=mid
        else:
            l=mid
    
    if(abs(k-nums[l])<abs(k-nums[r])):return nums[l]
    else:
        return nums[r]

print(find_closest([1,4,5,7,8,9],6))

