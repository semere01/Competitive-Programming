[num_of_rows, num_of_cols] = [int(i) for i in input().split(" ")]
data = []
for i in range(num_of_rows):
    data.append(list(input()))


row_map = [(set(), set()) for i in range(num_of_rows)]
col_map = [(set(), set()) for i in range(num_of_cols)]

for r in range(len(data)):
    for c in range(len(data[0])):
        letter = data[r][c]
        if (letter in row_map[r][0]):
            row_map[r][1].add(letter)
        row_map[r][0].add(letter)

        if (letter in col_map[c][0]):
            col_map[c][1].add(letter)
        col_map[c][0].add(letter)
ans = []

for r in range(len(data)):
    for c in range(len(data[0])):
        letter = data[r][c]
        if (letter not in row_map[r][1] and letter not in col_map[c][1]):
            ans.append(letter)

print(''.join(ans))


#         # letter = data[r][c]
#         # index = ord(letter)-97
#         # if (count[index]) == False:
#         #     continue
#         # if r in count[index][0]:
#         #     count[index] = False
#         #     continue
#         # if c in count[index][1]:
#         #     count[index] = False
#         #     continue
#         # count[index][0].add(r)
#         # count[index][1].add(c)
# print(count)
# ans = []
# for r in range(len(data)):
#     for c in range(len(data[0])):
#         letter = data[r][c]
#         index = ord(letter)-97
#         if (count[index]) == False:
#             continue
#         ans.append(letter)

# print(''.join(ans))
