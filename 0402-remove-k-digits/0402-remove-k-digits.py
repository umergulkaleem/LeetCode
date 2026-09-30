class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        monotonic stack keep it increasing until k
        """
        if len(num) == k:
            return "0"
        mono_stack = []
        # prev =num[0]
        # mono_stack.append(prev)
        count = 0
        for i in range(len(num)):
            while k>0 and mono_stack and  mono_stack[-1]>num[i]:
                print("in")
                mono_stack.pop()
                k-=1
                count+=1
            mono_stack.append(num[i])
            # prev= num[i]
        
        mono_stack = mono_stack[:len(mono_stack)-k]
        while len(mono_stack)>1 and mono_stack[0] == "0":
            mono_stack.pop(0)

        return "".join(mono_stack)

