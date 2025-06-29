# Лабораторная 5 - деревья и куча
## Задание 2 - высота дерева

Дерево будем хранить в списке, где каждый элемент списка - список индексов детей вершины.
Для удобного построения дерева можно сразу создать вложенный список длины `n`

```python
with open("input.txt") as f:
    n = int(f.readline())
    parent_indexes = list(map(int, f.readline().split()))

tree = [[] for _ in range(n)]
root = None
```

на вход поступили n индексов родителей `i`x детей.
`-1` индекс родителя - вершина = корень дерева

заполнение дерева
```python
for child in range(n):
    parent = parent_indexes[child]
    if parent == -1:
        root = child
    else:
        tree[parent].append(child)
```

Далее необходимо узнать высоту построенного дерева. сделать это можно с помощью рекурсивного обхода в высоту.
- Мы начинаем с корня дерева и запускаем рекурсию от всех детей.
- Если натыкаемся на вершину без детей, то просто возвращаем `1` - это лист.
- Если вершина с детьми, то выбираем макс результат.
Итого получаем высоту дерева
```python
def dfs(node):
    if not tree[node]:
        return 1
    return 1 + max(dfs(child) for child in tree[node])
```


## Задача 5 - потоки

Чтобы решить эту задачу, использую приоритетную очередь (мин. кучу).

Логика мин кучи
- дети вершины всегда меньше ее значения
- при добавлении элемент вставляется в конец и просеивается вверх `siftUP`
  - `siftUp` просеивает элемент рекурсивно или итеративно (у меня цикл `while`) в начало списка, пока он не будет удовлетворять условию мин кучи
- при удалении первый элемент удаляется, а последний переносится в начало и просеивается вниз
`siftDOWN`
  - `siftDOWN` просеивает элемент в конец списка, выбирая минимальный из детей, пока не выполнится условие кучи.
- храним значения в списке.
- Доступ к детям вершины по формуле `left = 2 * i + 1` и `right = 2 * i + 2`
- Доступ к родителю `parent = (i - 1) // 2`

Реализация Кучи:
```python
class Heap:
    def __init__(self):
        self.data = []

    def push(self, elem):
        self.data.append(elem)
        self.siftUp(len(self.data) - 1)

    def pop(self):
        self.data[0], self.data[len(self.data) - 1] = self.data[len(self.data) - 1], self.data[0]
        elem = self.data.pop()
        self.siftDown(0)
        return elem

    def siftUp(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.data[i] < self.data[parent]:
            self.data[i], self.data[parent] = self.data[parent], self.data[i]
            i = parent
            parent = (i - 1) // 2

    def siftDown(self, i):
        n = len(self.data)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == i:
                break
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest
```

- в этой куче будут храниться кортежи (`Время начала`, `Номер Потока`)
- Изначально время начала будет `0`
- Проходим по списку задач (их время выполнения)
- извлекаем поток с наименьшим временем, выводим его - в это время он начал новую задачу
- Добавляем этот поток обратно в кучу, увеличивая его значение времени на время выполнения.

Таким образом мин куча помогает распределять потоки по минимальному времени освобождения задачи.

main
```python
with open("input.txt") as f:
    n, m = map(int, f.readline().split())
    tasks = list(map(int, f.readline().split()))

heap = Heap()
for i in range(n):
    heap.push((0, i))

for task_time in tasks:
    ready_time, thread_index = heap.pop()
    print(f"{thread_index} {ready_time}")
    heap.push((ready_time + task_time, thread_index))
```

время выполнения будет
- `O(log n)` - каждая операция (`siftUp`, `siftDown`)
- `m` - количество потоков
- Всего - `O(m log n)`