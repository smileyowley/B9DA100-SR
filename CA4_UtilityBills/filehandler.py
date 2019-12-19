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
student_number: 10544458
github_link: https://github.com/smileyowley/B9DA100-SR/tree/master/CA4_UtilityBillManagement
"""

import os, sys, pandas, csv

##### MAIN MENU #####
def main_menu(bills):
    print('1: View bills\n2: View reports\n3: View User Manual\n4: Exit')
    menu_choice = int(input('Please pick one of the above: '))
    if menu_choice == 1: # Viewing the bills
        bill_menu(bills)
    elif menu_choice == 2: # Viewing the reports
        report_menu(bills)
    elif menu_choice == 3: # Viewing the user manual
        view_user_manual()
    elif menu_choice == 4: # Exiting the app
        print('Goodbye and thank you for stopping by! :)')
        sys.exit(0)
    else:
        print('\n1: View bills\n2: View reports\n3: View User Manual\n4: Exit:')
        menu_choice = int(input('Please pick one of the options between 1-4: '))

##### MAIN CHOICE 1: BILLS SUBMENU #####
def bill_menu(bills):
    print('1: View all bills\n2: Modify a bill\n3: Add a new bill\n4: Delete a bill\nOther: Back to Main Menu')
    menu_choice = int(input('What would you like to do with the bill? '))
    if menu_choice == 1: # View all bills
        view_bill(bills)
    elif menu_choice == 2: # Add new bill
        add_bill()
    else:
        main_menu()

# Choice 1: View bill
def view_bill(bills):
    #pre = datetime.datetime.now() # Timing the code - before
    for line in bills:
        if len(line) > 1:
            bills.append(line.strip().split(','))
            bills[-1][-1] = bills[-1][-1].strip()
    #print(datetime.datetime.now() - pre) # Timing the code - after
    return bills

# Choice 2: Add new bill
def add_bill(bills):
    print('Add a new bill')

##### MAIN CHOICE 2: REPORTS SUBMENU #####
def report_menu(bills):
    print('\n\nREPORTS MENU\n1: Show most popular company\n2: Show total bills/company\n3: Show most recent bill first\n4: Show highest Debit and Credit amount\n5: Search for average bill amount for a time frame (month/year)\n6: Searche for average time between bills\nOther: Back to Main Menu')
    menu_choice = int(input('Which report would you like to see? '))
    if menu_choice == 1: # Show most popular company based on number of bills
        print('company_highest')
    elif menu_choice == 2: # List the total number of bills per company
        print('company_bills')
    elif menu_choice == 3: # List bills by in descending order (date)
        print('bill_sort_latest')
    elif menu_choice == 4: # Show highest debit and credit amount on bills
        print('bill_highest')
    elif menu_choice == 5: # User searches for the average amount on bills between a certain period of time (month/year) 
       print('amount_average')
    elif menu_choice == 6: # User searches for the average time between 2 bills
       print('time_bw_bills')
    else:
        main_menu(bills)
    
##### MAIN CHOICE 3: VIEW USER MANUAL #####
def view_user_manual():
    os.system('start UserManual.pdf')
    main_menu()

##### MAIN FUNCTION #####
def main():
    path = 'C:/1_DBS/1_Programming/B9DA100-SR/CA4_UtilityBills'
    bills = open('bills.csv')
    print('*****************************************\n* Welcome to the Utility Bill Manager        *\n*****************************************')
    main_menu(bills)
    #process_choice()
    #process_bills(bilexits)

if __name__ == '__main__': #Only run code if mentioned in main
    main()