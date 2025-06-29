from tests import test_performance


def calc_fib(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

@test_performance
def main():
    f = open('input2.txt')
    number = int(f.read())
    f.close()

    fib_n = calc_fib(number)

    f = open('output.txt', 'w')
    f.write(str(fib_n))
    f.close()

if __name__ == '__main__':
    main()