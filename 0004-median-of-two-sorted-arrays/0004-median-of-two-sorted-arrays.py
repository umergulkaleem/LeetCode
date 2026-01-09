class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # length = len(nums1)+len(nums2)
        # if length % 2!=0:
        #     median = length+1
        #     median = median/2
        #     isodd = True
        # else:
        #     median = length/2
        #     isodd =False
        # if not nums1:  # nums1 empty
        #     if isodd:
        #         return nums2[(len(nums2)-1)//2]
        #     else:
        #         mid = len(nums2)//2
        #         return (nums2[mid-1] + nums2[mid])/2
        # if not nums2:  # nums2 empty
        #     if isodd:
        #         return nums1[(len(nums1)-1)//2]
        #     else:
        #         mid = len(nums1)//2
        #         return (nums1[mid-1] + nums1[mid])/2
        # print(median)
        # median = int(median)
        # n1,n2 = 1,1
        # print(n2,"n2")
        # while n1<=len(nums1):
        #     leftnums1 = nums1[:n1]
        #     n2 = median-n1
        #     leftnums2 = nums2[:n2] if n2>=0 else []
        #     maxleft = max(max(leftnums1) if leftnums1 else float('-inf'),
        #         max(leftnums2) if leftnums2 else float('-inf'))
        #     rightnums1 = nums1[n1:]
        #     rightnums2 = nums2[n2:]if n2>=0 else []

        #     minright = min(min(rightnums1) if rightnums1 else float('inf'),
        #         min(rightnums2) if rightnums2 else float('inf'))
        #     if maxleft<=minright:
        #         if isodd:
        #             return maxleft
        #         else:
        #             return (maxleft+minright)/2
        #     else:
        #         n1+=1

        A,B = nums1,nums2
        total = len(A)+len(B)
        half = total//2
        if len(B)<len(A):
            A,B = B,A

        l,r = 0,len(A)-1
        while True:
            m = (l+r)//2
            j = half-m-2
            Aleft = A[m] if m>=0 else float("-infinity")
            Aright = A[m+1]  if (m+1)<len(A)else float("infinity")
            Bleft = B[j] if j>=0 else float("-infinity")
            Bright = B[j+1] if (j+1)<len(B) else float("infinity")

            if Aleft <=Bright and Bleft <=Aright:

                if total %2!=0:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft) + min(Aright,Bright))/2
            elif Aleft>Bright:
                r = m-1
            else:
                l = m+1
        