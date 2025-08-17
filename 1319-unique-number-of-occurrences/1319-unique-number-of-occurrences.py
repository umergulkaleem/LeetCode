class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # occur  = Counter(arr)
        # print(occur)
        # present = []
        # for i in range(len(occur)):
        #     print(present,"present")
        #     if occur[i] not in present:
        #         present.append(occur[i])
        #     if occur[i] in present:
        #         return False
        # return True

        occur  = Counter(arr)
        print(occur)
        present = []
        for freq in occur.values():
            print(present,"present")
            if freq in present:
                return False
            present.append(freq)
        return True
            

        