import math

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) <= len(nums2):
            a, b = nums1, nums2  
        else:
            a, b = nums2, nums1
        left = (len(a) + len(b)) // 2
        
        l, r = 0, len(a) - 1
        
        while True:
            m1 = (l + r) // 2
            m2 = left - m1 - 2
            
            aL = a[m1] if m1 >= 0 else float('-inf')
            aR = a[m1 + 1] if (m1 + 1) < (len(a)) else float('inf')
            bL = b[m2] if m2 >= 0 else float('-inf')
            bR = b[m2 + 1] if (m2 + 1) < (len(b)) else float('inf')

            if aL <= bR and bL <= aR:
                if (len(a) + len(b)) % 2 == 1:
                    return min(aR, bR)
                else:
                    return (max(aL,bL) + min(aR,bR)) / 2.0
            elif aL > bR:
                r = m1 - 1
            else:
                l = m1 + 1
            
            