from typing import List

def run(nums1: List[int], nums2: List[int]) -> float:
    l = []
    import math
    y = ((len(nums1)+len(nums2))/2)
    z = math.floor(y)
    for i in range(z+1):
        
            if (len(nums1)>0) & (len(nums2)>0) :
                if  (nums1[0] < nums2[0])  :
                    l.append(nums1[0])
                    nums1.pop(0)
                else:
                    l.append(nums2[0])
                    nums2.pop(0)

            elif (len(nums1)>0):
                l.append(nums1[0])
                nums1.pop(0)  

            elif (len(nums2)>0):
                l.append(nums2[0])
                nums2.pop(0)
    if y != z:
        return (l[-1])
    else:
        return ((l[-1]+l[-2])/2)