#create a data structure for a stream of numbers and a add function that returns the kth largest element.
from heapq import *

class kthLargestNumberInstream:
    minHeap=[]

    def __init__(self, nums,k):
        self.k=k

        for num in nums:
            self.add(num)
    
    def add(self,num):
        heappush(self.minHeap,num)

        if(len(self.minHeap)>self.k):
            heappop(self.minHeap)
        
        return self.minHeap[0]

def main():
    kth = kthLargestNumberInstream([3,1,5,12,2,11],4)
    print("4th largest number is: "+str(kth.add(6)))
    print("4th largest number is: "+str(kth.add(13)))
    print("4th largest number is: "+str(kth.add(4)))

main()