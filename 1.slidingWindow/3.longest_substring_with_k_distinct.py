# Longest Substring with K Distinct Characters

# Q - Given a string, find the length of the longest
#     substring in it with no more than K distinct characters.

# O/P : length of longest substring in it with no more than K distinct characters.


def longestSubstring(arr, k):
    count_dict = {}
    window_start = 0
    result = 0

    for window_end in range(len(arr)):
        count_dict[arr[window_end]] = 1+count_dict.get(arr[window_end], 0)

        while(len(count_dict) > k):
            count_dict[arr[window_start]] -= 1
            if(count_dict[arr[window_start]] == 0):
                count_dict.pop(arr[window_start])
            window_start += 1
        result = max(result, window_end-window_start+1)

    return result


print(longestSubstring(['a', 'r', 'a','a','c', 'i'], 2))
