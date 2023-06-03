from collections import defaultdict

def find_string_anagrams(str, pattern):
    windowStart, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    result_indices = []

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if(matched == len(char_frequency)):
            result_indices.append(windowStart)

        if(windowStart >= len(pattern)-1):
            left_char = str[windowStart]

            windowStart += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    return result_indices


print(find_string_anagrams("ppqp", "pq"))
counter=defaultdict(int)
counter['a']=1
print(counter)