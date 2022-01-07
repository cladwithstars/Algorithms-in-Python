def solution(strings, patterns):
    """
    Given an array strings, determine whether it follows the sequence given in the patterns array.
    In other words, there should be no i and j for which strings[i] = strings[j]
    and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and 
    patterns[i] = patterns[j]
    """
    d = dict()
    seen = set()
    for i in range(len(patterns)):
        if patterns[i] in d:
            if d[patterns[i]] != strings[i]:
                return False
        else:
            if strings[i] in seen:
                return False
            d[patterns[i]] = strings[i]
        seen.add(strings[i])
            
    return True

strings = ["cat", "dog", "doggy"]
patterns = ["a", "b", "b"]

print(solution(strings, patterns)) #expect false

strings = ["cat", "dog", "dog"]
patterns = ["a", "b", "b"]

print(solution(strings, patterns)) #expect true

