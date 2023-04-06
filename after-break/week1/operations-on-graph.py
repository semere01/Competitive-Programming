from collections import defaultdict


vertice_count = int(input())
# data = [set() for verice in range(vertice_count)]
data = defaultdict(list)


# [{}, {}, {}]

operation_count = int(input())
for action_number in range(operation_count):
    action = [int(i) for i in input().split()]
    if (action[0] == 1):
        v1 = action[1]
        v2 = action[2]
        data[v1].append(v2)
        data[v2].append(v1)
        # data[v1-1].add(v2)
        # data[v2-1].add(v1)
    elif (action[0] == 2):
        v = action[1]
        current_data = data[v]
        if (current_data):
            print(*current_data)