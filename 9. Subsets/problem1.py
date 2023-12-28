#find the distinct subsets for all the numbers in the given distinct array


def find_subsets(nums):
    result=[]
    result.append([])

    for current_number in nums:
        n=len(result)
        for i in range(n):
            set=list(result[i])
            set.append(current_number)
            result.append(set)
    
    return result

def main():
    print("Here is the list of subsets: " + str(find_subsets([1,3])))
    print("Here is the list of subsets: " + str(find_subsets([1,5,3])))

main()