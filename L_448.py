from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    a = set(range(1, len(nums) + 1))
    for i in nums:
        a.discard(i)
    return list(a)


def findDisappearedNumbers2(nums: List[int]) -> List[int]:
    return list(set(range(1, len(nums) + 1)).difference(set(nums)))


print(findDisappearedNumbers2([1, 2, 2, 1]))
print(findDisappearedNumbers2([1, 1]))
