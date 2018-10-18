
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        Given two arrays, write a function to compute their intersection.

		Example 1:
		Input: nums1 = [1,2,2,1], nums2 = [2,2]
		Output: [2,2]

		Example 2:
		Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
		Output: [4,9]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        # Make sure nums1 is the shorter list
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        res = [] # Save result
        i = 0 # Pointer
        
        for num in nums1:
            while True:
                if i >= len(nums2):
                    break
                if nums2[i] == num:
                    res.append(num)
                    i += 1
                    break
                elif nums2[i] > num:
                    break
                else:
                    i += 1
        return res
