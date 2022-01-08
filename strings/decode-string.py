def solution(s):
    '''
    Given an encoded string, return its corresponding decoded string.
    The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated 
    exactly k times. Note: k is guaranteed to be a positive integer.
    '''
    stack = []
    # for i in range(len(s)):
    i = 0
    while i < len(s):
        if s[i] != ']':
            stack.append(s[i])
            i += 1
        else:
            substr = ""
            while stack[-1] != "[":
                ch = stack.pop()
                substr = ch + substr 
            stack.pop() # remove left bracket
            ourInt = ""
            # while loop to get the int
            while stack and stack[-1].isdigit():
                dig = stack.pop()
                ourInt = dig + ourInt
            decodedString = int(ourInt) * substr
            stack.append(decodedString)
            i += 1
            
            
    return "".join(stack)

s = "4[ab]"
print(solution(s)) # epxect "abababab"

s = "2[b3[a]]"
print(solution(s)) # "baaabaaa"

s = "z1[y]zzz2[abc]"
print(solution(s)) # "zyzzzabcabc"