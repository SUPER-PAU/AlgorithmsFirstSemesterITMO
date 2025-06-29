from tests import test_performance

def count_occurrences(arr, candidate, left, right):
    count = 0
    for i in range(left, right):
        if arr[i] == candidate:
            count += 1
    return count

def majority_element_rec(arr, left, right):
    if right - left == 1:
        return arr[left]
    if left >= right:
        return None

    mid = (left + right) // 2
    left_major = majority_element_rec(arr, left, mid)
    right_major = majority_element_rec(arr, mid, right)

    if left_major == right_major:
        return left_major

    count_left = count_occurrences(arr, left_major, left, right) if left_major is not None else 0
    count_right = count_occurrences(arr, right_major, left, right) if right_major is not None else 0

    if count_left > (right - left) // 2:
        return left_major
    if count_right > (right - left) // 2:
        return right_major

    return None


@test_performance
def main():
    with open("input.txt") as file:
        lst = list(map(int, file.readline().split()))
        file.close()

    candidate = majority_element_rec(lst, 0, len(lst))

    print(candidate)


if __name__ == '__main__':
    main()