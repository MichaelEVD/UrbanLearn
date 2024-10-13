import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        te_wa = Runner('Petya')
        for i in range(10):
            te_wa.walk()
        self.assertEqual(te_wa.distance, 50, f'Сбой матрицы!')
    def test_run(self):
        te_r = Runner('Vasya')
        for i in range(10):
            te_r.run()
        self.assertEqual(te_r.distance, 100, f'Сбой матрицы!')
    def test_challenge(self):
        t_chal1 = Runner('Denis')
        t_chal2 = Runner('Dima')
        for i in range(10):
            t_chal1.run()
            t_chal2.walk()
        self.assertNotEqual(t_chal1.distance, t_chal2.distance)

if __name__ == '__main__' :
    unittest.main()


