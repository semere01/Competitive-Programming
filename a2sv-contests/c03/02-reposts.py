import sys
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (source, dest) in edges:
            self.adjList[source].append((dest, 1))
    def DFS(self, v, discovered, departure, time):
        discovered[v] = True
        for (u, w) in self.adjList[v]:
            if not discovered[u]:
                time = self.DFS(u, discovered, departure, time)
        departure[time] = v
        time = time + 1
        return time

def distParser(graph, source, n):
    departure = [-1] * n
    discovered = [False] * n
    time = 0
    for i in range(n):
        if not discovered[i]:
            time = graph.DFS( i, discovered, departure, time)
    cost = [sys.maxsize] * n
    cost[source] = 0
    for i in reversed(range(n)):
        v = departure[i]
        for (u, w) in graph.adjList[v]:
            w = -w
            if cost[v] != sys.maxsize and cost[v] + w < cost[u]:
                cost[u] = cost[v] + w
    print((min(cost) * -1) + 1)

length = int(input())
data = {}
c = 0
edges = []
for i in range(length):
    rep = [ r.capitalize() for r in input().split(" reposted ")]
    if (rep[0] not in data):
        data[rep[0]] = c
        c += 1
    if (rep[1]not in data):
        data[rep[1]] = c
        c += 1
    edges.append((data[rep[1]], data[rep[0]]))

g = Graph(edges, c)
i = 1
distParser(g, i, c)
