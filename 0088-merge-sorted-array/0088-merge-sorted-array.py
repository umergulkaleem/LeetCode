class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # temp = []
        # for i in range(m):
        #     temp.append(nums1[i])
        # nums1 = temp
        # temp =[]
        # print(nums1)
        # for k in range(n):
        #     temp.append(nums2[k])
        # nums2 = temp
        
        # print(nums1,"num1")
        # print(nums2,"num2")

        # point1 = 0
        # point2 = 0
        # temp = []
        # while point1<m and point2<n:
        #     print(nums1[point1],"1")
        #     print(nums2[point2],"2")
        #     if nums1[point1]<nums2[point2]:
        #         temp.append(nums1[point1])
        #         point1+=1
        #     elif nums1[point1] == nums2[point2]:
        #         temp.append(nums1[point1])
        #         point1+=1
        #     else:
        #         temp.append(nums2[point2])
        #         point2+=1
        #     print(temp,"temp")
            
        temp = []
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        print(nums1)
        print(nums2)
        print(temp)

        # Add remaining elements
        while i < m:
            temp.append(nums1[i])
            i += 1
        while j < n:
            temp.append(nums2[j])
            j += 1

        # Copy merged list back to nums1 (in-place)
        for k in range(len(temp)):
            nums1[k] = temp[k]


        