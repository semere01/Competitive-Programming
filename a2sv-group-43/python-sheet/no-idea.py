ln, lm = input().split(" ")
data = list(map(int, input().split(" ")))
happy = list(map(int, input().split(" ")))
sad = list(map(int, input().split(" ")))

score = 0

# o(nxm)
# TODO: OPTIMIZE OPTIMIZE OPTIMIZE
for d in data:  # o(n)
    if (d in happy):  # o(m)
        score += 1
    elif (d in sad):  # o(m)
        score -= 1

print(score)
