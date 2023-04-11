class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = {}
        city_count = len(isConnected)

        for city_index in range(city_count):
            graph[city_index] = set()
            my_roads = isConnected[city_index]
            for road_index in range(len(my_roads)):
                road = my_roads[road_index]
                if (road):
                    graph[city_index].add(road_index)

        visited = set()

        group_count = 0
        for city_index in range(city_count):
            if city_index not in visited:
                print(f"new city_index {city_index}")
                self.dfs(city_index, graph, visited)
                group_count += 1

        return group_count

    # function to visit all cities
    def dfs(self, v, graph, visited):
        print(f"dfs: {v}")
        visited.add(v)
        neighbors = graph[v]
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dfs(neighbor, graph, visited)
