import unittest
import runner
from runner_and_tournament import *

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, "Тест в этом классе заморожен")
    def test_walk(self):
        test_obj = runner.Runner("test_obj")
        for _ in range(10):
            test_obj.walk()
        self.assertEqual(test_obj.distance,50)

    @unittest.skipIf(is_frozen, "Тест в этом классе заморожен")
    def test_run(self):
        test_obj = runner.Runner("test_obj")
        for _ in range(10):
            test_obj.run()
        self.assertEqual(test_obj.distance, 100)

    @unittest.skipIf(is_frozen, "Тест в этом классе заморожен")
    def test_challenge(self):
        test_obj_1 = runner.Runner("1")
        test_obj_2 = runner.Runner("2")
        for _ in range(10):
            test_obj_1.walk()
            test_obj_2.run()
        self.assertNotEqual(test_obj_1.distance, test_obj_2.distance)




class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = {}

    @classmethod
    def SetUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)

    # Тесты в задании Усейн и Ник
    @unittest.skipIf(is_frozen, "Тест в этом классе заморожен")
    def test_round_1(self):
        tour = Tournament(90, self.runner_1, self.runner_3)
        result = tour.start()
        self.all_results[1] = result
        # Последний должен быть Ник
        self.assertTrue(result[max(result.keys())] is self.runner_3)

    @unittest.skipIf(is_frozen, "Тест в этом классе заморожен")
    def test_round_2(self):
        tour = Tournament(90, self.runner_2, self.runner_3)
        result = tour.start()
        self.all_results[2] = result
        # Последний должен быть Ник
        self.assertTrue(result[max(result.keys())] is self.runner_3)

    @unittest.skipIf(is_frozen, "Тест в этом классе заморожен")
    def test_round_3(self):
        tour = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tour.start()
        self.all_results[3] = result
        # Последний должен быть Ник
        self.assertTrue(result[max(result.keys())] is self.runner_3)

    @unittest.skipIf(is_frozen, "Тест в этом классе заморожен")
    def test_logik(self):
        tour = Tournament(50, self.runner_3, self.runner_2, self.runner_1)
        result = tour.start()
        self.all_results[4] = result
        # Последний должен быть Ник, но ник будет первым и вызовет ошибку - тест не пройдет
        self.assertTrue(result[max(result.keys())] is self.runner_3)

    @classmethod
    def tearDownClass(cls):
        for items in sorted(cls.all_results.keys()):
            result = ""
            for res in cls.all_results[items].keys():
                result += str(res) + " место: " + str(cls.all_results[items][res]) + " "
            print(f"Раунд {items}. Результаты: {result} ")


if __name__ == "__main__":
    unittest.main()
