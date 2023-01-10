from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        data = defaultdict(list)
        for path in paths:
            path_split = path.split(" ")
            directory = path_split[0]

            for file_index in range(1, len(path_split)):
                file_with_content = path_split[file_index].split("(")
                file_name = file_with_content[0]
                file_content = file_with_content[1].split(")")[0]
                file_with_dir = directory+"/"+file_name
                data[file_content].append(file_with_dir)
        return [v for v in data.values() if len(v) > 1]


a = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)",
     "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]

print(Solution().findDuplicate(a))
