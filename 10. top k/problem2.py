#given an unsorted array return the kth smallest number
from heapq import *

def find_kth_smallest_number(nums,k):
    heap=[]
    heapify(heap)

    for i in range(k):
        heappush(heap,-nums[i])
    
    for i in range(k,len(nums)):
        if(-nums[i]>heap[0]):
            heappop(heap)
            heappush(heap,-nums[i])
    return -heap[0]

def main():
    print("Kth smalled number is: "+str(find_kth_smallest_number([1,5,12,2,11,5],3)))
    print("Kth smalled number is: "+str(find_kth_smallest_number([1,5,12,2,11,5],4)))
main()