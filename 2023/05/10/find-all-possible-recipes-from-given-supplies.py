class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        food_count = len(recipes)

        incomingCount = [0] * food_count
        outgoingList = {}

        for index, ingredientList in enumerate(ingredients):
            incomingCount[index] += len(ingredientList)
            for i in ingredientList:
                ingredient_dependents = outgoingList.get(i, [])
                ingredient_dependents.append((recipes[index], index))
                outgoingList[i] = ingredient_dependents
        
        possibleFoods = []

        while supplies:
            current_supply = supplies.pop()
            supply_deps = outgoingList.get(current_supply, [])
            for name, index in supply_deps:
                incomingCount[index] -=1 
                if (incomingCount[index] == 0):
                    supplies.append(name)
                    possibleFoods.append(name)
        
        return possibleFoods

            