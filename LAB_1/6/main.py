from tests import test_performance


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


@test_performance
def main():
    with open("input.txt") as file:
        lst = list(map(int, file.read().split()))
        file.close()
    lst_start = lst.copy()
    bubble_sort(lst)
    print(*lst)

    print("Проверка на длину: " + str(len(lst_start) == len(lst)))
    flag = True
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            flag = False
            break
    print("Проверка на условие: " + str(flag))

if __name__ == '__main__':
    main()