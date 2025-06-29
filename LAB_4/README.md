# Лабораторная 4 
## Задание 1 - Стэк
Стэк - Это структура данных, элементы которого можно добавлять в конец массива
и извелекать также только с конца.
Хранить Данные будем в списке.

Работа со Стэком
```python
def pushStack(arr, val):
    arr.append(val)

def popStack(arr):
    return arr.pop()
```

Интерфейс для задачи:
```python
with open("input.txt") as file:
    lines = file.readlines()

stack = []

for line in lines:
    line.strip()
    if line.startswith("+"):
        command, value = line.split()
        pushStack(stack, int(value))
    elif line.startswith("-"):
        print(popStack(stack))
```


## Задание 3 - Скобочная последовательность 
Идея задачи: для каждой `(` или `[` должна быть своя `)` или `]`

реализовать эту проверку можно с помощью стека:
- будем добавлять символы `([` в стек, и удалять их из стека, если встретится `)]`
- таким образом стек останется заполненным при неправильной последовательности
- также необходимо учитывать момент, когда есть `])`, но стэк пуст

функция проверки скобок
```python
def checkBrackets(string):
    stack = []
    pairs = {')': '(', ']': '['}

    for char in string:
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack
```

работа с файлом
```python
with open("input.txt") as file:
    _ = file.readline()
    lines = file.readlines()

for line in lines:
    line.strip()
    if (checkBrackets(line)):
        print("Yes")
    else:
        print("No")
```

## Задание 6 - Очередь с минимумом

необходимо реализовать очередь, которая будет овечать на запрос о своем минимальном элементе

Это можно сделать с помощью Очереди на 2-ух стэках
- есть 2 очереди `in_queue` и `out_queue`, которые состаят из кортежей (`значиние`, `мин число до этого элемента`)
- в `in_queue` поступают новые элементы, из `out_queue` удаляются элементы.
- при удалении проверяем `out_queue`, если он пуст, то переносим все элементы из `in_queue`
  - при этом пересчитываем минимум, добавляя элементы методом `_push`
  - Вставляем элементы в обратном порядке, тем самым сохраняя инвариант очереди.
  - `in_queue` очищается.
- Поиск минимума происходит в обоих стэках на последнем элементе. Выводится Минимальный из них.

Реализация очереди
```python
class MinQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _push(self, stack, value):
        curr_min = value
        if stack:
            curr_min = min(value, stack[-1][1])
        stack.append((value, curr_min))

    def addQueue(self, value):
        self._push(self.in_stack, value)

    def deleteQueue(self):
        if not self.out_stack:
            while self.in_stack:
                val = self.in_stack.pop()[0]
                self._push(self.out_stack, val)
        self.out_stack.pop()

    def get_min(self):
        mins = []
        if self.in_stack:
            mins.append(self.in_stack[-1][1])
        if self.out_stack:
            mins.append(self.out_stack[-1][1])
        return min(mins)
```

работа с файлами
```python
def main():
    with open("input.txt") as file:
        _ = file.readline()
        lines = file.readlines()

    queue = MinQueue()

    for line in lines:
        line = line.strip()
        if line.startswith('+'):
            _, num = line.split()
            queue.addQueue(int(num))
        elif line == '-':
            queue.deleteQueue()
        elif line == '?':
            print((queue.get_min()))
```

## Задание 9 - Поликлиника
необходимо реализовать очередь, с возможностью добавления в середину. 
Это можно сделать с помощью "Двойной очереди" левой и правой.
В конце каждого действия они будут балансироваться.
- добавление обычного пациента происходит в правую очередь, а привелигерованного - в левую
- извлечение происходит из левого.
- балансировка происходит путем извлечения крайних элементов первого списка и вставку во второй
    - балансировка происходит, если длины не равны (левый больше при нечетной длине)
  
Балансировка
```python
def balance(left, right):
    while len(left) < len(right):
        left.append(right.pop(0))
    while len(left) > len(right) + 1:
        right.insert(0, left.pop())
```

работа с интерфейсом
```python
with open("input2.txt") as file:
    _ = file.readline()
    lines = file.readlines()

left = []
right = []

for line in lines:
    line = line.strip()
    if line.startswith('+'):
        _, val = line.split()
        right.append(val)
    elif line.startswith('*'):
        _, val = line.split()
        left.append(val)
    elif line == '-':
        print(left.pop(0))

    balance(left, right)
```
