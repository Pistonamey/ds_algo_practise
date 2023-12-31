# find distinct subset for an array that might contain duplicates

def find_subset_distinct(nums):
    result=[]
    result.append([])
    startindex,endindex=0,0
    for i in range(len(nums)):
        startindex=0
        if(i>0 and nums[i-1]==nums[i]):
            startindex=endindex+1
        endindex=len(result)-1

        for j in range(startindex,endindex+1):
            set=list(result[j])
            set.append(nums[i])
            result.append(set)
    
    return result



def main():
    print("Here is the list of subsets: " + str(find_subset_distinct([1,3,3])))
    print("Here is the list of subsets: " + str(find_subset_distinct([1,5,3,3])))

main()