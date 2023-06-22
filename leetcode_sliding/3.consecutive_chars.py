class Solution:
    def maxPower(self, s: str) -> int:
        max_length=0
        cur_length=1
        cur_character=s[0]

        for i in range(1,len(s)):
            if(s[i]==cur_character):
                cur_length+=1
            else:
                max_length=max(max_length,cur_length)
                cur_length=1
                cur_character=s[i]
        max_length=max(max_length,cur_length)
        return max_length