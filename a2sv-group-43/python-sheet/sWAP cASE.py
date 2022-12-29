def swap_case(s):
    final = []
    difference = ord('a') - ord('A')
    for letter in s:
        letter = ord(letter)
        if letter >= ord('a') and letter <= ord('z'):
            final.append(chr(letter - difference))
        elif letter >= ord('A') and letter <= ord('Z'):
            final.append(chr(letter + difference))
        else:
            final.append(chr(letter))
    return ''.join(final)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
