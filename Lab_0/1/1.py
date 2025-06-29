# 1 сумма
a, b = map(int, input().split())
print(a + b)
# 2 b в квадрате
a, b = map(int, input().split())
print(a + b ** 2)


# 3 сумма из файла
f = open('input.txt')
numbers = list(map(int, f.read().split()))
f.close()
result = a + b
f = open('output.txt', 'w')
f.write(str(result))
f.close()

# 4 a + b^2 из файла
f = open('input.txt')
numbers = list(map(int, f.read().split()))
f.close()
result = a + b ** 2
f = open('output2.txt', 'w')
f.write(str(result))
f.close()