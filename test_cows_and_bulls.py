import unittest
from guess import success

#IMPORTANT:
#All test functions must start with test_
#unittest Assertion Methods: https://docs.python.org/3/library/unittest.html#assert-methods


class TestGuess(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #Use setUpClass to run code at the beginning of the test Suite
        pass
  
    @classmethod
    def tearDownClass(cls):
        #Use tearDownClass to run code at the end of the test Suite
        pass

    def setUp(self):
        #Use setUp function to run code before each test case
        pass
  
    def tearDown(self):
        #Use setUp function to run code after each test case
        pass

    def test_one(self):
        result = success(2, 2)
        self.assertEqual(result, True, 'Result should be True for 2 as guess and 2 as bingo')

    def test_two(self):
        result = success(2, 3)
        self.assertEqual(result, False, 'Result should be False for 2 as guess and 3 as bingo')

#With the below function we can run the tests with 'python test_cows_and_bulls.py'
#Without this function we would have to do 'python -m unittest test_cows_and_bulls.py'
if __name__ == '__main__':
    unittest.main()