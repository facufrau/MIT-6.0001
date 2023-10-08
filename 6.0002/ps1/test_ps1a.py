import unittest
import ps1a

class TestProblemSet1A(unittest.TestCase):
    """
    Test Problem Set 1 A solutions
    """
    def test_greedy(self):
        cows ={'Jesse': 6, 'Maybel': 3, 'Callie': 2, 'Maggie': 5}
        limit = 10
        trips_calculated = ps1a.greedy_cow_transport(cows, limit)
        trips = [['Jesse', 'Maybel'], ['Maggie', 'Callie']]
        self.assertEqual(trips, trips_calculated)

    def test_greedy_other(self):
        cows ={'Lilo': 9, 'Jesse': 6, 'Maybel': 3, 'Callie': 2, 'Maggie': 5}
        limit = 10
        trips_calculated = ps1a.greedy_cow_transport(cows, limit)
        trips = [['Lilo'], ['Jesse', 'Maybel'], ['Maggie', 'Callie']]
        self.assertEqual(trips, trips_calculated)

if __name__ == '__main__':
    unittest.main()