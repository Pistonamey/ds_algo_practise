# Longest Substring with K Distinct Characters

# Q - Given a string, find the length of the longest
#     substring in it with no more than K distinct characters.

# O/P : longest substring in it with no more than K distinct characters.


def longestSubstring(arr, k):
    windowStart = 0
    characters = {}
    maxl = 0
    for windowEnd in range(len(arr)):
        right = arr[windowEnd]
        characters[right] = 1+characters.get(right, 0)

        while len(characters) > k:
            left = arr[windowStart]
            characters[left] -= 1
            windowStart += 1
            if(characters[left] == 0):
                del characters[left]
        maxl = max(maxl, windowEnd-windowStart+1)
    return maxl


print(longestSubstring(['a', 'r', 'a', 'a', 'c', 'i'], 2))
