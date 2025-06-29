import time
import tracemalloc

def test_performance(func):
    def wrapper(*args, **kwargs):
        # Засекаем время и запускаем отслеживание памяти
        start_time = time.perf_counter()
        tracemalloc.start()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        # Получаем статистику по памяти
        memory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()

        print(f"[{func.__name__}] Время выполнения: {round(end_time - start_time, 4)} секунд")
        print(f"[{func.__name__}] Память: {round(memory / 1024, 2)} КБ")
        print("__________________________________________________________")

        return result
    return wrapper

