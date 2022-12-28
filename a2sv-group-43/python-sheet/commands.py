if __name__ == '__main__':
    N = int(input())
    data = []
    for index in range(N):
        command = input()
        command_word = command.split(" ")
        if command_word[0] == "insert":
            data.insert(int(command_word[1]), int(command_word[2]))
        elif command_word[0] == "print":
            print(data)
        elif command_word[0] == "remove":
            d = int(command_word[1])
            if d in data:
                data.remove(d)
        elif command_word[0] == "append":
            data.append(int(command_word[1]))
        elif command_word[0] == "sort":
            data.sort()
        elif command_word[0] == "pop":
            data.pop()
        elif command_word[0] == "reverse":
            data.reverse()
