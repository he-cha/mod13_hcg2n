import unittest
from datetime import datetime
from MainProgram import get_chart_type, get_symbol, get_time, get_end_date, get_start_date

class TestStockVisualizer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
    @classmethod
    def tearDownClass(cls):
        print('teadownClass')
    
    def setUp(self):
        self.sym_1 = "GOOGL"
        self.sym_2 = "IN_"
        self.chart_type1 = "1"
        self.chart_type2 = "9"
        self.time_series1 = "1"
        self.time_series2 = "8"
        self.start_date1 = "2024-01-01"
        self.start_date2 = "22-22-22"
        self.end_date1 = "2024-03-01"
        self.end_date2 = "20-10-10"
    
    def tearDown(self):
        print('tearDown\n')
   
    def test_symbol(self):
        print('test_symbol')
        self.assertTrue(get_symbol(self.sym_1))
        self.assertFalse(get_symbol(self.sym_2))
    
    def test_chart_type(self):
        print('test_chart_type')
        self.assertTrue(get_chart_type(self.chart_type1))
        self.assertFalse(get_chart_type(self.chart_type2))
    
    def test_time_series(self):
        print('test time series')
        self.assertTrue(get_time(self.time_series1))
        self.assertFalse(get_time(self.time_series2))
    
    def test_start_date(self):
        print('test_start_date')
        self.assertTrue(get_start_date(self.start_date1))
        self.assertFalse(get_start_date(self.start_date2))

    
    def test_end_date(self):
        print('test_end_date')
        self.assertTrue(get_end_date(self.end_date1))
        self.assertFalse(get_start_date(self.end_date2))

if __name__ == "__main__":
    unittest.main()