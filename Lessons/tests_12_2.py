from runner_and_tournament import *
import unittest
from pprint import *

class TournamentTest(unittest.TestCase):

    all_results = {}

    @classmethod
    def SetUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)

    # Тесты в задании Усейн и Ник
    def test_round_1(self):
        tour = Tournament(90, self.runner_1, self.runner_3)
        result = tour.start()
        self.all_results[1] = result
        # Последний должен быть Ник
        self.assertTrue(result[max(result.keys())] is self.runner_3)

    def test_round_2(self):
        tour = Tournament(90, self.runner_2, self.runner_3)
        result = tour.start()
        self.all_results[2] = result
        # Последний должен быть Ник
        self.assertTrue(result[max(result.keys())] is self.runner_3)

    def test_round_3(self):
        tour = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tour.start()
        self.all_results[3] = result
        # Последний должен быть Ник
        self.assertTrue(result[max(result.keys())] is self.runner_3)

    # Анализ на логическую ошибку:
    # Если дистанция меньше чем удвоенная скорость (в данном тесте - 5, если ее поменять на 20 все будет ок)
    # участника с минимальной скоростью, то финишируют они
    # в том порядке, в котором были перечислены в конструкторе класса Tournament
    # т.к. после первой итерации они уже пройдут всю дистанцию и самый первый участник в конструкторе    #
    # окажется первым. Если больше чем удвоенная скорость самого медленного
    # но меньше чем удвоенная скорость самого быстрого и если быстрый в вызове последний
    # то тот, кто со средней скоростью раньше финиширует и тоже выйдет на первое место
    #
    def test_logik(self):
        tour = Tournament(5, self.runner_3, self.runner_2, self.runner_1)
        result = tour.start()
        self.all_results[4] = result
        # Последний должен быть Ник, но ник будет первым и вызовет ошибку - тест не пройдет
        self.assertTrue(result[max(result.keys())] is self.runner_3)

    # Как исправить этот баг?
    # Перед стартом циклом while необходимо отсортировать self.participants
    # по убыванию скорости и только потом запускать цикл.


    @classmethod
    def tearDownClass(cls):
        for items in sorted(cls.all_results.keys()):
            result = ""
            for res in cls.all_results[items].keys():
                result += str(res) + " место: " + str(cls.all_results[items][res]) + " "
            print(f"Раунд {items}. Результаты: {result} ")


if __name__ == "__main__":
    unittest.main()