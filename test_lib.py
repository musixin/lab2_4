import unittest
from lib import fib, bubble_sort, find_primes


class TestAlgorithms(unittest.TestCase):

    # диапазон корректных значений фукнции n >= 1
    # классы эквивалентности:
    # корректный - n > 0
    # граничный - n = 1/2
    # нулевой - n = 0
    # отрицательный - n < 0
    # некорректный - n не целое число
    # граничные значения 0, 1, 2
    def test_fibonacci(self):
        self.assertEqual(fib(5), [0, 1, 1, 2, 3])
        self.assertEqual(fib(1), [0])
        self.assertEqual(fib(2), [0, 1])
        self.assertEqual(fib(0), [])
        self.assertEqual(fib(-3), [])
        with self.assertRaises(TypeError):
            fib("2")

    # диапазон корректных значений фукнции len([числа]) >= 0
    # граничные значения: [], [x], [x,y]
    # классы эквивалентности:
    # корректный - список из нескольких чисел
    # граничный, корректный - пустой список
    # граничный, корректный - список из одного элемента
    # список уже отсортирован
    # список с наличием одинаковых элементов
    # некорректный - передается не список
    # некорректный - список с некорректными типами
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([5]), [5])
        self.assertEqual(bubble_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(bubble_sort([3, 3, 1]), [1, 3, 3])
        with self.assertRaises(AttributeError):
            bubble_sort("2,3,4")
        with self.assertRaises(TypeError):
            bubble_sort([2.2, "string", 3.1, "", 5.0])



    # граничные значения: n = 1, n = 2, n = 3
    # классы эквивалентности:
    # корректный - n >= 2
    # граничный, корректный - n = 2
    # меньше минимального - n < 2
    # некорректный тип n - не целое число
    def test_find_primes(self):
        self.assertEqual(find_primes(10), [2, 3, 5, 7])
        self.assertEqual(find_primes(3), [2])
        self.assertEqual(find_primes(2), [])
        self.assertEqual(find_primes(1), [])
        self.assertEqual(find_primes(0), [])
        self.assertEqual(find_primes(-10), [])
        with self.assertRaises(TypeError):
            find_primes(6.5)


if __name__ == '__main__':
    unittest.main()
