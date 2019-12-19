# -*- coding: utf-8 -*-
"""
module_title: 'Programming for Data Analytics'
module_code: 'B9DA100'
lecturer: 'Darren Redmond'
stage: 'Semester 1'
assessment_title: 'Utility Bill Management'
assessment_number: 'CA4'
individual_or_group: 'Individual'
issue_date: 27/11/2019
submission_date: 22/12/2019
mode_of_submission: 'Moodle/Github'
student_name: 'Sophie Reisenleitner'
student_number: 10544458
"""

import unittest
from filehandler import read_bills

# Red/Green/Refactor
class TestFileHandler(unittest.TestCase):

    def test_file_handler(self):
        bills = read_bills()
        self.assertEqual(20, len(bills))
        self.assertEqual('Electric Ireland', bills[0][0])
        self.assertEqual('credit', bills[19][6])

if __name__ == '__main__': #Only run code if mentioned in main
    unittest.main()
