def getAverages(self, nums, k: int):
    window_size = k*2+1
    window_start = 0
    res = []
    index = k
    cur_sum = 0

    for i in range(len(nums)):
        res.append(-1)

    for window_end in range(len(nums)):
        cur_sum += nums[window_end]

        if(window_end-window_start+1 >= window_size):
            cur_avg = cur_sum//window_size
            res[index] = cur_avg
            index += 1
            cur_sum -= nums[window_start]
            window_start += 1

    return res
