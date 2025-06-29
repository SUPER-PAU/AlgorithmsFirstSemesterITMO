from tests import test_performance


def calc_fib(n):
    n %= 60
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, (prev + curr) % 10
    return curr


@test_performance
def main():
    f = open('input3.txt')
    number = int(f.read())
    f.close()

    fib_n = calc_fib(number)

    f = open('output.txt', 'w')
    f.write(str(fib_n))
    f.close()


if __name__ == '__main__':
    main()