from tests import test_performance


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

@test_performance
def main():
    with open("best_case.txt") as file:
        lst = list(map(int, file.read().split()))
        file.close()

    lst = merge_sort(lst)

    print(*lst)

    flag = True
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            flag = False
            break
    print("Проверка на условие: " + str(flag))


if __name__ == '__main__':
    main()