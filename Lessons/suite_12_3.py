import unittest
import tests_12_3

runner_tests = unittest.TestSuite()

runner_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runner_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

test_run = unittest.TextTestRunner(verbosity=2)
test_run.run(runner_tests)