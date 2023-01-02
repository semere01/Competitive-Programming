input()
data = [int(i) for i in input().split(' ')]

counter = 0
max = data[0]
min = data[0]
for i in data:
    if i > max:
        max = i
        counter += 1
    if i < min:
        min = i
        counter += 1

print(counter)