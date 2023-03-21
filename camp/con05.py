[days, assistants] = [ int(i) for i in input().split(" ")]

presence = [0] * days


for assistant in range(assistants):
    [firstDay, lastDay] = [ int(i) for i in input().split(" ")]
    presence[firstDay] += 1
    presence[lastDay] -= 1

current = presence[0]

# for attendance in presence:
for i in range(1,days):
    if (current) <= 0:
        print("YES")
        break
    attendance = presence[i]
    current += attendance

print("NO")
    




    