vertice_count = int(input())
rows =[]

for row_index in range(vertice_count):
    rows.append([int(i) for i in input().split()])

adjacencyMap = []

for row_index in range(vertice_count):
    adjacencyMap.append([])
    for col_index in range(vertice_count):
        datum = rows[row_index][col_index]
        if (datum):
            adjacencyMap[row_index].append(col_index+1)

for row_index in range(vertice_count):
    print(len(adjacencyMap[row_index]), end = " ")
    print(*(adjacencyMap[row_index]))


