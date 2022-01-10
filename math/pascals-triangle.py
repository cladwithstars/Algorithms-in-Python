
def generate(numRows):
    """
    Args:
        numRows (int): number of rows of pascals' triangle to generate

    Returns:
        List of List: Pascals' triangle up to numRows
    """
    
    triangle = []
    
    while len(triangle) < numRows:
        if not triangle:
            triangle = [[1]]
        
        else:
            vals = [1]
            i, j = 0, 1
            row = triangle[-1]
            print(triangle, row)
            while j < len(row):
                val = row[i] + row[j]
                vals.append(val)
                j += 1
                i+=1
            vals.append(1)
            triangle.append(vals)
    return triangle

print(generate(12))