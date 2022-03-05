#Author: Zach Naymik
#Date: March 5, 2022

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        bool_array = candies
        i = 0
        while (i < len(candies)):
            if (candies[i] + extraCandies) >= max_candies:
                bool_array[i] = True
            else:
                bool_array[i] = False
            i += 1
        return bool_array