   
import numpy as np
import math  
def run(x:int):
    """
    :type x: int
    :rtype: int
    """
    li = []
    h = 1

    if abs(x) != x:
        h = -1
        x = abs(x)
    while x > 0:
        li.append(x%10)
        x = math.floor(x/10)
    s = 0
    for i in range(len(li)):
        s += (li[i])*(np.power(10,len(li)-i-1))
    l = s * h
    if (l >= -np.power(2,31)) and (l < np.power(2,31)): 
        pass
    else:
        l = 0 
    return(int(l))