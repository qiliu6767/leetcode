class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = collections.defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)
        
        # The maximum number of appearing times
        max_val = max(collections.Counter(nums).values())
        
        res = min([d[n][-1] - d[n][0] + 1 for n in d if len(d[n]) == max_val])
        
        return res
        