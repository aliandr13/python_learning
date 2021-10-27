from typing import List

"""
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
"""


def sortColors(self, nums: List[int]) -> None:
    red = 0  # 0
    white = 0  # 1
    blue = 0  # 2

    for i in nums:
        if i == 0:
            red += 1
        elif i == 1:
            white += 1
        else:
            blue += 1

    for i in range(0, len(nums)):
        if red > 0:
            nums[i] = 0
            red -= 1
        elif white > 0:
            nums[i] = 1
            white -= 1
        else:
            nums[i] = 2


histo = {0:0, 1:0, 2:0}
print(histo)