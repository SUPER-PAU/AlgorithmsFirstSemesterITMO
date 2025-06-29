import random

from tests import test_performance


def calc_dist(point):
    x, y = point
    return (x ** 2) + (y ** 2)

def partition(points, left, right, pivot_index):
    pivot_distance = calc_dist(points[pivot_index])
    points[pivot_index], points[right] = points[right], points[pivot_index]
    store_index = left
    for i in range(left, right):
        if calc_dist(points[i]) < pivot_distance:
            points[store_index], points[i] = points[i], points[store_index]
            store_index += 1
    points[right], points[store_index] = points[store_index], points[right]
    return store_index

def quickselect(points, left, right, K):
    if left < right:
        pivot_index = random.randint(left, right)
        pivot_index = partition(points, left, right, pivot_index)
        if pivot_index == K:
            return
        elif pivot_index < K:
            quickselect(points, pivot_index + 1, right, K)
        else:
            quickselect(points, left, pivot_index - 1, K)

def k_closest(points, K):
    quickselect(points, 0, len(points) - 1, K)

    result = sorted(points[:K], key=calc_dist)
    return result

@test_performance
def main():
    with open('input.txt') as file:
        n, k = map(int, file.readline().split())
        points = []
        for _ in range(n):
            x, y = map(int, file.readline().split())
            points.append((x, y))
        file.close()

    closest = k_closest(points, k)
    print(*closest)

if __name__ == '__main__':
    main()
