import random

with open("worst.txt", "w") as f:
    f.write("10000\n")
    f.write(" ".join(map(str, range(10000, 0, -1))))

with open("best.txt", "w") as f:
    f.write("10000\n")
    f.write(" ".join(map(str, range(1, 10001))))

with open("middle.txt", "w") as f:
    f.write("10000\n")
    f.write(" ".join(map(str, random.sample(range(1, 10000000), 10000))))

def generate_low_unique_array(n, unique_count=5):
    base = random.sample(range(1, 100), unique_count)
    return [random.choice(base) for _ in range(n)]

sizes = [10**3, 10**4, 10**5]
results = []

for n in sizes:
    with open(f"{n}.txt", "w") as f:
        f.write(f"{n}\n")
        f.write(" ".join(map(str, generate_low_unique_array(n))))

