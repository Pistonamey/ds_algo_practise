# Q - Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.


def mergeIntervals(intervals):
    result = []
    intervals.sort()
    if(len(intervals) < 2):
        return intervals
    result.append(intervals[0])

    for i in range(1, len(intervals)):
        if(result[-1][1] >= intervals[i][0]):
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append(intervals[i])
    return result


interval1 = [[1, 4], [2, 5], [7, 9]]
interval2 = [[6, 7], [2, 4], [5, 9]]
interval3 = [[1, 4], [2, 6], [3, 5]]
print(mergeIntervals(interval1))
print(mergeIntervals(interval2))
print(mergeIntervals(interval3))
