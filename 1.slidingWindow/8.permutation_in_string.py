# Permutation in a String (hard)

# Q - Given a string and a pattern, find out if the string
#     contains any permutation of the pattern.

# O/P : Boolean

def checkPermutation(s, pattern):
    pattern = set(pattern)
    hasit = set()

    for i in range(len(s)):
        if(s[i] in pattern):
            hasit.add(s[i])
            j = i+1
            while(j < len(s)):
                if(s[j] in pattern):
                    hasit.add(s[j])
                    j += 1
                else:
                    break
            if(hasit == pattern):
                return True
            else:
                hasit.clear()

    return False


print(checkPermutation("aaaacb", "abc"))

# Linear Version


def checkPermutation2(s, pattern):
    windowStart = 0
    charFreq = {}
    matched = 0
    for i in range(len(pattern)):
        charFreq[s[i]] = 1+charFreq.get(s[i], 0)

    for windowEnd in range(len(s)):
        right = s[windowEnd]
        if(right in charFreq):
            charFreq[right] -= 1
            if(charFreq[right] == 0):
                matched += 1
        if(matched == len(charFreq)):
            return True
        if(windowEnd >= len(pattern)-1):
            left = s[windowStart]
            windowStart += 1
            if(left in charFreq):
                if(charFreq[left] == 0):
                    matched -= 1
                charFreq[left] += 1
    print(matched)
    return False


print(checkPermutation2("aaaacb", "abc"))
