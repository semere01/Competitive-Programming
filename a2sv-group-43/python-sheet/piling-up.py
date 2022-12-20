count = int(input())
for i in range(count):
    n = int(input())
    blocks = list(map(int, input().split(" ")))
    finish = False

    current = None
    if (blocks[0] > blocks[-1]):
        current = blocks.pop(0)
    else:
        current = blocks.pop()

    while (not finish and len(blocks) != 0):
        nextToPop = 0 if (blocks[0] >= blocks[-1]) else -1
        if (blocks[nextToPop] > current):
            print("No")
            finish = True
        current = blocks.pop(nextToPop)
    if not finish:
        print("Yes")
