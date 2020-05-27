from typing import List
import copy


class Max():

    def max(self, list: List[int]):
        max = 0
        for i in list:
            max = i if i > max else max
        return max

    def maxRecursive(self, list: List[int], max: int = 0):
        if list:
            i = list.pop(0)
            max = i if i > max else max
            return self.maxRecursive(list, max)
        else:
            return max

    def maxListMod(self, list: List[int]):
        if len(list) == 1:
            return list[0]
        else:
            n_list = []
            for i in range(0, len(list), 2):
                try:
                    if list[i + 1] > list[i]:
                        n_list.append(list[i + 1])
                    else:
                        n_list.append(list[i])
                except IndexError:
                    n_list.append(list[i])
                    continue
            return self.maxListMod(n_list)

    def maxNOne(self, list: List[int]):
        max = list[0]
        for i in list[1:]:
            max = i if i > max else max
        return max


data = [3, 5, 4, 8, 7, 9, 2, 1, 0, 6, 10, 13, 12, 15, 16, 17, 14, 19, 18, 20, 21]
max = Max()
print('max()', max.max(copy.deepcopy(data)), 'O(n)')
print('maxRecursive()', max.maxRecursive(copy.deepcopy(data)), 'O(n) with list management overhead and a risk of maximum recursion depth exceeded')
print('maxListMod()', max.maxListMod(copy.deepcopy(data)), 'O(?)')
print('maxNOne()', max.maxNOne(copy.deepcopy(data)), 'O(n-1)')
