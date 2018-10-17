class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
        """
        self.nums = nums
        self.cumsum = [sum(nums[0:i+1]) for i in range(len(nums))]
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.cumsum[j]
        else:
            return self.cumsum[j] - self.cumsum[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)