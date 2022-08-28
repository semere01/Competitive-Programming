n = int(input())
[ax, ay] = (int(i) for i in (input().split(" ")))
[bx, by] = (int(i) for i in (input().split(" ")))
[cx, cy] = (int(i) for i in (input().split(" ")))
 
 
def defineQuadrant(x,y):
    global ax, ay
    if (x > ax) and (y > ay):
        return 1
    elif (x < ax ) and (y > ay):
        return 2
    elif (x < ax ) and (y < ay):
        return 3
    elif (x > ax) and (y < ay):
        return 4
 
if defineQuadrant(bx, by) == defineQuadrant(cx, cy):
    print("YES")
else:
    print("NO")