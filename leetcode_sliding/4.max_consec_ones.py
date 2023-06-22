class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length=0
        current_length=0

        for window_end in range(len(nums)):
            if(nums[window_end]==1):
                current_length+=1
            else:
                max_length=max(max_length,current_length)
                current_length=0
        max_length=max(max_length,current_length)
        return max_length