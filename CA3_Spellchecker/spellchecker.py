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

class SpellChecker(object):
    def __init__(self):
        self.words = []

    def load_file(self, file_name):
        my_file = open(file_name)
        lines = my_file.readlines()
        my_file.close()
        return list(map(lambda x: x.strip().lower(), lines))

    def load_words(self, file_name):
        self.words = self.load_file(file_name)

    def check_document(self, file_name):
        self.sentences = self.load_file(file_name)
        failed_words_in_sentences = []
        index = 0
        for index, sentence in enumerate(self.sentences):
            failed_words_in_sentences.extend(self.check_words(sentence, index))
            index = index + 1
        return failed_words_in_sentences

    def check_word(self, word):
        return word.strip('.').lower() in self.words

    def check_words(self, sentence, index=0):
        words_to_check = sentence.split(' ')
        caret_position = 0
        failed_words = []
        for word in words_to_check:
            if not self.check_word(word):
                print('Word is misspelt ' + word + ' at line : ' + str(index+1) + ' pos ' + str(caret_position+1))
                failed_words.append({'word':word,'line':index+1,'pos':caret_position+1})
            # update the caret position to be the length of the word plus 1 for the split character.
            caret_position = caret_position + len(word) + 1
        return failed_words

if __name__ == '__main__':
    spellChecker = SpellChecker()
    spellChecker.load_words('spell.words')
    print(len(spellChecker.words))
    # now check if the word zygotic is a word
    print(spellChecker.check_word('zygotic'))
    print(spellChecker.check_word('zogotic'))
    print(spellChecker.check_words('zygotic mistasdas elementary'))
    print(spellChecker.check_document('darren.txt'))

    import os
    import glob
    os.chdir('R:/')
    files = glob.glob('*.txt')
    for file in files:
        print(file)
        spellChecker.check_document(file)
        