class Solution:
    def __init__(self):
        pass


    def set_intresction(self, s1: Set, s2: Set):
        return [x for x in s1 if x in s2]

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1: Set = set(num1)
        s2 = set(nums2)

        # r = []
        # for i in s2:
        #     if i in s1:
        #         r.append(i)
        # return r

        if len(nums1) < len(num2):
            return set_intresction(nums1, nums2)
        else:
            return set_intresction(nums2, nums1)