def compress_string(s):
    """
    e.g. aabbbcca -> a2b3c2a1
    """
    output = ""
    i = 0
    while i < len(s):
        ch = s[i]
        j = i + 1
        count = 1
        while j < len(s) and s[j] == ch:
            count += 1
            j += 1
        output += f'{ch}{count}'
        i += count
    return output

s1 = "hello"
print(compress_string(s1))

s2 = "aaaaaabbcaaaa"
#expect a6b2c1a4
print(compress_string(s2))

