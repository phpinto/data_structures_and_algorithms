## Brute Force

class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        for i in range(len(arr) - (m * k) + 1):
            pat = arr[i:(i+m)]
            pat_count = 1
            for j in range((i+m), (len(arr) - m + 1)):
                if arr[j:(j+m)] == pat:
                    pat_count += 1
                    if pat_count == k:
                        return True
                    j += m
                else:
                    break
        return False
    
    

    
    
## Optimized (One Look)


class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        count = m
        for i in range(len(arr) - m):
            if arr[i] != arr[i + m]:
                count = m
            else:
                count += 1
            if count == k * m:
                return True
        return False