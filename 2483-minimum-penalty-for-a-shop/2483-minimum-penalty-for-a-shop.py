class Solution:
    def bestClosingTime(self, customers: str) -> int:

        # res = float("inf")
        # y,n = 0,0
        # for i in customers:
        #     if i =="Y":
        #         y+=1
        #     else:
        #         n+=1
        
        # curr_y = 0
        # curr_n = 0
        # best_hour = len(customers)
        # for i in range(len(customers)-1,-1,-1):
        #     if customers[i] =="Y":
        #         curr_y+=1
        #     else:
        #         curr_n+=1
        #     y_after = y-curr_y
        #     n_before =  n-curr_n
        #     penalty = y_after+n_before
            
        #     if penalty<=res:
        #         res = penalty
        #         best_hour = i
        # if y<res:
        #     best_hour = 0
        # return best_hour
        
 
        penalty = customers.count('Y')
        min_penalty = penalty
        best_hour = 0

        for i, c in enumerate(customers):
            if c == 'Y':
                penalty -= 1
            else:
                penalty += 1
            
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = i + 1
        
        return best_hour
            

        