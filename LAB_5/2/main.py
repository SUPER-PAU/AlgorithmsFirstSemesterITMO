import sys
sys.setrecursionlimit(10**6)

def main():
    with open("input.txt") as file:
        n = int(file.readline())
        parent_indexes = list(map(int, file.readline().split()))

    tree = [[] for _ in range(n)]
    root = None

    for child in range(n):
        parent = parent_indexes[child]
        if parent == -1:
            root = child
        else:
            tree[parent].append(child)

    def dfs(node):
        if not tree[node]:
            return 1
        return 1 + max(dfs(child) for child in tree[node])

    height = dfs(root)
    print(height)

if __name__ == "__main__":
    main()