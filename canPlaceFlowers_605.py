class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # Add a zero to start and end respecitively
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        
        count = 0
        for f in flowerbed:
            if f == 0:
                count += 1
            else:
                count = 0
            if count == 3:
                count = 1
                n -= 1
            if n == 0:
                return True
        
        return False