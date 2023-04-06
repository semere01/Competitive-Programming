vertice_count = int(input())
data = []

for i in range(vertice_count):
    data.append([int(i) for i in input().split(' ')])


sinks = []
sources = []

for row_index in range(vertice_count):
    row = data[row_index]
    if row == ([0] * vertice_count):
        sinks.append(row_index+1)

for col_index in range(vertice_count):
    is_source = True
    for row_index in range(vertice_count):
        if data[row_index][col_index] != 0:
            is_source = False
            break
    
    if (is_source):
        sources.append(col_index+1)

print(len(sources), end = " ")
print(*(sorted(sources)))
print(len(sinks), end = " ")
print(*(sorted(sinks)))