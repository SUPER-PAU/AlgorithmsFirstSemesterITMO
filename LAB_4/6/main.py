class MinQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _push(self, stack, value):
        curr_min = value
        if stack:
            curr_min = min(value, stack[-1][1])
        stack.append((value, curr_min))

    def addQueue(self, value):
        self._push(self.in_stack, value)

    def deleteQueue(self):
        if not self.out_stack:
            while self.in_stack:
                val = self.in_stack.pop()[0]
                self._push(self.out_stack, val)
        self.out_stack.pop()

    def get_min(self):
        mins = []
        if self.in_stack:
            mins.append(self.in_stack[-1][1])
        if self.out_stack:
            mins.append(self.out_stack[-1][1])
        return min(mins)



def main():
    with open("input.txt") as file:
        _ = file.readline()
        lines = file.readlines()

    queue = MinQueue()

    for line in lines:
        line = line.strip()
        if line.startswith('+'):
            _, num = line.split()
            queue.addQueue(int(num))
        elif line == '-':
            queue.deleteQueue()
        elif line == '?':
            print(queue.get_min())

if __name__ == '__main__':
    main()
