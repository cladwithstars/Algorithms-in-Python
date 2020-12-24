def is_anagram(s1, s2):
    """Returns whether s1 and s2 are anagrams

    Args:
        s1 (String): any string
        s2 (String): any string

    complexity: O(n)
    """
    if len(s1) != len(s2):
        return False
    letterCount = dict();
    for ch in s1:
        if ch in letterCount:
            letterCount[ch] += 1
        else:
            letterCount[ch] = 1
    for ch in s2:
        if ch in letterCount:
            letterCount[ch] -= 1
        else:
            return False

    for v in letterCount.values():
        if v != 0:
            return False

    return True

print(is_anagram('bob', 'ob'))
print(is_anagram('hello', 'loelh'))

def is_anagram2(s1, s2):
    """
    complexity: O(n) where n is length of longer string
    """
    return len(s1) == len(s2) and set(s1) == set(s2)

print(is_anagram2('bob', 'ob'))
print(is_anagram2('hello', 'loelh'))

def is_anagram3(s1, s2):
    """
    complexity: O(n log n ) where n is length of longer string
    """
    return sorted(s1) == sorted(s2)

print(is_anagram3('bob', 'ob'))
print(is_anagram3('hello', 'loelh'))

