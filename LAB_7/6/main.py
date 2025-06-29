from bisect import bisect_left

def nvp(arr):
    n = len(arr)
    tail = []
    tail_idx = []
    prev = [-1] * n

    for i in range(n):
        num = arr[i]
        pos = bisect_left(tail, num)
        if pos == len(tail):
            tail.append(num)
            tail_idx.append(i)
        else:
            tail[pos] = num
            tail_idx[pos] = i
        if pos > 0:
            prev[i] = tail_idx[pos - 1]

    res = []
    k = tail_idx[-1]
    while k != -1:
        res.append(arr[k])
        k = prev[k]
    res.reverse()
    return len(res), res


def main():
    with open("input.txt") as file:
        _ = int(file.readline())
        a = list(map(int, file.readline().split()))

    length, arr = nvp(a)

    print(length)
    print(*arr)

if __name__ == '__main__':
    main()