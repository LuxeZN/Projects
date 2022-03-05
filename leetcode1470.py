#Author: Zach Naymik
#Date: March 5, 2022

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        new_list = nums
        i = 0
        x = [0] * n
        y = [0] * n
        while (i < n):
            x[i] = nums[i]
            i += 1
        while (i >= n and i < (2 * n)):
            y[i - n] = nums[i]
            i += 1
        j = 0
        for i in x:
            new_list[j] = i
            j += 2
        k = 1
        for i in y:
            new_list[k] = i
            k += 2
        return new_list
            