import textwrap


def wrap(string, max_width):
    prev = 0
    final = ""

    for i in range(max_width, len(string), max_width):
        final += string[prev:i] + "\n"
        prev = i
    final += string[prev:]
    return final


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
