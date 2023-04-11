n = int(input())
total = 0

for _ in range(n):
    row = [int(i) for i in input().split()]
    total += row.count(1)
print(total // 2)

