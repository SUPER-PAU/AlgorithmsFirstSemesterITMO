import random
from tests import test_performance
import sys
sys.setrecursionlimit(20000)


def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def randomized_partition(arr, l, r):
    pivot_index = random.randint(l, r)
    arr[pivot_index], arr[r] = arr[r], arr[pivot_index]
    return partition(arr, l, r)

def quicksort(arr, l, r):
    if l < r:
        q = randomized_partition(arr, l, r)
        quicksort(arr, l, q - 1)
        quicksort(arr, q + 1, r)

def partition3(arr, l, r):
    pivot = arr[r]
    lt = l
    gt = r
    i = l
    while i <= gt:
        if arr[i] < pivot:
            arr[i], arr[lt] = arr[lt], arr[i]
            i += 1
            lt += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt

def randomized_quicksort3(arr, l, r):
    if l < r:
        k = random.randint(l, r)
        arr[r], arr[k] = arr[k], arr[r]
        m1, m2 = partition3(arr, l, r)
        randomized_quicksort3(arr, l, m1 - 1)
        randomized_quicksort3(arr, m2 + 1, r)

@test_performance
def main():
    with open("10000.txt") as file:
        n = int(file.readline())
        lst = list(map(int, file.readline().split()))
        file.close()
    quicksort(lst, 0, len(lst) - 1)
    # merge_sort(lst)

    print(*lst)

if __name__ == '__main__':
    main()