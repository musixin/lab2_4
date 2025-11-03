# Функция для определения n чисел Фибоначчи
# Принимает n
# Возвращает список чисел Фибоначчи длинны n
# Пример: 10 -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
def fib(n: int) -> list[int]:
    if n <= 0:
        return []
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]


# Функция сортировки пузырьком
# Принимает список неупорядоченных элементов
# Возвращает упорядоченный по неубыванию список
# Пример: [9, 8, 7, 6, 6, 4, 1] -> [1, 4, 6, 6, 7, 8, 9]
def bubble_sort(numbers: list[int]) -> list[int]:
    arr = numbers.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Функция поиска простых чисел методом Решето Эратосфена
# Принимает n
# Возвращает список простых чисел < n
# Пример: 11 -> [2, 3, 5, 7]
def find_primes(n):
    pre_primes = []
    for i in range(n):
        pre_primes.append(i)
    pre_primes[1] = 0
    for i in range(2, n):
        if pre_primes[i]:
            for j in range(2*i, n, i):
                pre_primes[j] = 0
    primes = []
    for number in pre_primes:
        if number:
            primes.append(number)
    return primes

