import unittest
from secret_santa import secret_santa


class TestSecretSanta(unittest.TestCase):
    def test_2persons(self):
        two_persons = ['Anton', 'Berta']
        assert secret_santa(two_persons) == {'Anton': 'Berta', 'Berta': 'Anton'}

    def test_receiver_uniqueness(self):
        persons = ['Anton', 'Berta', 'Caesar', 'Dora', 'Emil', 'Friedrich', 'Gustav']
        secret_santas = secret_santa(persons)
        receiver = []
        for value in secret_santas.values():
            receiver.append(value)
        receiver.sort()
        assert persons == receiver

    def test_giver_not_equal_to_receiver(self):
        persons = ['Anton', 'Berta', 'Caesar', 'Dora', 'Emil', 'Friedrich', 'Gustav']
        secret_santas = secret_santa(persons)
        for k, v in secret_santas.items():
            assert k != v

# ToDo: How to test random function? Just run the test multiple times because of the random list?
