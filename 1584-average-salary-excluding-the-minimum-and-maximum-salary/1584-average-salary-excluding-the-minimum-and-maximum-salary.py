class Solution:
    def average(self, salary: List[int]) -> float:
        salaryf = 0
        count = 0
        salary.sort()
        # sort1 = sorted(salary)
        for i in range(1,len(salary)-1):
            count+=1
            salaryf +=salary[i]
        return salaryf/count
            
        