# Longest Substring with Same Letters after Replacement

# Q - Given a string with lowercase letters only, if you are allowed
#     to replace no more than ‘k’ letters with any letter, find the
#     length of the longest substring having the same letters after replacement.

# O/P: length of longest subsequence after replacement.

def replacement(s,k):
    windowStart = 0
    maxl = 0
    maxRepeatingCharacterFreq = 0
    characterFreq = {}

    for windowEnd in range(len(s)):
        right = s[windowEnd]
        characterFreq[right] = 1+characterFreq.get(right, 0)

        maxRepeatingCharacterFreq = max(
            maxRepeatingCharacterFreq, characterFreq[right])

        if(windowEnd-windowStart+1 - maxRepeatingCharacterFreq>k):
            left=s[windowStart]
            characterFreq[left]-=1
            windowStart+=1
        maxl=max(maxl,windowEnd-windowStart+1)
    return maxl

print(replacement("aabccbb",2))