t = int(input())
for i in range (t):
    n = input()
    if (int(n)%2)==0:
        print(0)
        continue
    if int(n[0]) % 2 == 0:
        print(1)
        continue
    hasEven = False
    for digit in n:
        if int(digit) % 2 == 0:
            hasEven = True
            break
    if hasEven:
        print(2)
        continue
    else:
        print(-1)
