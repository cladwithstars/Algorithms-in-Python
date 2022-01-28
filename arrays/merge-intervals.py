
def merge(intervals):
    
    intervals = sorted(intervals, key=lambda x: x[0])
    res = []
    i = 0
    while i < len(intervals) - 1:
        while intervals[i][1] >= intervals[i + 1][0]:
            print('intervals: ', intervals[i][1], intervals[i  + 1][0])
            intervals[i] = [intervals[i][0], intervals[i + 1][1]]
        i += 1
    return intervals

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))