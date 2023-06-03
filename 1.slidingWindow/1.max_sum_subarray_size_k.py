# Maximum Sum Subarray of Size k

# Q - Given an array of positive numbers and a positive number 'k', find the maximum
#     sum of any contigous subarray of size 'k'

def maximumSum(arr, k):
    window_start = 0
    max_sum = 0
    current_sum = 0
    for window_end in range(len(arr)):
        current_sum += arr[window_end]

        if(window_end >= k-1):
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[window_start]
            window_start += 1

    return max_sum


print(maximumSum([2, 1, 5, 1, 3, 2], 3))
