class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        # keys = []
        # for i in range(len(rooms)):
        #     if i not in keys and i != 0:
        #         return False
        #     for k in rooms[i]:
        #         if k not  in keys:
        #             keys.append(k)
        #     print(keys,"keys")
        #     print(i,"at")
        # return True
        visited = set()
        stack = [0]  # start with room 0
        
        while stack:
            room = stack.pop()
            if room not in visited:
                visited.add(room)
                for key in rooms[room]:
                    if key not in visited:
                        stack.append(key)
        
        return len(visited) == len(rooms)
