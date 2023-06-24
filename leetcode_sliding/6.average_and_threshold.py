def numOfSubarrays(self, arr, k: int, threshold: int) -> int:
    cur_average = 0
    res = 0
    window_start = 0
    cur_sum = 0
    for window_end in range(len(arr)):
        cur_sum += arr[window_end]
        cur_average = cur_sum//(window_end-window_start+1)

        if(window_end >= k-1):
            if(cur_average >= threshold):
                res += 1
            cur_sum -= arr[window_start]
            window_start += 1
    return res
