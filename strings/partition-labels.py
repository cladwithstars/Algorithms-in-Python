def partitionLabelsOld(S):
    
    partition =[]
    
    i = 0
    while i < len(S):
        ch = S[i]
        lastIndex = S.rfind(ch)
        
        if i == lastIndex: 
            partition.append(ch)
            i += 1
        else:
            
            st = S[ i : lastIndex ]

            print('st is : ', st)
            
            
            chars = set(st)
            
            print('chars', chars)
            lastIndexes = [S.rfind(c) for c in chars]

            maxIndex = max(lastIndexes)

            newS = S[i : max(lastIndexes)]

            print('new S: ', newS)

            

            p = S[:maxIndex]
            
            partition.append(p)
            return p
    
    # print(partition)
    # return [len(p) for p in partition]

def partitionLabels(S):
    partitions = []
    i = 0
    while i < len(S):
        ch = S[i]
        lastIndex = S.rfind(ch)

        if i == lastIndex: 
            partition.append(ch)
            i += 1

        else:
            st = S[ i : lastIndex ]
            print('st is : ', st)
            chars = set(st)
            
            print('chars', chars)
            maxCurIndex = max([S.rfind(c) for c in chars])
            
            while maxCurIndex > lastIndex:
                st = st[i:  maxCurIndex ]
                chars = set(st)
                lastIndex, maxCurIndex = maxCurIndex, max([S.rfind(c) for c in chars])
            partitions.append(st)
            print(partitions)






# S = 'abc'
S = "qiejxqfnqceocmy"
print(partitionLabels(S))



