from typing import List
import math

class Max():

    def max(self, list: List[int]):
        try:
            max = 0
            for i in list:
                max = i if i > max else max
            return max
        except:
            return 0

    def maxRecursive(self, list: List[int], max: int = 0):
        if list:
            l = list.pop(0)
            max = l if l > max else max
            return self.maxRecursive(list, max)
        else:
            return max


l = [3,5,4,8,7,9,2,1,0,6]
max = Max()
print('max()', max.max(l), 'O(n)')
print('max recursive', max.maxRecursive(l), 'O(n) with list management overhead and a risk of maximum recursion depth exceeded')

