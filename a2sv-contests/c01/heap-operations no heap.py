
n = int(input())
data = []
commands = []


def insert(list, n):
    index = len(list)
    for i in range(len(list)):
        if list[i] > n:
            index = i
            break
    if index == len(list):
        list = list[:index] + [n]
    else:
        list = list[:index] + [n] + list[index:]
    return list


for i in range(n):
    command = input()
    if (command.split(" ")[0] == "insert"):
        data = insert(data, int(command.split(" ")[1]))
        commands.append(command)
        continue
    if (command.split(" ")[0] == "removeMin"):
        if (len(data)) == 0:
            commands.append("insert 5")
            data = insert(data, 5)
        data.pop(0)
        commands.append(command)
        continue
    if (command.split(" ")[0] == "getMin"):
        expected = int(command.split(" ")[1])
        if len(data) == 0:
            commands.append(f"insert {expected}")
            commands.append(command)
            data.append(expected)
            continue
        if data[-1] < expected:
            commands += (["removeMin"] * len(data)) + \
                [f"insert {expected}", command]
            data = [expected]
            continue
        counter = 0
        while data[counter] < expected:
            counter += 1
            commands.append("removeMin")
        data = data[counter:]
        if data[0] == expected:
            commands.append(command)
            continue
        if data[0] > expected:
            data.insert(0, expected)
            commands.append(f"insert {expected}")
            commands.append(command)
print(len(commands))
for c in commands:
    print(c)
