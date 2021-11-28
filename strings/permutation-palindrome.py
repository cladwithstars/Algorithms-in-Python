"""
write a function to determine if a string is a paldinrome or some permutation of that string
is a palindrome.

E.g., both 'racecar' and 'acecarr' would both be true, whereas 'cat' wouldn't. 
"""
def palindrome_perm(s):
    d = {}
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch]+= 1
    numOdds = 0  
    for val in d.values():
        if val % 2 == 1:
            numOdds += 1
    return numOdds == 1 or numOdds == 0

print(palindrome_perm('racecar'))
print(palindrome_perm('acecarr'))
print(palindrome_perm('cat'))
print(palindrome_perm('pipli'))
print(palindrome_perm('popjj'))