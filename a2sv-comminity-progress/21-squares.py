# n, m, a
v = [int(x) for x in input().split(' ')]
n = v[0]
m = v[1]
a = v[2]
side1 = ((n/a) if (n/a == n//a) else (n//a) + 1)
side2 = ((m/a) if (m/a == m//a) else (m//a) + 1)
# side2 = (m//a) + 1

print(int(side1 * side2))