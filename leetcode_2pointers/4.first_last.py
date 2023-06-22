class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.first_occurrence(nums, target), self.last_occurrence(nums, target)]
    
    def first_occurrence(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if l < len(nums) and nums[l] == target:
            return l
        return -1
    
    def last_occurrence(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        if r >= 0 and nums[r] == target:
            return r
        return -1