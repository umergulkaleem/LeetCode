class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # even = True
        # prev = nums1[0]
        # if prev % 2 == 0:
        #     even = True
        # else:
        #     even  = False

        # nums2 = []
        # nums2.append(prev)

        # for i in range(1,len(nums1)):
        #     print(nums2)
        #     if nums1[i] % 2 ==0 :
        #         # if current is even
        #         print('IN')
        #         if even:
        #             # if prev is also even 
        #             nums2.append(nums1[i])
        #         else:
        #             # if prev is false
        #             new = nums1[i] - prev
        #             if new % 2 != 0:
        #                 nums2.append(new)
        #             else:
        #                 return False
        #     else:
        #         # if curr is not even
        #         if not even:
        #             # and prev is also not even 
        #             nums2.append(nums1[i])
        #         else:
        #             new = nums1[i] -prev
        #             if new % 2 == 0 :
        #                 # if new is even
        #                 nums2.append(new)
        #             else:
        #                 return False
        #     prev= nums1[i]
        # return True


        # prev= nums1[0]
        # nums2  = []
        # nums2.append(prev)
        # for i in range(1,len(nums1)):
        #     preveven = True
        #     curreven = True
        #     curr =  nums1[i]
        #     if prev % 2 == 0:
        #         preveven = True
        #     else:
        #         preveven = False
            
        #     if curr  % 2 == 0:
        #         curreven = True
        #     else:
        #         curreven = False
            
        #     if preveven and not  curreven:
        #         new = prev-curr
        #         if new % 2 !=0:
        #             return False
        #     if  not preveven and curreven:
        #         new = prev - curr
        #         if new %2 == 0:
        #             return False

        # return True


        # prev = nums1[0]

        # for i in range(1,len(nums1)):
        #     curr = nums1[i]

        #     if (prev-curr)% 2 ==0:
        #         return False
            
        #     prev = curr
        # return True
        # if len(nums1) == 1:
        #     return True

        # odd =0
        # for num in nums1:
        #     if num % 2:
        #         odd+=1
        # return odd !=1
        min_val = min(nums1)
        if min_val % 2 != 0:
            return True
        
        # If min_val is even, it's only possible if there are no odd numbers
        return all(x % 2 == 0 for x in nums1)




                    

        