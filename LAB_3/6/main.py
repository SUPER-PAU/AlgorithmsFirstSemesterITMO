from tests import test_performance
from LAB_3.mergeSort import merge_sort

@test_performance
def main():
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        A = list(map(int, f.readline().split()))
        B = list(map(int, f.readline().split()))

    C = [a * b for a in A for b in B]

    C = merge_sort(C)

    result = sum(C[i] for i in range(0, len(C), 10))
    print(result)


if __name__ == "__main__":
    main()
