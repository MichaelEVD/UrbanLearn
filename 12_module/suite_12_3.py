import unittest
from module_12_1 import RunnerTest as RT
import module_12_2

obj_TS = unittest.TestSuite()
obj_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(RT))
obj_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

if __name__ == "__main__":
    runner_TS = unittest.TextTestRunner(verbosity=2)
    runner_TS.run(obj_TS)
