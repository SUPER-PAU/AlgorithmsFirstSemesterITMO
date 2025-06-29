class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class LinkedMap:
    def __init__(self):
        self.map = {}
        self.order = {}
        self.head = None
        self.tail = None

    def put(self, key, value):
        if key in self.map:
            self.map[key] = value
        else:
            self.map[key] = value
            node = Node(key)
            self.order[key] = node
            if self.tail:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            else:
                self.head = self.tail = node

    def get(self, key):
        return self.map.get(key)

    def delete(self, key):
        if key not in self.map:
            return
        del self.map[key]

        node = self.order.pop(key)
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def prev(self, key):
        if key not in self.order:
            return "<none>"
        prev_node = self.order[key].prev
        return self.map.get(prev_node.key) if prev_node else "<none>"

    def next(self, key):
        if key not in self.order:
            return "<none>"
        next_node = self.order[key].next
        return self.map.get(next_node.key) if next_node else "<none>"

def main():
    with open("input.txt") as file:
        n = int(file.readline())
        commands = [file.readline().strip() for _ in range(n)]

    lm = LinkedMap()

    for cmd in commands:
        parts = cmd.split()
        if parts[0] == 'put':
            _, k, v = parts
            lm.put(k, v)
        elif parts[0] == 'get':
            print(lm.get(parts[1]))
        elif parts[0] == 'delete':
            lm.delete(parts[1])
        elif parts[0] == 'prev':
            print(lm.prev(parts[1]))
        elif parts[0] == 'next':
            print(lm.next(parts[1]))

if __name__ == '__main__':
    main()
