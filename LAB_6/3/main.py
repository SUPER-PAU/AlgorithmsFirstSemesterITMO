P = 1000000007
X = 263


class HashSet:
    def __init__(self, m):
        self.m = m
        self.table = [[] for _ in range(m)]

    def hash(self, s):
        hash_val = 0
        for i in range(len(s)):
            hash_val += ord(s[i]) * (X ** i)
        return (hash_val % P) % self.m

    def add(self, x):
        h = self.hash(x)
        if x not in self.table[h]:
            self.table[h].insert(0, x)

    def delete(self, x):
        h = self.hash(x)
        if x in self.table[h]:
            self.table[h].remove(x)

    def exists(self, x):
        h = self.hash(x)
        return "yes" if x in self.table[h] else "no"

    def check(self, i):
        return " ".join(self.table[i])


def main():
    with open("input.txt") as file:
        m = int(file.readline())
        n = int(file.readline())
        lines = [file.readline().strip() for _ in range(n)]

    ht = HashSet(m)

    for line in lines:
        cmd, val = line.split()
        if cmd == "add":
            ht.add(val)
        elif cmd == "del":
            ht.delete(val)
        elif cmd == "find":
            print(ht.exists(val))
        elif cmd ==  "check":
            print(ht.check(int(val)))


if __name__ == "__main__":
    main()
