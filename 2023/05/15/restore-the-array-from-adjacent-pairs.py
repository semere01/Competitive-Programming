
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        data = defaultdict(list)

        for pair in adjacentPairs:
            
            data[pair[0]].append(pair[1])
            data[pair[1]].append(pair[0])
        
        restoredArray = []
        
        for key in data.keys():
            if len(data[key]) == 1:
                restoredArray.append(key)
                restoredArray.append(data[key][0])
                break
        
        visited = set(restoredArray)
        while True:
            nextPair = data[restoredArray[-1]]
            
            if (len(nextPair)) == 1:
                restoredArray.append(nextPair[0])
                break
            else:
                for k in nextPair:
                    if (k not in visited):
                        restoredArray.append(k)
                        visited.add(k)
        restoredArray.pop()
        return restoredArray
    
