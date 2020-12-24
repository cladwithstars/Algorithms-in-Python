def is_palindrome(s):
    """Return whether or not s is a palindrome

    Disregards punctuation and whitespace characters

    Args:
        s (String): any string 
    """
    i, j = 0, len(s) - 1

    while i < j :
        while not s[i].isalnum():
            i+=1
        while not s[j].isalnum():
            j -= 1
        
        if i < j and s[i].lower() != s[j].lower():
                return False
        i+=1
        j-= 1

    return True

print(is_palindrome('hey'))
print(is_palindrome('111'))
print(is_palindrome('hannah'))
print(is_palindrome('BLLBP'))

print(is_palindrome('hann     ah'))
print(is_palindrome('Was it a cat I saw?'))