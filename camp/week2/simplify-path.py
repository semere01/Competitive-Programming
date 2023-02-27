class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for node in path:
            if node == '' or node == '.':
                continue
            if node == '..':
                if (len(stack)):stack.pop()
            else:
                stack.append(node)
        return "/" + "/".join(stack)

