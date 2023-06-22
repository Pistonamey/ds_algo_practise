class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        l, r = 0, 0
        res = 0
        currCost = 0
        while r < n:
            # Calculate the cost of changing s[r] to t[r]
            currCost += abs(ord(s[r]) - ord(t[r]))
            if currCost <= maxCost:  # If the current cost is within the limit
                # Update the maximum length of the valid substring
                res = max(res, r - l + 1)
                r += 1
            else:
                # Update the current cost by removing s[l] from the window
                currCost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
                r += 1
        return res
