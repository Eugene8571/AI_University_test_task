import random
import csv
import os
import time
import sys


class History:
    def __init__(self):
        self.history_arr = []
        self.score = ''
        self.count_overlaps = 0

    def set_history(self, sequence, score):
        """
        - проверяет имеющийся массив history_arr на наличие в нем
        дубликата sequence
        - если дубликат найден - проверяет score, и записывает score только
        если оно меньше уже находящегося в данных
        - если дубликат не найден записывает входные данные
        - и ведет счетчик дубликатов
        >>> H = History()
        >>> _sequence = random_sequence()
        >>> _score = random_score()
        >>> H.set_history(_sequence, _score)
        >>> len(H.history_arr)
        1
        >>> H.count_overlaps
        0
        >>> H = History()
        >>> H.history_arr
        []
        >>> H.set_history([1,2,3], 10)
        >>> H.history_arr
        [[1, 2, 3]]
        >>> H.score
        10
        >>> H.set_history([1,2,3], 8)
        >>> H.history_arr
        [[1, 2, 3]]
        >>> H.score
        8
        >>> H.count_overlaps
        1
        >>> H.set_history([3,4,5], 11)
        >>> H.history_arr
        [[1, 2, 3], [3, 4, 5]]
        >>> H.score
        8
        >>> H.count_overlaps
        1
        """
        if self.score == '':
            self.score = score
            self.history_arr = [sequence]
            return

        if self.is_it_dupe_sequence(sequence):
            self.count_overlaps += 1
            if self.score > score:
                self.score = score
        else:
            self.history_arr.append(sequence)

    def is_it_dupe_sequence(self, sequence):
        """
        - проверяет, есть ли такая в истории.
        Если есть True если нет False
        >>> H = History()
        >>> H.history_arr = [[1,2,3], [2,3,4]]
        >>> _sequence = [1,2,3]
        >>> H.is_it_dupe_sequence(_sequence)
        True
        >>> _sequence = [5,6,7]
        >>> H.is_it_dupe_sequence(_sequence)
        False
        """
        if not self.history_arr:
            return False

        if sequence in self.history_arr:
            return True

        return False

    def save_history(self, filepath):
        """
        - записывает данные истории на диск
        """
        if not os.path.exists(os.path.dirname(filepath)):
            os.makedirs(os.path.dirname(filepath))
        with open(filepath, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(self.history_arr)

    def load_history(self, filepath):
        """
        - загружает данные истории с диска
        """
        with open(filepath, 'r', newline='') as file:
            reader = csv.reader(file)
            self.history_arr = list(reader)


def random_sequence():
    """
    генерировать случайный набор для sequence
    >>> _sequence = random_sequence()
    >>> len(_sequence)
    500
    """
    sequence = []
    for i in range(500):
        x = random.randint(0, 1000)
        sequence.append(x)
    return sequence


def random_score():
    """
    генерировать случайный набор для sequence
    """
    return random.uniform(-10 ** 5, 10 ** 5)


def test_func(h, limit) -> object:
    t1 = time.time()

    while sys.getsizeof(h.history_arr) < 3 * 10 ** 3:
        if time.time() - t1 >= 10:
            print('time limit')
            break
        sequence = random_sequence()
        score = random_score()
        h.set_history(sequence, score)
    h.history_arr = h.history_arr[:-1]
    print('Время выполнения ', time.time() - t1)
    print('Кол-во дубликатов', h.count_overlaps)


if __name__ == "__main__":
    """
    - функция должна генерировать случайный набор для sequence и score
    - подавать этот набор на вход метода set_history
    - кол_во данных в history_arr должно быть не более 3gb
    - при достижении порога, должна вывести максимально точное время на
    работу функции и кол-во дубликатов найденных в истории
    - после этого данные истории должны записаться на диск и загрузиться
    - после загрузки, истории, порог увеличивается до 5gb и генерация
    продолжается
    - при достижении порога, должна вывести максимально точное время на
    работу функции, с момента загрузки, и кол-во дубликатов найденных в
    истории
    - Прислать код модуля, и jupyter notebook где этот модуль бы подгружался и
    и демонстрировалась работа тестовой функции
    
    Разрешается использование любых модулей
    """

    print('Test 1')

    filepath = 'save/h1.csv'
    h = History()
    test_func(h, 3000)
    h.save_history(filepath)

    print('Test 2')

    h.load_history(filepath)
    test_func(h, 5000)

    import doctest
    doctest.testmod()
