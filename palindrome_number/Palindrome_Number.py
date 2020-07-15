class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        import math
        li = []
        
        if x < 0:
            return False
        while x > 0:
            li.append(int(x%10))
            x = int(x/10)
        y = len(li)
        for i in range(int(math.floor(y/2))):
            if li[i] != li[y-i-1]:
                return False
        return True