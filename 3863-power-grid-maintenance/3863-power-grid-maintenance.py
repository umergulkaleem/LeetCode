class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 1: Find connected components
        visited = [False] * (c + 1)
        station_to_grid = {}
        grid_members = defaultdict(list)
        grid_id = 0
        
        for node in range(1, c + 1):
            if not visited[node]:
                grid_id += 1
                queue = deque([node])
                visited[node] = True
                while queue:
                    cur = queue.popleft()
                    station_to_grid[cur] = grid_id
                    grid_members[grid_id].append(cur)
                    for nei in graph[cur]:
                        if not visited[nei]:
                            visited[nei] = True
                            queue.append(nei)
        
        # Step 2: Prepare heaps and online status
        online = [True] * (c + 1)
        grid_heap = {}
        for gid, members in grid_members.items():
            heapq.heapify(members)
            grid_heap[gid] = members  # use as a min-heap
        
        # Step 3: Process queries
        result = []
        for t, x in queries:
            gid = station_to_grid[x]
            
            if t == 1:
                if online[x]:
                    result.append(x)
                else:
                    heap = grid_heap[gid]
                    while heap and not online[heap[0]]:
                        heapq.heappop(heap)  # remove offline stations
                    if not heap:
                        result.append(-1)
                    else:
                        result.append(heap[0])
            
            elif t == 2:
                online[x] = False  # mark offline
        
        return result

        