class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_ = sum(nums)
        cumsum_ = 0
        for i, num in enumerate(nums):
            # If the current num is subtracted from the total sum
            # and the result is 2 * cumsum_, this means that 
            # the cumsum_ is equal to the sum of the right part of this num
            if sum_ - num == 2 * cumsum_:
                return i
            
            # Update the sum of left part "cumsum_"
            cumsum_ += num
        
        return -1
        