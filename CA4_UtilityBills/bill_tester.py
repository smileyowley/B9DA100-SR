# -*- coding: utf-8 -*-
import unittest
import pandas as pd

from bill_manager import view_bills

bills = view_bills("bills.csv")
bills_df = pd.read_csv(bills)
bills_df.columns = ['company', 'customer', 'year', 'month', 'day', 'amount_eur', 'credit_debit']

class TestFileHandler(unittest.TestCase):
        
    def test_view_bill(self):
        self.assertTrue(len(bills) >= 9)
        self.assertTrue('Electric Ireland', bills[0][0])

    def test_add_bill(self):
        self.assertTrue(bills_df["month"].any() <= 12)
        self.assertTrue(bills_df["day"].any() <= 31)

if __name__ == '__main__': #Only run code if mentioned in main
    unittest.main()