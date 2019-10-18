import unittest


class PractiveA(unittest.TestCase):

    def setUp(self):
        print("setup_A")

    def tearDown(self):
        print("teardown_A")

    def test_A1(self):
        print("test_A1")

    def test_A2(self):
        print("test_A2")


# class PractiveB(unittest.TestCase):
#
#     def setUp(self):
#         print("setup_B")
#
#     def tearDown(self):
#         print("teardown_B")
#
#     def test_B1(self):
#         print("test_B1")
#
#     def test_B2(self):
#         print("test_B2")


if __name__ == '__main__':
    unittest.main()
    # suit = unittest.TestSuite()
    # suit.addTest(PractiveA("test_A1"))
    # unittest.TextTestRunner().run(suit)


