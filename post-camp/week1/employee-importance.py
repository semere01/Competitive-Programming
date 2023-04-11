"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {}
        for datum in employees:
            id_ = datum.id
            imp = datum.importance
            children = datum.subordinates
            graph[id_] = [imp, children]

        def dfs(employee):
            my_imp = graph[employee][0]
            kids_imp = 0
            for kid_id in (graph[employee])[1]:
                v = dfs(kid_id)
                kids_imp += v
            return (my_imp + kids_imp)
        return dfs(id)