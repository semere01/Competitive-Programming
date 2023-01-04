test_case_count = int(input())
for test_case in range(test_case_count):
    size_strings = input().split(' ')

    size_numbers = []

    for size_string in size_strings:
        if (size_string == "M"):
            size_numbers.append(0)
        elif (size_string[-1] == "S"):
            number_of_x =  len(size_string)
            size = number_of_x * -1
            size_numbers.append(size)
        elif (size_string[-1] == "L"):
            number_of_x = len(size_string)
            size = number_of_x * 1
            size_numbers.append(size)
    
    if (size_numbers[0] > size_numbers[1]):
        print(">")
    elif (size_numbers[0] < size_numbers[1]):
        print("<")
    else:
        print("=")
