def insertInterval(intervals, newInterval):
    intervals.append(newInterval)
    intervals = sorted(intervals, key=lambda x: x[0])
    res = [intervals[0]]
    for i in intervals:
        if i[0] >= res[-1][0] and i[1] <= res[-1][1]:
            pass
        elif i[0] < res[-1][1] and i[1] >= res[-1][1]:
            res[-1][1] = i[1]
        else:
            res.append(i)
    return res


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]

print(insertInterval(intervals, newInterval))
