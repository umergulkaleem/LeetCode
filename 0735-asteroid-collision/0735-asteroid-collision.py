class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # stack = [asteroids[0]]

        # for i in range(1,len(asteroids)):
        #     curr = asteroids[i]
        #     prev = stack[-1]
        #     print(prev,"prev")
            
        #     if curr<0:
        #         print("found negative")
        #         while curr>prev:
        #             stack.pop(prev)
        #         continue

                
        #     stack.append(asteroids[i])
        #     print(stack,"stack")
        #     print(curr,"asteroids[")
        # print(stack)
        # asteroids = [5, 10, -5]

        # stack = [asteroids[0]]

        # for i in range(1, len(asteroids)):
        #     curr = asteroids[i]
        #     if stack:
        #         prev = stack[-1]
        #     else:
        #         prev = None
        #     print(prev, "prev")
            
        #     if curr < 0:
        #         print("found negative")
        #         while stack and curr < 0 < stack[-1] and stack[-1] < -curr:
        #             stack.pop()
        #         if stack and curr < 0 < stack[-1] and stack[-1] == -curr:
        #             stack.pop()
        #         elif not stack or stack[-1] < 0:
        #             stack.append(curr)
        #     else:
        #         stack.append(curr)

        #     print(stack, "stack")
        #     print(curr, "asteroid")

        # return(stack)
        stack = []

        for curr in asteroids:
            alive = True
            while stack and curr < 0 < stack[-1]:
                if stack[-1] < -curr:      # right asteroid smaller → it explodes
                    stack.pop()
                    continue
                elif stack[-1] == -curr:  # equal → both explode
                    stack.pop()
                alive = False             # curr also destroyed
                break
            if alive:
                stack.append(curr)

        return stack


        