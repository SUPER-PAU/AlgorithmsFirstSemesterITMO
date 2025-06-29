with open("worst_case.txt", "w") as file:
    file.write(" ".join(map(str, range(10_000, 0, -1))))

# Генерация массива от 1 до 10_000 (возрастание)
with open("best_case.txt", "w") as file:
    file.write(" ".join(map(str, range(1, 10_001))))
