
inp = list(input())
inv = [int(i) for i in input().split(" ")]
cost = [int(i) for i in input().split(" ")]
money = int(input())

recipe = [0, 0, 0]
for letter in inp:
    if letter == "B":
        recipe[0] += 1
    if letter == "S":
        recipe[1] += 1
    if letter == "C":
        recipe[2] += 1

recipe_cost = (recipe[0]*cost[0]) + (recipe[1]*cost[1]) + (recipe[2]*cost[2])

buyable_burgers = money // recipe_cost
remaining_money = money % recipe_cost


arr = []
if recipe[0]:
    arr.append(inv[0] // recipe[0])
if recipe[1]:
    arr.append(inv[1] // recipe[1])
if recipe[2]:
    arr.append(inv[2] // recipe[2])
makeable_burgers = min(arr)

remaining_inventory = [inv[0] - (makeable_burgers*recipe[0]), inv[1] -
                       (makeable_burgers*recipe[1]), inv[2] - (makeable_burgers*recipe[2]), ]

inv_def = [
    recipe[0] - remaining_inventory[0],
    recipe[1] - remaining_inventory[1],
    recipe[2] - remaining_inventory[2],
]

inv_dev_cost = max(inv_def[0] * cost[0]*recipe[0], 0) + \
    max(inv_def[1] * cost[1]*recipe[1], 0) + max(inv_def[2] * cost[2]*recipe[2], 0)


last_burger = 0

if (remaining_money >= inv_dev_cost):
    last_burger = 1
# print(f"cost - ${cost}")
# print(f"recipe - ${recipe}")
# print(f"recipe_cost - ${recipe_cost}")
# print(f"inventory - ${inv}")
# print(f"makeable_burgers - ${makeable_burgers}")

# print()
# print(f"remaining_inventory - ${remaining_inventory}")
# print(f"remaining_money - ${remaining_money}")
# print(f"buyable_burgers - ${buyable_burgers}")
# print(f"inv_def - ${inv_def}")
print(makeable_burgers + buyable_burgers + last_burger)
