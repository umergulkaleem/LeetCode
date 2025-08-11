class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # first = Counter(nums1)
        # second = Counter(nums2)
        # flist = []
        # list1 = list(first-second)
        # flist.append(list1)
        # list2 = list(second-first)
        # flist.append(list2)
        # return flist

        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
        