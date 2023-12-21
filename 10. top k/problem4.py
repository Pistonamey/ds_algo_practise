# given a string sort it according to its decreasing frequency occuring characters.
from heapq import *
def sort_character_by_frequency(string):
    freqDict={}

    for character in string:
        freqDict[character]=1+freqDict.get(character,0)
    
    maxHeap=[]
    for char,freq in freqDict.items():
        heappush(maxHeap,(-freq,char))
    ls=[]
    while maxHeap:
        freq,char=heappop(maxHeap)
        for _ in range(-freq):
            ls.append(char)
    
    return "".join(ls)

def main():
    print("String after sorting characters by frequency: "+sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: "+sort_character_by_frequency("abcbab"))

main()