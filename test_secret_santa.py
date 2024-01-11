import unittest
import pytest
from secret_santa import secret_santa
# pytest -m secret_santa -v --cov=secret_santa --cov-report=term-missing --cov-branch


class TestSecretSanta(unittest.TestCase):
    @pytest.mark.secret_santa
    def test_2persons(self):
        two_persons = ['Anton', 'Berta']
        assert secret_santa(two_persons) == {'Anton': 'Berta', 'Berta': 'Anton'}

    # test fails sometimes, at receiver = random.choice(temp_players): list index out of range
    @pytest.mark.secret_santa
    def test_receiver_uniqueness(self):
        persons = ['Anton', 'Berta', 'Caesar', 'Dora', 'Emil', 'Friedrich', 'Gustav']
        secret_santas = secret_santa(persons)
        receiver = []
        for value in secret_santas.values():
            receiver.append(value)
        receiver.sort()
        assert persons == receiver

    @pytest.mark.secret_santa
    def test_giver_not_equal_to_receiver(self):
        persons = ['Anton', 'Berta', 'Caesar', 'Dora', 'Emil', 'Friedrich', 'Gustav']
        secret_santas = secret_santa(persons)
        for k, v in secret_santas.items():
            assert k != v

    def test_2remaining_in_hat_and_last_person_to_draw_as_well(self):
        persons = ['Anton', 'Berta', 'Caesar']
        secret_santas = secret_santa(persons)

# ToDo: How to test random function? Just run the test multiple times because of the random list?
#       I need to come up with a way to run test: test_2remaining_in_hat_and_last_person_to_draw_as_well
