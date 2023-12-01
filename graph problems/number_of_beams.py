from typing import List

def numberOfBeams(self, bank: List[str]) -> int:
        number_of_lasers=0
        for i in range(len(bank)):
            if "1" in bank[i]:
                ones_in_row=bank[i].count("1")
                for j in range(i+1,len(bank)):
                    if("1" in bank[j]):
                        ones_in_this_row=bank[j].count("1")
                        number_of_lasers+=ones_in_row*ones_in_this_row
                        break
        return number_of_lasers

print(numberOfBeams(["011001","000000","010100","001000"]))