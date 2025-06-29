MOD = 10**6 + 5


class HashSet:
    def __init__(self):
        self.table = [[] for _ in range(MOD)]

    def hash(self, x):
        return x  % MOD

    def add(self, x):
        h = self.hash(x)
        if x not in self.table[h]:
            self.table[h].append(x)

    def delete(self, x):
        h = self.hash(x)
        if x in self.table[h]:
            self.table[h].remove(x)

    def exists(self, x):
        h = self.hash(x)
        return x in self.table[h]

def main():
    hs = HashSet()

    with open("input.txt") as file:
        n = int(file.readline())
        for _ in range(n):
            cmd, val = file.readline().strip().split()
            x = int(val)

            if cmd == 'A':
                hs.add(x)
            elif cmd == 'D':
                hs.delete(x)
            elif cmd == '?':
                print('Y' if hs.exists(x) else 'N')
if __name__ == '__main__':
    main()