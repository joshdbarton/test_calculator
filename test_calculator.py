import unittest
from calculator import Calculator

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    self.calc = Calculator()

  @classmethod
  def tearDownClass(self):
    print('Tear down class')

  def test_add(self):
    self.assertEqual(self.calc.add(2, 7), 9)

  def test_subtract(self):
    self.assertEqual(self.calc.subtract(4, 3), 1)
  
  def test_multiply(self):
    self.assertEqual(self.calc.mult(3, 4), 12)

  def test_divide(self):
    self.assertEqual(self.calc.divide(12, 3), 4)

if __name__ == '__main__':
    unittest.main()