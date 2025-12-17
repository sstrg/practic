массив = [None] * 6
размер = 0


def insert(индекс, значение):
    global размер

    if размер >= len(массив):
        print("Ошибка: массив полон!")
        return False

    if индекс < 0 or индекс > размер:
        print(f"Ошибка: индекс {индекс} вне диапазона")
        return False

    for i in range(размер, индекс, -1):
        массив[i] = массив[i - 1]

    массив[индекс] = значение
    размер += 1
    return True


# Тест
insert(0, 100)
insert(1, 300)
insert(1, 200)
insert(0, 50)
insert(2, 150)
insert(5, 400)

print(f"Массив: {массив}")
print(f"Факт. размер: {размер}")
