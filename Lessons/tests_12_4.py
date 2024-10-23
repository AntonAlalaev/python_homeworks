import unittest
import rt_with_exceptions as runner
import logging

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, "Тест в этом классе заморожен")
    def test_walk(self):
        try:
            test_obj = runner.Runner(2)
            for _ in range(10):
                test_obj.walk()
            self.assertEqual(test_obj.distance,50)
            logging.info(f" инициализация walk прошла успешно ")
        except ValueError as err:
            logging.warning("test_walk Задана отрицательная скорость", exc_info=True)
        except TypeError as err:
            logging.warning("test_walk Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "Тест в этом классе заморожен")
    def test_run(self):
        try:
            test_obj = runner.Runner("Вася", -5)
            for _ in range(10):
                test_obj.run()
            self.assertEqual(test_obj.distance, 100)
            logging.info(f" test_run прошел успешно ")
        except ValueError as err:
            logging.warning("test_run Задана отрицательная скорость", exc_info=True)
        except TypeError as err:
            logging.warning("test_run Неверный тип данных для объекта Runner", exc_info=True)


    @unittest.skipIf(is_frozen, "Тест в этом классе заморожен")
    def test_challenge(self):
        try:
            test_obj_1 = runner.Runner("1")
            test_obj_2 = runner.Runner("2")
            for _ in range(10):
                test_obj_1.walk()
                test_obj_2.run()
            self.assertNotEqual(test_obj_1.distance, test_obj_2.distance)
            logging.info(f" test_challenge прошел успешно ")
        except:
            logging.warning("Что-то пошло не так в test_challenge", exc_info=True)
