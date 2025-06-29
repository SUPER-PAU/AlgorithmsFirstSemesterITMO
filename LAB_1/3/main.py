from tests import test_performance


def insertion_sort_rev(lst):
    for j in range(1, len(lst)):
        i = j
        while i > 0 and lst[i - 1] < lst[i]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1

@test_performance
def main():
    with open("input.txt") as file:
        lst = list(map(int, file.read().split()))
        file.close()
    insertion_sort_rev(lst)
    print(*lst)

if __name__ == '__main__':
    main()