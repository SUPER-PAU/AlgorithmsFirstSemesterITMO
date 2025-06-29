def checkBrackets(string):
    stack = []
    pairs = {')': '(', ']': '['}

    for char in string:
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack

def main():
    with open("input.txt") as file:
        _ = file.readline()
        lines = file.readlines()

    for line in lines:
        line.strip()
        if (checkBrackets(line)):
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()