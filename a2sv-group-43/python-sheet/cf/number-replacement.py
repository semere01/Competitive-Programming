from collections import defaultdict


test_case_count = int(input())

for test_case in range(test_case_count):
    length = int(input())
    numbers = input().split(" ")
    letters = list(input())

    key_mapping = {}
    is_valid_list_pair = True

    for pointer in range(length):
        letter = letters[pointer]
        number = int(numbers[pointer])


        if number not in key_mapping:
            key_mapping[number] = letter
        elif key_mapping[number] == letter:
            pass
        else:
            print("NO")
            is_valid_list_pair = False
            break

    if (is_valid_list_pair):
        print("YES")
