a = set(map(int, input().split(' ')))
n = int(input())
isSub = True
for i in range(n):
    currentSet = set(map(int, input().split(' ')))
    if (currentSet.issubset(a) and len(currentSet) < len(a)):
        pass
    else:
        isSub = False
        print("False")
        break

if (isSub):
    print("True")
