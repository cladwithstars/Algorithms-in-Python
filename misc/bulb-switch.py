def bulbSwitch(n):
        #represent on by 1 and off by -1
        
        bulbs = [1 for _ in range(n)] #initialize this, counts as the first round
        
        for i in range(1, n+1): # the "skip value"
            for j in range(i, len(bulbs), i + 1):
                print('skip val: ',i)
                print('index to switch off: ', j)
                bulbs[j] = -bulbs[j]
            
                
        print(bulbs)
        return len([bulb for bulb in bulbs if bulb == 1])

print(bulbSwitch(3))
print(bulbSwitch(1))
print(bulbSwitch(0))
            