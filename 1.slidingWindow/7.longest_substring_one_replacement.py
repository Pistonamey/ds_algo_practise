# Longest Subarray with Ones after Replacement (hard)

# Q - Given an array containing 0s and 1s, if you are allowed
#     to replace no more than ‘k’ 0s with 1s, find the length
#     of the longest contiguous subarray having all 1s.


def replaceZero(arr, k):

    windowStart = 0
    maxl = 0
    maxOneCount = 0

    for windowEnd in range(len(arr)):
        if arr[windowEnd] == 1:
            maxOneCount += 1

        if(windowEnd-windowStart+1 - maxOneCount) > k:
            if(arr[windowStart] == 1):
                maxOneCount -= 1
            windowStart += 1
        maxl = max(windowEnd-windowStart+1, maxl)
    return maxl


print(replaceZero([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
