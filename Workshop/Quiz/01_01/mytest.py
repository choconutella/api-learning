import unittest
import myfunction


class TestFunction(unittest.TestCase):
  
  def test_data1(self):
    self.assertEqual(myfunction.result_reader('SGU'),('Berat Jenis','1.020'))
  
  def test_data2(self):
    self.assertEqual(myfunction.result_reader('CREA'),('Kreatinin','1.1'))
  
  def test_data3(self):
    self.assertEqual(myfunction.result_reader('UA'),('Asam Urat','5.3'))
  
  def test_data4(self):
    self.assertEqual(myfunction.result_reader('RBC'),('Eritrosit','5.28'))
  
  def test_data5(self):
    self.assertEqual(myfunction.result_reader('MCV'),('MCV','83.7'))
  
  def test_data6(self):
    self.assertEqual(myfunction.result_reader('RDW'),('RDW','12.8'))
  
  def test_data7(self):
    self.assertEqual(myfunction.result_reader('ERYU'),('Eritrosit','Negatif'))


if __name__ == '__main__':
  unittest.main()