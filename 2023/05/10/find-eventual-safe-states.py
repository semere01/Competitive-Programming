class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        node_count = len(graph)
        incomingCounts = [0] * node_count
        outgoingLists = graph
        
        invertedGraph = [[] for _ in range(node_count)] 

        ends = []
        ends_set = set(ends)
        for index,outgoings in enumerate(outgoingLists):
            if (len(outgoings) == 0):
                ends.append(index)

        for index, neighbors in enumerate(graph):
            for neighbor in neighbors:
                invertedGraph[neighbor].append(index)
                incomingCounts[neighbor] += 1
        # sources = []
        # for index, count in enumerate(incomingCounts):
        #     if not count:
        #         sources.append(index)
        
        # valid_spaces = set()
        # valid_spaces_list = []
        # print(f": {sources}")
        # print(f"sources: {sources}")
        # while sources:
        #     current_source = sources.pop()
        #     valid_spaces.add(current_source)
        #     valid_spaces_list.append(current_source)
        #     current_neighbors = outgoingLists[current_source]

        #     for index, neigh in enumerate(current_neighbors):
        #         incomingCounts[index] -= 1
        #         if incomingCounts[index] == 0:
        #             sources.append(neigh)

        visited = set()
        crossed_count = [0] * node_count
        def dfs(index):
            if index not in visited:
                visited.add(index)
                for neighbors in invertedGraph[index]:
                    crossed_count[neighbors] += 1
                    if len(outgoingLists[neighbors]) == crossed_count[neighbors]:
                        if neighbors not in ends_set:
                            ends_set.add(neighbors)
                            ends.append(neighbors)
        
        for vs in ends:
            dfs(vs)
        return sorted(ends)



    
