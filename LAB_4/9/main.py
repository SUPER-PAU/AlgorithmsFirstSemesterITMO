
def balance(left, right):
    while len(left) < len(right):
        left.append(right.pop(0))
    while len(left) > len(right) + 1:
        right.insert(0, left.pop())


def main():
    with open("input2.txt") as file:
        _ = file.readline()
        lines = file.readlines()

    left = []
    right = []


    for line in lines:
        line = line.strip()
        if line.startswith('+'):
            _, val = line.split()
            right.append(val)
        elif line.startswith('*'):
            _, val = line.split()
            left.append(val)
        elif line == '-':
            print(left.pop(0))

        balance(left, right)

if __name__ == '__main__':
    main()
