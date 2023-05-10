class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        outgoingPaths = {}
        incomingCounts = [0] * numCourses

        for pair in prerequisites:
            [to, fro] = pair
            incomingCounts[to] += 1
            paths = outgoingPaths.get(fro, [])
            paths.append(to)
            outgoingPaths[fro] = paths
        
        sources = deque([])
        for index, req_count in enumerate(incomingCounts):
            if req_count == 0:
                sources.append(index)
        

        courses_taken = 0
        while(sources):
            current_source = sources.popleft()
            courses_taken += 1
            source_neighbors = outgoingPaths.get(current_source, [])

            for neigh in source_neighbors:
                incomingCounts[neigh] -= 1
                if (incomingCounts[neigh] == 0):
                    sources.append(neigh)
        
        if (courses_taken < numCourses):
            return False
        return True
                




        pass