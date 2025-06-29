def pushStack(arr, val):
    arr.append(val)

def popStack(arr):
    return arr.pop()

def main():
    with open("input.txt") as file:
        lines = file.readlines()

    stack = []

    for line in lines:
        line.strip()
        if line.startswith("+"):
            command, value = line.split()
            pushStack(stack, int(value))
        elif line.startswith("-"):
            print(popStack(stack))

if __name__ == "__main__":
    main()
