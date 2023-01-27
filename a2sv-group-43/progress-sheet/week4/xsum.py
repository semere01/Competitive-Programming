for _ in range(int(input())):
    [num_of_rows, num_of_cols] = [int(i) for i in input().split(" ")]
    data = []
    for i in range(num_of_rows):
        data.append([int(i) for i in input().split(" ")])

    right_diag_sums = {}
    for i in range(num_of_cols):
        r = 0
        c = i
        current_sum = 0
        while (r < num_of_rows and c < num_of_cols):
            current_sum += data[r][c]
            r += 1
            c += 1
        right_diag_sums[(0, i)] = current_sum

    for i in range(num_of_rows):
        r = i
        c = 0
        current_sum = 0
        while (r < num_of_rows and c < num_of_cols):
            current_sum += data[r][c]
            r += 1
            c += 1
        right_diag_sums[(i, 0)] = current_sum

    left_diag_sums = {}
    for i in range(1, num_of_rows):
        r = i
        c = num_of_cols-1
        current_sum = 0
        while (r < num_of_rows and c >= 0):
            current_sum += data[r][c]
            r += 1
            c -= 1
        left_diag_sums[i, num_of_cols-1] = current_sum

    for i in range(num_of_cols):
        r = 0
        c = i
        current_sum = 0
        while (r < num_of_rows and c >= 0):
            current_sum += data[r][c]
            r += 1
            c -= 1
        left_diag_sums[0, i] = current_sum

    maximum = 0

    for r in range(num_of_rows):
        for c in range(num_of_cols):
            tr = (0, r+c)
            if (r+c >= num_of_cols):
                tr = (r+c-num_of_cols+1, num_of_cols-1)

            tl = None
            if (r > c):  # bottom left of matrix
                tl = (r-c, 0)
            else:
                tl = (0, c-r)
            # print(left_diag_sums[tr], end=' ')
            # print(tr, end=' ')

            # print(left_diag_sums[tr] + right_diag_sums[tl], end=' ')
            if maximum < (left_diag_sums[tr] + right_diag_sums[tl])-data[r][c]:
                maximum = (left_diag_sums[tr] + right_diag_sums[tl])-data[r][c]
        # print()

    print(maximum)
    # print()
