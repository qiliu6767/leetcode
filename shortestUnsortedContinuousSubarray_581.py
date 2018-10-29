import collections

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Create a dictionary with key as each number and value as its appearance times
        num_time = collections.Counter(nums)
        
        # A list with the unique elements of nums
        uni_nums = list(set(nums))
        
        indices = []
        for i, num1 in enumerate(uni_nums):
            if (num1 + 1) in uni_nums:
                temp = [num1, num1 + 1]
                indices.append(temp)
        
        len_lst = []
        for item in indices:
            len_lst.append(num_time[item[0]] + num_time[item[1]])
        
        return max(len_lst)
        
soln = Solution()
print(soln.findLHS(nums = [1,3,2,2,5,2,3,7]))