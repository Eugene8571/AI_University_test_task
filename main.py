import random


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
        500
        >>> H.count_overlaps
        0
        >>> H = History()
        >>> H.history_arr
        []
        >>> H.set_history([1,2,3], 10)
        >>> H.history_arr
        [1, 2, 3]
        >>> H.score
        10
        >>> H.set_history([1,2,3], 8)
        >>> H.history_arr
        [1, 2, 3]
        >>> H.score
        8
        >>> H.count_overlaps
        1
        >>> H.set_history([3,4,5], 11)
        >>> H.history_arr
        [1, 2, 3, 3, 4, 5]
        >>> H.score
        8
        >>> H.count_overlaps
        1
        """
        # if len(sequence) != 500:
        #     return
        if self.score == '':
            self.score = score
            self.history_arr = sequence
            return

        if self.is_it_dupe_sequence(sequence):
            self.count_overlaps += 1
            if self.score > score:
                self.score = score
        else:
            self.history_arr = self.history_arr + sequence

    def is_it_dupe_sequence(self, sequence):
        """
        - проверяет, есть ли такая в истории.
        Если есть True если нет False
        >>> H = History()
        >>> H.history_arr = [1,2,3,4,5,6,7]
        >>> _sequence = [1,2,3]
        >>> H.is_it_dupe_sequence(_sequence)
        True
        >>> _sequence = [5,6,7]
        >>> H.is_it_dupe_sequence(_sequence)
        True
        """
        if not self.history_arr:
            return False

        for i in range(len(self.history_arr) - len(sequence) + 1):
            if self.history_arr[i:i+len(sequence)] == sequence:
                return True
        return False

    def save_history(self, filepath):
        """
        - записывает данные истории на диск
        """
        data = ' '.join(str(e) for e in self.history_arr)
        file = open(filepath, 'w')
        file.write(data)

    def load_history(self, filepath):
        """
        - загружает данные истории с диска
        """
        with open(filepath, 'r') as file:
            data = file.read()
        return [int(i) for i in data.split()]


def random_sequence():
    """
    функция должна генерировать случайный набор для sequence и score
    >>> _sequence = random_sequence()
    >>> len(_sequence)
    500
    >>> type(_sequence)
    <class 'list'>
    """
    sequence = []
    for i in range(500):
        x = random.randint(0, 1000)
        sequence.append(x)
    return sequence


def random_score():
    """
    >>> score = random_score()
    >>> type(score)
    <class 'float'>
    """
    return random.uniform(-10**5, 10**5)


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

    import doctest
    doctest.testmod()
