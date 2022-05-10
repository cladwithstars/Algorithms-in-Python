def compare(s, t):
    def process(s):
        stack = []
        i = 0
        while i < len(s):
            if s[i] != '#':
                stack.append(s[i])
            else:
                if not stack:
                    continue
                else:
                    stack.pop()
            i+=1
        return ''.join(stack)
    return process(s) == process(t)


print(compare('ab#g', 'ab#c')) #false
print(compare('ac#d', 'ab#d')) #true