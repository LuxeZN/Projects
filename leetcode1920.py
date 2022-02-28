#Author: Zach Naymik
#Date: February 21, 2022

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]