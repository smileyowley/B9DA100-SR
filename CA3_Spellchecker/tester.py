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
submission_date: 24/11/2019
mode_of_submission: 'Moodle/Github'
student_name: 'Sophie Reisenleitner'
student_number: 10544458
github_link: 
"""

import unittest
from spellcheck import SpellChecker
class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        self.spellChecker = SpellChecker()
        self.spellChecker.load_words('spell.words')

    def test_spell_checker(self):
        self.assertTrue(len(self.spellChecker.words) > 50000)
        self.assertTrue(self.spellChecker.check_word('zygotic'))
        self.assertFalse(self.spellChecker.check_word('zogotic'))
        self.assertEqual([{'line': 1, 'pos': 9, 'word': 'mistasdas'}],
                self.spellChecker.check_words('zygotic mistasdas elementary'))
        self.assertEqual([],
                self.spellChecker.check_words('our first correct sentence'))
        self.assertEqual(0,
                len(self.spellChecker.check_words('Our first correct sentence.')))
        self.assertEqual([{'line': 1, 'pos': 9, 'word': 'mistasdas'}, {'line': 1, 'pos': 19, 'word': 'spelllleeeing'}],
                self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary'))
        self.assertEqual(2,
                len(self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary')))
        #self.assertEqual(0, len(self.spellChecker.check_document('spell.words')))
        self.assertEqual([{'line': 2, 'pos': 15, 'word': 'larn'}, {'line': 2, 'pos': 20, 'word': 'huw'}, {'line': 2, 'pos': 33, 'word': 'wurdz'}],
                self.spellChecker.check_document('darren.txt'))


if __name__ == '__main__':
    unittest.main()
