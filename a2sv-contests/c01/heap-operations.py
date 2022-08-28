from heapq import heappush, heappop, heapify
n = int(input())
data = []
commands = []

for i in range(n):
    command = input()
    if (command.split(" ")[0] == "insert"):
        # data = insert(data, int(command.split(" ")[1]))
        heappush(data, int(command.split(" ")[1]))
        commands.append(command)
        continue
    if (command.split(" ")[0] == "removeMin"):
        if (len(data)) == 0:
            commands.append("insert 5")
            # data = insert(data, 5)
            heappush(data, 5)
        # data.pop(0)
        heappop(data)
        commands.append(command)
        continue
    if (command.split(" ")[0] == "getMin"):
        expected = int(command.split(" ")[1])
        if len(data) == 0:
            commands.append(f"insert {expected}")
            commands.append(command)
            # data.append(expected)
            heappush(data, expected)
            continue
        if data[-1] < expected:
            commands = commands + (["removeMin"] * len(data)) + \
                [f"insert {expected}"] + [command]
            data = [expected]
            continue
        while data[0] < expected:
            commands.append("removeMin")
            heappop(data)
        if data[0] == expected:
            commands.append(command)
            continue
        if data[0] > expected:
            # data.insert(0, expected)
            heappush(data, expected)
            commands.append(f"insert {expected}")
            commands.append(command)
print(len(commands))
for c in commands:
    print(c)
