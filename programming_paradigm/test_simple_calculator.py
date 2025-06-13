import unittest
from simple_calculator import SimpleCalculator


class TestAll (unittest.TestCase):

    def setUp(self):                        #setUp() is a special method in unittest that runs before each test. Here, it creates an instance of your calculator.
        self.calc = SimpleCalculator()    #it makes sure we can acess the methods in the imported class by using self.calc and adding it to add,subtract etc

    def test_addition (self):
        self.assertEqual(self.calc.add(5, 3), 8)
        #result = self.calc.add(5, 3) instead of creating a variable seperately... we then join it all
        #self.assertEqual(result, 8)

    def test_subtraction (self):
        self.assertEqual(self.calc.subtract(7, 2), 5)

    def test_multiplication (self):
        self.assertEqual(self.calc.multiply(1, 10), 10)

    def test_division (self):
        self.assertEqual(self.calc.divide(28, 4), 7)

if __name__ == "__main__":
    unittest.main()

    

