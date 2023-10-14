def run_match(lists, command_line):
    command, *rest = command_line.split()
    match command:
        case "print":
            print(lists)
        case "insert":
            i, e = map(int, rest)
            lists.insert(i, e)
        case "remove":
            e = int(rest.pop())
            lists.remove(e)
        case "append":
            e = int(rest.pop())
            lists.append(e)
        case "sort":
            lists.sort()
        case "pop":
            lists.pop()
        case "reverse":
            lists.reverse()
                    
N = int(input())

lists = []
for _ in range(N):
    run_match(lists, input())
