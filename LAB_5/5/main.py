class Heap:
    def __init__(self):
        self.data = []

    def push(self, elem):
        self.data.append(elem)
        self.siftUp(len(self.data) - 1)

    def pop(self):
        self.data[0], self.data[len(self.data) - 1] = self.data[len(self.data) - 1], self.data[0]
        elem = self.data.pop()
        self.siftDown(0)
        return elem

    def siftUp(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.data[i] < self.data[parent]:
            self.data[i], self.data[parent] = self.data[parent], self.data[i]
            i = parent
            parent = (i - 1) // 2

    def siftDown(self, i):
        n = len(self.data)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == i:
                break
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest


def main():
    with open("input.txt") as file:
        n, m = map(int, file.readline().split())
        tasks = list(map(int, file.readline().split()))

    heap = Heap()
    for i in range(n):
        heap.push((0, i))


    for task_time in tasks:
        ready_time, thread_index = heap.pop()
        print(f"{thread_index} {ready_time}")
        heap.push((ready_time + task_time, thread_index))


if __name__ == "__main__":
    main()