def conflictingAppointments(intervals):
    intervals.sort()
    previousEnd=intervals[0][1]
    if(len(intervals)<2):
        return True
    intervals.sort()
    for i in range(1,len(intervals)):
        if(intervals[i][0]<previousEnd):
            return False
        else:
            previousEnd=intervals[i][1]
    
    return True


print(conflictingAppointments([[1,4], [2,5], [7,9]]))
print(conflictingAppointments([[6,7], [2,4], [8,12]]))
print(conflictingAppointments([[4,5], [2,3], [3,6]]))
