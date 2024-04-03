
#insert intervals
def insertInterval(intervals,interval):
    result=[]
    for i in range(len(intervals)):
        if(intervals[i][1]<interval[0]):
            result.append(intervals[i])
        elif(intervals[i][1]==interval[0]):
            result.append([intervals[i][0],max(intervals[i][1],interval[1])])
        else:
            result.append([min(intervals[i][0],interval[0]),max(intervals[i][1],interval[1])])
            
            for j in range(i+1,len(intervals)):
                result.append(intervals[j])
            return result
    return result
    
    

print(insertInterval([[1,3], [5,7], [8,12]],[4,6]))
print(insertInterval([[1,3], [5,7], [8,12]],[4,10]))
