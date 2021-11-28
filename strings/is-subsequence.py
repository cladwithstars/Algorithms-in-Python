def isSubsequence(s, t):
    """
    (1) First check if s is a subset of t. If not, return False 
    
    (2) Now that we know all the characters in s are in t as well, we just need to make sure that the order is right.
    I.e., we need to ensure that the first character in s also appears first in t, second character in s also appears second in t,
    and so on.
    We can use python's index() method here and just compare all in t. 
    """
    #First check if subset
    
    sChars = set(s)
        
    for ch in sChars:
        if ch not in t or t.count(ch) < s.count(ch):
            return False
        
    stack = [ch for ch in s][::-1]
    print(stack)
    seen = set()
    
    for ch in t:
        if ch in sChars:
            seen.add(ch)
            if stack:
                if ch not in seen and ch != stack.pop():
                    return False
            else:
                return True
    return True
print(isSubsequence('leetcode', 'yyylyyyeyyyeyyytycyoyydye') )

print(isSubsequence('abc', 'hhbabc'))

print(isSubsequence('abc', 'hhacb'))
