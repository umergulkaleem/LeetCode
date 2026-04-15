class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # for i in range(len(arr)):
            
        #     max_right = 0
        #     print(i,"i")
        #     for j in range(i,len(arr)):
        
        #         max_right = max(max_right,arr[j])
        #     print(max_right,"right")
        #     if i+1<len(arr)-1:
        #         arr[i+1]=max_right

        # arr[-1]=-1
        # return arr
        max_right = -1

        for i in range(len(arr)-1,-1,-1):
            tmp  = arr[i]
            arr[i] = max_right
            max_right = max(max_right,tmp)
        return arr

        