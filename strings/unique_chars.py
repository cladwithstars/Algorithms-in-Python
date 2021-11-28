# def unique_chars(s):
#     """
#     return whether string s has all unique characters (no duplicate chars)

#     Args:
#         s (string): any string
#     """
#     #method 1, if allowed additional data structures
#     return len(s) == len(set(s))

def unique_chars(s):
    """
    return whether string s has all unique characters (no duplicate chars)

    Args:
        s (string): any string
    """
    #method 2, if NOT allowed additional data structures
    if (len(s) == 1):
        return True
    sortedString = sorted(s)
    for i in range(0, len(sortedString) - 1):
        if sortedString[i] == sortedString[i + 1]:
            return False

    return True

s1 = 'hello'
#expect false
print(unique_chars(s1))

s2 = 'qwertyuiop'
#expect true
print(unique_chars(s2))

s3 = 'asdfghjkla'
#expect false
print(unique_chars(s3))


