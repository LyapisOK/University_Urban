import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test = runner.Runner("Sasha")
        for i in range(10):
            test.walk()
        self.assertEqual(test.distance, 50)

    def test_run(self):
        test = runner.Runner("Misha")
        for i in range(10):
            test.run()
        self.assertEqual(test.distance, 100)

    def test_challenge(self):
        object_1 = runner.Runner("Petr")
        object_2 = runner.Runner("Kolya")
        for i in range(10):
            object_1.run()
            object_2.walk()
        self.assertNotEqual(object_1.distance, object_2.distance)

if __name__ == '__main__':
    unittest.main()
