import unittest
from auto_test.practive1 import PractiveA


class PractiveB(unittest.TestCase):

    def setUp(self):
        print("setup_B")

    def tearDown(self):
        print("teardown_B")

    def test_B1(self):
        print("test_B1")

    def test_B2(self):
        print("test_B2")


if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTests([PractiveA("test_A1"), PractiveB("test_B1")])
    unittest.TextTestRunner().run(suit)
