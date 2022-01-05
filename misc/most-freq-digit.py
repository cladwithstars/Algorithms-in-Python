def most_freq_digit(a):
    """return the most frequent digits in the list of integers a

    Args:
        a ([list]): list of positive integers

    Returns:
        [list]: list of most common digits in a
    """
    strNums = []
    for num in a:
        strNums.append(str(num))
    
    digitString = ''
    for s in strNums:
        digitString += s
    
    output = []
    
    currMax = 0
    uniqueChars = list(set(digitString))
    for dig in uniqueChars:
        count = digitString.count(dig)
        if count > currMax:
            output = [int(dig)]
            currMax = count
        elif count == currMax:
            output.append(int(dig))
    
    return sorted(output)

print(most_freq_digit([25, 2, 3, 57, 38, 41]))