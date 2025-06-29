from tests import test_performance


def insertion_sort(lst):
    for j in range(1, len(lst)):
        key = lst[j]
        i = j - 1
        while i >= 0 and lst[i] > key:
            lst[i + 1] = lst[i]
            i -= 1
        lst[i + 1] = key

@test_performance
def main():
    with open("input.txt") as file:
        lst = list(map(int, file.read().split()))
        file.close()
    insertion_sort(lst)
    print(*lst)

if __name__ == '__main__':
    main()