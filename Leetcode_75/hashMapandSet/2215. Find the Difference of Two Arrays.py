class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        set_a = set(nums1)
        set_b = set(nums2)
        return [list(set_a - set_b),list(set_b-set_a)]
        # a = set(nums1)
        # b = set(nums2)
        # intersection = a.intersection(b)
        # res = [[],[]]
        # for num in a:
        #     if num not in intersection:
        #         res[0].append(num)

        # for num in b:
        #     if num not in intersection:
        #         res[1].append(num)
        
        # return res
        
        