def reverseOnlyLetters(S):
        """
        Algorithm: 
        """
        if S.isalpha():
            return S[::-1]
        nonLetters = [ch for ch in S if not ch.isalpha()][::-1]
        print(nonLetters)
        letters = [ch for ch in S if ch.isalpha()]
        rev = ''.join(letters)[::-1]
        print(rev)
        
        newStr = ''
        i = 0
        j=0
        while i < len(S):
            print(S[i])
            if S[i].isalpha():
                print(j)
                newStr += rev[j]
                print(newStr)
                j+= 1
            else:
                print('in the else')
                newStr += nonLetters.pop()
            i+=1
        return newStr
        
print(reverseOnlyLetters('ab-cd'))