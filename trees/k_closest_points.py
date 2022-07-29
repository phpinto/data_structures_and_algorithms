## Sorting (nlog(n))

import math

class Solution(object):
    def minkovski_dist(self, pair, norm=2):
        return math.sqrt(sum((pair[0][i] - pair[1][i]) ** norm for i in range(len(pair[0]))))
    
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dists = [self.minkovski_dist([p, [0]*len(p)]) for p in points]
        idx = [i[0] for i in sorted(enumerate(dists), key=lambda x:x[1])][:k]
        
        return [points[i] for i in idx]        

## Using a Min Heap (klog(n))

import math
from heapq import heapify, heappop

class Solution(object):
    def minkovski_dist(self, pair, norm=2):
        return math.sqrt(sum((pair[0][i] - pair[1][i]) ** norm for i in range(len(pair[0]))))
    
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        min_heap = [[self.minkovski_dist([p, [0]*len(p)])] + p for p in points]
        heapify(min_heap)
        
        k_closest = []
        for _ in range(k):
            _, x, y = heappop(min_heap)
            k_closest.append([x,y])

        return k_closest  

## Using a Min Heap (klog(n)) just adding squares

import math
from heapq import heapify, heappop

class Solution(object):
    
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        min_heap = [[sum([v ** 2 for v in p])] + p for p in points]
        heapify(min_heap)
        
        k_closest = []
        for _ in range(k):
            _, x, y = heappop(min_heap)
            k_closest.append([x,y])

        return k_closest   