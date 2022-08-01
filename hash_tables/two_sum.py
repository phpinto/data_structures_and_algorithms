class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = dict()
                
        for i in range(len(nums)):
            num = nums[i]
            rem  = target - num
            if rem in hash_map:
                return [hash_map[rem], i]
            hash_map[num] = i   
                
        return []