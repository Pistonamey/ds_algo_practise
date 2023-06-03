# No repeat Substring
# Q - Given a String, find the length of a longest substring which has
#     no repeating characters.

# Length of longest no repeating characters sequence

def noRepeat(arr):
    windowStart=0
    maxl=0
    characterIndex={}
    for windowEnd in range(len(arr)):
        right=arr[windowEnd]

        if right in characterIndex:
            windowStart=max(windowStart,characterIndex[right]+1)
        
        characterIndex[right]=windowEnd
        maxl=max(maxl,windowEnd-windowStart+1)
    
    return maxl

print(noRepeat("aabccbb"))