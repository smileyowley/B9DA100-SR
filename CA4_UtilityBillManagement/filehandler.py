# -*- coding: utf-8 -*-

"""
module_title: 'Programming for Data Analytics'
module_code: 'B9DA100'
lecturer: 'Darren Redmond'
stage: 'Semester 1'
assessment_title: ''
assessment_number: 'CA4'
individual_or_group: 'Individual'
issue_date: 27/11/2019
submission_date: 22/12/2019
mode_of_submission: 'Moodle/Github'
student_name: 'Sophie Reisenleitner'
student_number: 10544458
github_link: 
"""

print("**********************************************")
print("* Welcome to the Utility Bill Manager        *")
print("**********************************************")
print("")

def read_bills():
    bills = []
    bills_file = open('results.csv')
    for line in bills_file:
        if len(line) > 1: #optional
            bills.append(line.strip().splot(', '))
            bills[-1][-1] = bills[-1][-1].strip()
    #pass
    return bills


my_path = input("Please set your working directory here: ")

# CREATING SPELLCHECKER OBJECT
class FileHandler(object):
    def __init__(self):
        self.words = []

    def load_file(self, file_name):
        my_file = open(file_name)
        reading_lines = my_file.readlines()
        my_file.close()
        return list(map(lambda x: x.strip().lower(), reading_lines))

    def load_words(self, file_name):
        self.words = self.load_file(file_name)

    def check_document(self, file_name):
        self.sentences = self.load_file(file_name)
        failed_words_in_sentences = []
        index = 0
        for index, sentence in enumerate(self.sentences):
            failed_words_in_sentences.extend(self.check_words(sentence, index))
            index = index + 1
        if not failed_words_in_sentences: # If there are no errors, print confirmation
            print(file_name + " has no spelling errors.")
        else: # If there are errors, print each word
            return failed_words_in_sentences
        

    def check_word(self, word):
        return word.strip('.').lower() in self.words

    def check_words(self, sentence, index=0):
        words_to_check = sentence.split(' ')
        caret_position = 0
        failed_words = [] 
        for word in words_to_check:
            if not self.check_word(word):
                print('Line ' + str(index+1) + ', position ' + str(caret_position+1) + ': "' + word.strip(".!,:-_/()") + '" is misspelt.')
                failed_words.append({'word':word,'line':index+1,'pos':caret_position+1})
            # updating the caret position to be the length of the word plus 1 for the split character.
            caret_position = caret_position + len(word) + 1
        return failed_words


# CREATING AN INSTANCE OF THE SPELLCHECKER OBJECT
if __name__ == '__main__':
    spellChecker = SpellChecker()
    spellChecker.load_words('spell.words')
    print("Spellchecker's dictionary has " + str(len(spellChecker.words)) + " words.")

# CHECKING THE WORDS IN ALL FILES WITHIN THE DIRECTORY
    os.chdir(my_path)
    files = glob.glob('*.txt')
    for file in files:
        print("")
        print("Checking " + file)
        spellChecker.check_document(file)
