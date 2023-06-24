def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
    cur_sum = 0
    window_start = 0
    index = 0
    max_sum = 0

    for window_end in range(len(customers)):
        if grumpy[window_end] == 1:
            cur_sum += customers[window_end]
        if window_end >= minutes:
            # Remove customers only if the owner was grumpy
            if grumpy[window_start] == 1:
                cur_sum -= customers[window_start]
            window_start += 1
        if cur_sum > max_sum:
            index = window_start
            max_sum = cur_sum

    for i in range(index, index+minutes):
        grumpy[i] = 0
    ans = 0
    for j in range(len(grumpy)):
        if(grumpy[j] == 0):
            ans += customers[j]
    return ans
