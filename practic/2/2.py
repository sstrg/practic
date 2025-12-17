import time

print("СРАВНЕНИЕ ВРЕМЕНИ ВСТАВКИ 100000 ЭЛЕМЕНТОВ")
print("=" * 50)


start = time.perf_counter()
static_arr = [0] * 100000

for i in range(100000):
    static_arr[i] = i
static_time = time.perf_counter() - start

start = time.perf_counter()
dynamic_arr = []

for i in range(100000):
    dynamic_arr.append(i)
dynamic_time = time.perf_counter() - start

print(f"Статический массив: {static_time:.6f} сек")
print(f"Динамический массив: {dynamic_time:.6f} сек")
print(f"Разница: {dynamic_time/static_time:.2f}x")