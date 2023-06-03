# Fruits into Baskets

# Q - Given an array of characters where each character represents a fruit tree,
#     you are given two baskets and your goal is to put maximum number of fruits
#     in each basket. The only restriction is that each basket can have only one
#     type of fruit.

# O/p: maximum NUMBER of fruits in both the baskets:

def maxFruits(arr):
    windowStart = 0
    maxl = 0
    fruits = {}

    for windowEnd in range(len(arr)):
        right = arr[windowEnd]
        fruits[right] = 1+fruits.get(right, 0)

        while len(fruits) > 2:
            left = arr[windowStart]
            fruits[left] -= 1
            windowStart += 1
            if(fruits[left] == 0):
                del fruits[left]
        maxl = max(maxl, windowEnd-windowStart+1)

    return maxl


print(maxFruits(['A', 'B', 'C', 'A', 'C']))
