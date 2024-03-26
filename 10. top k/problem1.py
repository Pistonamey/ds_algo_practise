# return the top K largest elements from the unsorted array
from heapq import *

# top k elements algorithm
def top_k_largest(nums,k):
    result=[]
    heapify(result)
    for i in range(k):
        heappush(result,nums[i])
    
    for i in range(k,len(nums)):
        if(nums[i]>result[0]):
            heappop(result)
            heappush(result,nums[i])
    


    return result

def main():
    print("Here are the top K elements: "+str(top_k_largest([3,1,5,12,2,11],3)))

main()
