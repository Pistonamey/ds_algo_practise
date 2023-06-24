def findRepeatedDnaSequences(self, s: str) -> List[str]:
    check_set = set()
    cur_string = ""
    ans = set()

    for i in range(len(s)):
        cur_string += s[i]

        if(i >= 9):
            if(cur_string in check_set):
                ans.add(cur_string)
            else:
                check_set.add(cur_string)
            cur_string = cur_string[1:]
    return list(ans)
