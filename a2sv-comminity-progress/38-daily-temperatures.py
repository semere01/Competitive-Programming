import copy
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        temperaturesCopy = copy.deepcopy(temperatures)
        tempCache = [[]]*71
        finalList = []
        for i in range(len(temperatures)):
            t = temperatures[i]
            temperatures[i] = -1
            tempCache[t-30] = tempCache[t-30] + [i]

        for currentDay in range(len(temperaturesCopy)):
            temperatureToday = temperaturesCopy[currentDay]
            if temperatureToday==100:
                finalList.append(-1)
                continue 
            closestDay = -1
            for occurenceDays in tempCache[t-29:]:
                for day in occurenceDays:
                    if closestDay == -1 or closestDay > day: closestDay = day
            if closestDay >= 0: closestDay -= currentDay
            finalList.append(closestDay)
        
        return finalList


tests = [[73,74,75,71,69,72,76,73]]
for test in tests: print(Solution().dailyTemperatures(test))



        
        


        
