from itertools import product
def nextTime(time):
    def isValid(d1, d2, d3, d4):
        if d1 not in (0, 1, 2) or d3 not in (0, 1, 2, 3, 4, 5):
            return False
        if d1 == 2 and d2 not in (0, 1, 2, 3):
                return False
        return True
    def toInt(digits):
        return int(''.join([str(d) for d in digits]))
    def format(digits):
        return str(digits[0]) + str(digits[1]) + ":" + str(digits[2]) + str(digits[3])
        
    digits = [int(ch) for ch in time if ch != ":"]
    candidates = []
    for comb in product(digits, repeat = 4):
        if isValid(comb[0], comb[1], comb[2], comb[3]):
            candidates.append(list(comb))
    candidates.sort()
    
    for c in candidates:
        if toInt(c) > int(time[0:2] + time[3:5]):
            return format(c)
    return format(candidates[0])
            


print(nextTime("19:34"))
print(nextTime("23:59"))
print(nextTime("01:30"))
print(nextTime("20:03"))
    

