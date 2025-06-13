import unittest
from simple_calculator import SimpleCalculator


class TestAll (unittest.TestCase):

    def setUp(self):                        #setUp() is a special method in unittest that runs before each test. Here, it creates an instance of your calculator.
        self.calc = SimpleCalculator()    #it makes sure we can acess the methods in the imported class by using self.calc and adding it to add,subtract etc

    def test_add (self):
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)

    def test_subtract (self):
        result = self.calc.subtract(7, 2)
        self.assertEqual(result, 5)

    def test_multiply (self):
        result = self.calc.multiply(1, 10)
        self.assertEqual(result, 10)

    def test_divide (self):
        result = self.calc.divide(28, 4)
        self.assertEqual(result, 7)

if __name__ == "__main__":
    unittest.main()

    

