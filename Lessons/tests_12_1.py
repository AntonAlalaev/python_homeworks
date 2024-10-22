import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_obj = runner.Runner("test_obj")
        for _ in range(10):
            test_obj.walk()
        self.assertEqual(test_obj.distance,50)

    def test_run(self):
        test_obj = runner.Runner("test_obj")
        for _ in range(10):
            test_obj.run()
        self.assertEqual(test_obj.distance, 100)

    def test_challenge(self):
        test_obj_1 = runner.Runner("1")
        test_obj_2 = runner.Runner("2")
        for _ in range(10):
            test_obj_1.walk()
            test_obj_2.run()
        self.assertNotEqual(test_obj_1.distance, test_obj_2.distance)
