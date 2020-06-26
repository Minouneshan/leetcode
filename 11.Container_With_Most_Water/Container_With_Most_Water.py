class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=len(height)
        water_list=[]

        p1=0
        p2=l-1

        while p1<p2:

            if height[p1]<=height[p2]:
                water_list.append(height[p1]*(p2-p1))
                p1+=1
            if height[p1]>height[p2]:
                water_list.append(height[p2]*(p2-p1))
                p2-=1
        return max(water_list)