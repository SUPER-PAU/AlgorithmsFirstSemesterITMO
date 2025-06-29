# Лабораторная 7 - ДП
## Задача 6 - Наибольшая возрастающая подпоследовательность

Необходимо найти НВП в последовательности

чтобы это сделать эффективно O(n log n) воспользуемся следующим алгоритмом:
- заводим 3 списка
  - `tail` - он хранит возможные значения концов нвп длины `i + 1 `
  - `tail_idx` - хранит индекс значений `tail` в исходной последовательности
  - `prev` - хранит индекс предыдущего элемента в нвп, для восстановления ответа.
- затем находим для каждого элемента место, куда его можно вставить в последовательности `tail` - `pos` 
  - если это - конец, то это значение становится новым максимумом длины.
  - если нет, то вставляем элемент `a[i]` в это самое место `pos`, заменяя тем самым больший элемент.
  - также обновляем предыдущий элемент для текущего `prev[i] = tail_idx[pos - 1]`, если он не начальный.
- Затем циклом восстанавливаем ответ, начиная с конца `tail_idx` и идя по индексам предыдущих элементов в `prev`.

алгоритм:
```python
def nvp(arr):
    n = len(arr)
    tail = []
    tail_idx = []
    prev = [-1] * n

    for i in range(n):
        num = arr[i]
        pos = bisect_left(tail, num)
        if pos == len(tail):
            tail.append(num)
            tail_idx.append(i)
        else:
            tail[pos] = num
            tail_idx[pos] = i
        if pos > 0:
            prev[i] = tail_idx[pos - 1]
            
    res = []
    k = tail_idx[-1]
    while k != -1:
        res.append(arr[k])
        k = prev[k]
    res.reverse()
    return len(res), res
```


## Задача 7 - шаблоны
Необходимо сравнить шаблон, состоящий из символов `?` - случайный символ и `*` - случайная подстрока любой длины (даже 0)
со второй строкой. Если шаблон может быть строкой, то вывести Да, если нет, то Нет.

- создаем таблицу `dp = [[False] * (m + 1) for _ in range(n + 1)]`, 
  - где `i` - идет по символам шаблона
  - `j` по символам строки
  - `dp[i][j] = True` означает, что первые `i` символов шаблона равны первым `j` символам строки
  - `dp[0][0]` делаем `True` так как пустой шаблон соответствует пустой строке.
- если шаблон состоит только из `*` то заполняем `dp[0-n][0] = True` т.к. такой шаблон может быть любой строкой.
```python
for i in range(1, n + 1):
    if template[i - 1] == '*':
        dp[i][0] = dp[i - 1][0]
    else:
        break
```
- заполняем таблицу `dp` проходясь по ней
```python
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if template[i - 1] == '*':
            dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        elif template[i - 1] == '?' or template[i - 1] == string[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
```

- если `i - 1` элемент шаблона равен `?` или элементы `template[i - 1] == string[j - 1]` то
  - записываем предыдущий результат в таблицу `dp[i][j] = dp[i - 1][j - 1]`. 
  - так она продолжится с `True` по диагонали.
- если `i - 1` элемент шаблона равен `*`
  - текущий элемент `[i][j]` будет равен элементу `[i-1][j]`, если он `True` - строка может быть пустой
  - либо элемент `[i][j]` будет равен `dp[i][j - 1]`, если он `True` - строка может быть любой длины.
- если на каком либо из этапов прохода по `i` оба условных операторов не выполнились, то остальная таблица будет состоять из `false` - условие не выполнилось
- если все норм, то в конце `dp[n][m]` будет стоять `True`

```python
def matches(template, string):
    n, m = len(template), len(string)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        if template[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
        else:
            break
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if template[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif template[i - 1] == '?' or template[i - 1] == string[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[n][m]

def main():
    with open("input.txt") as f:
        template = f.readline().strip()
        string = f.readline().strip()

    if matches(template, string):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
```

пример 
```python
template = "k?t*n"
string = "kitten"
```

тогда таблица `dp`:
```cmd
[True, False, False, False, False, False, False]
[False, True, False, False, False, False, False]
[False, False, True, False, False, False, False]
[False, False, False, True, False, False, False]
[False, False, False, True, True, True, True]
[False, False, False, False, False, False, True]
```
