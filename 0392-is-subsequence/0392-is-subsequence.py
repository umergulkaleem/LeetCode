class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        point1 = 0
        point2 = 0
        if s=="" :
            return True
        while point2<len(t):
            print(s[point1],"s")
            print(t[point2],"t")
            if s[point1]== t[point2]:
                point1+=1
                point2+=1
                print("has ")
            else:
                point2+=1
            print(point1,"point1")
            print(len(s)-1)
            if point1>len(s)-1:
                return True
        return False
