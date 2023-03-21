n = list(input())
out = []

if len(n) == 0:
    print("")
else:
    for digit in n:
        if int(digit) >= 5:
            out.append(str(9-int(digit)))
        else:
            out.append(str(digit))

    if out[0] == "0":
        out[0] = "9"

    print(''.join(out))