from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # 1. Initial people who know the secret
        knows = [False] * n
        knows[0] = True
        knows[firstPerson] = True
        
        # 2. Sort meetings by time
        meetings.sort(key=lambda x: x[2])
        
        i = 0
        m = len(meetings)
        while i < m:
            currentTime = meetings[i][2]
            
            # 3. Group all meetings happening at the same 'currentTime'
            local_graph = defaultdict(list)
            people_at_time = set()
            
            while i < m and meetings[i][2] == currentTime:
                u, v, _ = meetings[i]
                local_graph[u].append(v)
                local_graph[v].append(u)
                people_at_time.add(u)
                people_at_time.add(v)
                i += 1
            
            # 4. BFS starting ONLY from people who already know the secret
            queue = deque([p for p in people_at_time if knows[p]])
            
            while queue:
                curr = queue.popleft()
                for neighbor in local_graph[curr]:
                    if not knows[neighbor]:
                        knows[neighbor] = True
                        queue.append(neighbor)
        
        # 5. Return all indices where knows[i] is True
        return [i for i in range(n) if knows[i]]