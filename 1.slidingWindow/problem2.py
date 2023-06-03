# Smallest Subarray with a given sum

# Q - Given an array of positive numbers and a positive number ‘S’, find the length
#     of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
#     Return 0, if no such subarray exists.

# O/P : length of the smallest subarray whose sum >= 'S'.

def smallestLength(arr, S):
    smallest_length=float("inf")
    current_sum=0
    window_start=0

    for window_end in range(len(arr)):
        current_sum+=arr[window_end]

        while(current_sum>=S):
            smallest_length=min(smallest_length,window_end-window_start+1)
            current_sum-=arr[window_start]
            window_start+=1
    
    return smallest_length
print(smallestLength([2,1,5,2,3,2],7))
