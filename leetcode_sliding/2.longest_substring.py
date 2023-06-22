class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, 0
        res = 0
        structs = set()
        while r < n:
            if s[r] not in structs:
                structs.add(s[r]) #update data structures to add s[r]
                res = max(res, r-l+1)
                r += 1
                
                 #update res if the current window is better
            
            else:
                structs.remove(s[l])
                l +=1
        return res