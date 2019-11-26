# -*- coding: utf-8 -*-
"""
module_title: 'Programming for Data Analytics'
module_code: 'B9DA100'
lecturer: 'Darren Redmond'
stage: 'Semester 1'
assessment_title: 'Spellchecker'
assessment_number: 'CA3'
individual_or_group: 'Individual'
issue_date: 13/11/2019
submission_date: 1/1/2019
mode_of_submission: 'Moodle/Github'
student_name: 'Sophie Reisenleitner'
student_number: 10544458
github_link: https://github.com/smileyowley/B9DA100-SR/tree/master/CA3_Spellchecker
"""

import unittest
from spellchecker import SpellChecker

# CREATING TEST SPELLCHECKER OBJECT
class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        self.spellChecker = SpellChecker()
        self.spellChecker.load_words('spell.words')

    def test_spell_checker(self):
        self.assertTrue(len(self.spellChecker.words) > 50000) #Checking the length of dictionary file
        self.assertTrue(self.spellChecker.check_word('misspell'))
        self.assertNotEqual([{'line': 1, 'pos': 13, 'word': 'the'}, {'line': 3, 'pos': 8, 'word': 'someone'}],
                self.spellChecker.check_document('spelling_bad.txt'))
        self.assertNotEqual([{'line': 3, 'pos': 1, 'word': 'whereas'}, {'line': 3, 'pos': 5, 'word': 'alright'}],
                self.spellChecker.check_document('spelling_ok.txt'))

if __name__ == '__main__':
    unittest.main()
