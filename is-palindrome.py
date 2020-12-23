def is_palindrome(s):
    """Return whether or not s is a palindrome

    Args:
        s (String): any string 
    """
    def relevant_char(ch):
        return ch.isalpha() 
    i, j = 0, len(s) - 1

    while i != j and i < len(s) and j>=0:
        if s[i].lower() != s[j].lower():
            return False
        i+=1
        j-= 1

    return True

print(is_palindrome('hey'))
print(is_palindrome('111'))
print(is_palindrome('hannah'))
print(is_palindrome('BLLBP'))
