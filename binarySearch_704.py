class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        
        # Special cases
        if nums[low] == target:
            return low
        
        if nums[high] == target:
            return high
        
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            if nums[mid] > target:
                high = mid
            
        return -1
                
                
        
        
        