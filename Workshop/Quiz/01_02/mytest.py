import unittest
import myfunction


class TestFunction(unittest.TestCase):
  
  def test_data1(self):
    self.assertEqual(myfunction.converter(100,'USD','USD'), 100)
  
  def test_data2(self):
    self.assertEqual(myfunction.converter(1.5,'usd','USD'), 1.5)
  
  def test_data3(self):
    self.assertEqual(myfunction.converter(2, 'usd', 'usd'), 2)
  


if __name__ == '__main__':
  unittest.main()