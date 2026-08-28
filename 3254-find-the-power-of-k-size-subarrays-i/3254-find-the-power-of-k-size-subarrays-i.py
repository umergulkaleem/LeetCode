class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:



        count = -1
        res = []
        while count<len(nums)-k:
            count+=1
            arr = nums[count:count+k]
            check = set(arr)
            prev  = arr[0]
            done  = False
            print(arr)
            for i in range(1,len(arr)):
                # print(prev,"prev",arr[i],"now")
                if arr[i] != prev+1:
                    # print("in")
                    res.append(-1)
                    done = True
                    break
                prev = arr[i]
            if not done:
                res.append(max(arr))
        return res


        