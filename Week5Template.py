"""
>>> doomsday(2012)
3
>>> doomsday(1899)
2
>>> doomsday(1923)
3
>>> doomsday(10000)
-1
>>> doomsday(1756)
-1
"""

# Removed for irrelivence
#>>> type(doomsday(2010))
#<type 'int'>

# *** DO NOT CHANGE CODE ABOVE THIS LINE ***

def doomsday(y):
    if y in range(1800,1900):
    	x=5
    elif y in range(1900,2000):
    	x = 3
    elif y in range(2000,2100):
    	x = 2
    elif y in range(2100,2200):
    	x = 0
    else:
    	return -1

    w = y%100
    b = w%12
    a = (w-b) // 12
    c=b//4

    d = (a+b+c)%7

    return (d+x)%7