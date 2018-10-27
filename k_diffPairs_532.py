class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num_time_dict = collections.Counter(nums)
        
        res = 0
        for num in num_time_dict:
            if k > 0:
                if (num + k) in num_time_dict:
                    res += 1
            elif k == 0:
                if num_time_dict[num] > 1:
                    res += 1
        
        return res