#return the top k elements that occur most frequently

from heapq import *

def find_k_frequent_numbers(nums,k):
    freq={}
    for i in range(len(nums)):
        freq[nums[i]]=1+freq.get(0,nums[i])
    
    heap=[]

    for num,fre in freq.items():
        heappush(heap,(fre,num))
        if(len(heap)>k):
            heappop(heap)
    
    ans=[]
    for i in range(len(heap)):
        ans.append(heap[i][1])
    
    return ans

def main():
    print("Here are the k frequent numbers: "+str(find_k_frequent_numbers([1,3,5,12,11,12,11],2)))
main()