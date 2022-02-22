#Author: Zach Naymik
#Date: February 21, 2022

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))
        i = 0
        while (i < len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
            i += 1
        return ans
            