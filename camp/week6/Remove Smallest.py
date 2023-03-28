# https://codeforces.com/problemset/problem/1399/A

for _ in range(int(input())):
    n = int(input())
    data = [int(i) for i in input().split(" ")]
    data.sort()

    ans = "YES"
    for i in range(n - 1):
        if data[i+1] - data[i] > 1:
            ans = "NO"
            break
    
    print(ans)

