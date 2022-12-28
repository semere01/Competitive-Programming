input()
a = set(input().split(" "))
input()
b = set(input().split(" "))

count = 0

for el in a:
    if (el not in b):
        count += 1

print(count)
