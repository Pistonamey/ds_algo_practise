# Smallest Subarray with a given sum

# Q - Given an array of positive numbers and a positive number ‘S’, find the length
#     of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
#     Return 0, if no such subarray exists.

# O/P : length of the smallest subarray whose sum >= 'S'.

def smallestLength(arr, S):
    smallestLength = float("inf")

    windowStart = 0
    windowSum = 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowSum >= S:
            smallestLength = min(windowEnd-windowStart+1, smallestLength)
            windowSum -= arr[windowStart]
            windowStart += 1
            while(windowSum >= S):
                smallestLength = min(windowEnd-windowStart+1, smallestLength)
                windowSum -= arr[windowStart]
                windowStart += 1

    return smallestLength

print(smallestLength([2,1,5,2,3,2],7))
