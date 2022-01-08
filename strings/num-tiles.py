def numTilePossibilities(tiles):
    s = set()
    for i in range(len(tiles)):
        for j in range(i, len(tiles) + 1):
            word = tiles[i:j]
            
            
            if word not in s:
                s.add(word)
            if word[::-1] not in s:
                s.add(word[::-1])
    print(s)
    return len(s)

print(numTilePossibilities("AAB"))