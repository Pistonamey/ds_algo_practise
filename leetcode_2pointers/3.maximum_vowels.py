class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ('a', 'e', 'i', 'o', 'u')
        max_length = 0
        cur_num = 0
        window_start = 0
        for i in range(len(s)):
            if s[i] in vowels:
                cur_num += 1
            if i >= k:
                if s[window_start] in vowels:
                    cur_num -= 1
                window_start += 1

            max_length = max(max_length, cur_num)
        return max_length
