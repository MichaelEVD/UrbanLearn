from unittest import TestCase
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    def setUp(self):
        self.runner_1 = Runner('Усейн',10)
        self.runner_2 = Runner('Андрей',9)
        self.runner_3 = Runner('Ник',3)

    @classmethod
    def tearDownClass(cls):
        for i, j in cls.all_results.items():
            print(f'Результат теста {i}:')
            for key, value in j.items():
                print(f'{key}: {value.name}')

    def test_comptn_1(self, num = 1):
        comptn1 = Tournament(90,self.runner_1,self.runner_3)
        all_results = comptn1.start()
        self.assertTrue(all_results[2], self.runner_3.name)
        self.all_results[num] = all_results

    def test_comptn_2(self, num = 2):
        comptn2 = Tournament(90, self.runner_2, self.runner_3)
        all_results = comptn2.start()
        self.assertTrue(all_results[2], self.runner_3.name)
        self.all_results[num] = all_results

    def test_comptn_3(self, num=3):
        comptn3 = Tournament(90, self.runner_1,self.runner_2, self.runner_3)
        all_results = comptn3.start()
        self.assertTrue(all_results[3], self.runner_3.name)
        self.all_results[num] = all_results


if __name__ == '__main__' :
    TestCase.main()
