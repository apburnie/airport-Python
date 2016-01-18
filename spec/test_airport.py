import unittest

import sys
sys.path.append('../lib')

from airport import Airport

class AirportTestCase(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.plane = 1

    def test_planes_default_empty(self):
        self.assertEqual(self.airport.planes,[])

    def test_planes_can_be_overriden(self):
        self.airport = Airport(20, [self.plane])
        self.assertEqual(self.airport.planes,[self.plane])

    def test_capacity_default(self):
        self.assertEqual(self.airport.capacity, self.airport._DEFAULTCAPACITY)

    def test_capacity_can_be_overriden(self):
        self.random_capacity = 100
        self.airport = Airport(self.random_capacity)
        self.assertEqual(self.airport.capacity, self.random_capacity)

    def test_is_full_returns_true_when_airport_full(self):
        pass


if __name__ == '__main__':
  # suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
  # unittest.TextTestRunner(verbosity=2).run(suite)
  unittest.main()
