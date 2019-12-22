import os,time,sys,csv
import pandas as pd
import random

import re

from pathlib import Path

from tkinter import Tk
from tkinter.filedialog import askopenfilename

# =================== GLOBAL VARIABLES ========================     
bills = ""
bills_df = ""  
company_count = ""
file_n="bills.csv"

# ======================== FUNCTIONS   ======================== 
def loading(arg):
#{ 
    print(arg)
    for i in range(0, 101,random.randint(1,25)):
        time.sleep(0.1)
        sys.stdout.write(""+ "\r")

        sys.stdout.write(str(i) + "%")
        sys.stdout.flush()
        sys.stdout.write(""+ "\r")
#}  // ===== end loading function =====

def open_file():
#{ 
      global bills
      global bills_df
      global file_n 
      
      file = Path(file_n)
      
      loading("extracting csv file...")
      
      if(file.is_file()!=True):
          print("File: ",file_n," not found in current dir!\nPlease browse for csv file...")               
          browse_dir()
          
          if(file_n==""):
              print("FAILED to open...")
              print("\n\nThank you for using my program!\nSee you later...   :)\n")
              time.sleep(4.0)
              #sys.stdout.flush()
              return "",""                
      print("Successfully opened")
      bills = open(file_n)
      bills_df = pd.read_csv(bills)       
#}  // ===== end open_file function =====

def add_bill():
#{ 
    global file_n 
    with open(file_n, 'a', newline='') as file:
         writer = csv.writer(file)
         print("\n=== Add User data === ")
         company = input("company: ")
         customer = input("customer: ")
         year = input("year[YYYY]: ")
         month = input("month[MM]: ")
         day = input("day[DD]: ")
         amount = input("amount[€XX.XX]: ")
         type_ = input("type[credit/debit]: ")

         writer.writerow([company,customer,year,month,day,amount,type_])
#}  // ===== end add_bills function =====

def view_bills():
#{  
    global file_n
    with open(file_n, 'r', newline='') as file:
       reader = csv.reader(file)
       for row in reader:
           print(row)
#}  // ===== end view_bills function =====      

def browse_dir():
#{ 
    global file_n
    root = Tk()
    
    root.iconify()   # hide tk window
    root.withdraw()  # hide tk window
    #root.deiconify() # show tk window
    
    ftypes = [('CSV File',"*.csv")]
    ttl  = "Browse for File" 
    dir1 = 'C:\\'
    root.fileName = askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl)
    path=root.fileName
    
    root.quit()    # destroy the root window 
    root.destroy() # destroy the root window 
     
    print(path)
    file_n = path  
#}  // ===== end browse_dir function =====

def switch(arg):
#{ 
    if(arg == "b"):    # Bills_menu
        bills_helpscreen()
        choice = ""
        while choice != "b":
            choice = input("\nPlease, type the letter of your choice...\n\n")
            choice = choice.lower()
            choice = bills_switch(choice)
        sub_helpscreen()
        #break
    elif(arg == "r"):  # Report_menu
       reports_helpscreen()
       choice = ""
       while choice != "b":
            choice = input("\nPlease, type the letter of your choice...\n\n")
            choice = choice.lower()
            choice = reports_switch(choice)
       sub_helpscreen()
        #break
    elif(arg =="u"):
        os.system('start UserManual.pdf')
        #break
    elif(arg == "h"):  # helpscreen
       sub_helpscreen()
       #break
    elif(arg == "x"): # exit
        return "x"
        #break
    else :
        print("\nInvalid command...\n")
        sub_helpscreen()
       #break
#}  // ===== end switch function =====

def bills_switch(arg):
#{     
    if(arg == "v"):    # view_all
        view_bills()        
        #break
    elif(arg == "a"):  # add_new
        add_bill()
        #break
    elif(arg == "h"):  # helpscreen
       bills_helpscreen()
       #break
    elif(arg == "b"): # back_to_main
        return "b"
        #break
    else :
        print("\nInvalid command...\n")
        bills_helpscreen()
       #break
#}  // ===== end switch function =====

def reports_switch(arg):
#{     
    global bills
    global bills_df
    
    bills.__new__
    
    open_file()
    bills_df.columns = ['company', 'customer', 'year', 'month', 'day', 'amount_eur', 'credit_debit']
    company_count = bills_df.groupby("company")['amount_eur'].agg(total_bills='count')
    latest_bills = bills_df.sort_values(by=['year', 'month', 'day'],ascending=[False,False,False])
    
    # create a date column out of year, month and day and add to dataframe
    date_column = pd.to_datetime(bills_df[['year', 'month', 'day']].rename(columns={'YY': 'year', 'MM': 'month', 'DD': 'day'}))
    bills_df['date'] = date_column
    
    # calculate average time between bills
    bills_df['previous_bill'] = bills_df.groupby('customer')['date'].shift()
    bills_df['days_bw_bills'] = bills_df['date'] - bills_df['previous_bill']
    
    if(arg == "1"):    # List total debit and credit each year in ascending order
        year_debit_credit = bills_df['amount_eur'].groupby([bills_df['year'],bills_df['credit_debit']]).agg(total_amount_eur='sum')
        print('\n1. Viewing the Credit and Debit amounts for each year', year_debit_credit, '\n\n')      
        #break
    elif(arg == "2"):  # List the total number of bills per company
        print('\n2. Viewing the total number of bills for each utility company',company_count, '\n')
        #break
    elif(arg == "3"):  # Show most popular company based on number of bills
        arr_ = company_count.sort_values(by=['total_bills'],ascending=False)
        
        max_bill = int(arr_.max())
        company_highest = arr_.query('total_bills == @max_bill')
        
        if(len(company_highest) == 1):
            print('\nThe company with the most bills is:\n') 
        else :    
            print('\nThe companies with the most bills are:\n')
        print(company_highest)
        #break
    elif(arg == "4"):  # List bills by in descending order (date)
        
        print('\n4. Viewing all bills, latest first:\n')
        print(latest_bills)
        #break
    elif(arg == "5"):  # Show highest debit and credit amount on bills
        max_debit = bills_df.amount_eur[bills_df.credit_debit == ' debit'].max()
        max_credit = bills_df.amount_eur[bills_df.credit_debit == ' credit'].max()
        print('\nThe Maximum Debit on a bill is', max_debit)
        print('The Maximum Credit on a bill is', max_credit, '\n')
        #break
    elif(arg == "6"):  # User searches for the average amount on bills between a certain period of time (month/year) 
        print("=== Average bill between a period of time (yr) === ")
        start_yr = input("start_yr [yyyy]: ")
        end_yr   = input("end_yr [yyyy]: ")
        
        if((re.match('[\d]{4}$',start_yr)) and (re.match('[\d]{4}$',end_yr))):
            start_yr = int(start_yr)
            end_yr   = int(end_yr)
            
            if(start_yr>end_yr):
                start_yr, end_yr = end_yr, start_yr
                
            amount_average = latest_bills.amount_eur.loc[(latest_bills['year'] >= start_yr) & (latest_bills['year'] <= end_yr)].mean()
            print("-> Average bills: ", round(amount_average,2))
        #elif(re.match('[\d]{2}$',user_in)):
        #    print('correct Month format!')
        else :
            print('Invalid input format...')  
        #break
    elif(arg == "7"):  # Show average time between bills
       average_time = bills_df['days_bw_bills'].mean()
       print('\nThe average time between bills is', average_time, '\n')
        #break
    elif(arg == "h"):  # helpscreen
       reports_helpscreen()
       #break
    elif(arg == "b"): # back_to_main
        return "b"
        #break
    else :
        print("\nInvalid command...\n")
        reports_helpscreen()
       #break
#}  // ===== end switch function =====  

def sub_helpscreen():
#{ 
    print("***********************************************")
    print("*                                             *")
    print("*  MAIN DISPLAY MENU                          *")
    print("*                                             *")
    print("* B. View Bills                               *")
    print("* R. View Reports                             *")
    print("* U. View User Manual                         *")
    print("*                                             *")
    print("*                                             *")
    print("* H. help screen                              *")
    print("* X. exit (finish the program)                *")
    print("*                                             *")
    print("***********************************************")
#}  // ===== end helpscreen function ===== 

def bills_helpscreen():
#{ 
    print("***********************************************")
    print("*                                             *")
    print("*  BILLS DISPLAY MENU                         *")
    print("*                                             *")
    print("* V. View ALL                                 *")
    print("* A. Add Bill                                 *")
    print("*                                             *")
    print("*                                             *")
    print("* H. help screen                              *")
    print("* B. back to Main Menu                        *")
    print("*                                             *")
    print("***********************************************")
#}  // ===== end bills_helpscreen function ===== 

def reports_helpscreen():
#{ 
    print("***************************************************************")
    print("*                                                             *")
    print("*  REPORTS DISPLAY MENU                                       *")
    print("*                                                             *")
    print("* == BASIC Report ==                                          *")
    print("* 1. View Debit/Credit per year                               *")
    print("* 2. Show total bills/company                                 *")
    print("* 3. Show the most popular company                            *")
    print("* 4. Show all bills (most recent first)                       *")
    print("* 5. Show highest Debit and Credit amount                     *")
    print("* 7. Viewing average time between bills                       *")
    print("*                                                             *")
    print("* == SEARCH Report==                                          *")
    print("* 6. Search for average spent per period of time (month/year) *")
    print("*                                                             *")
    print("* H. help screen                                              *")
    print("* B. back to Main Menu                                        *")
    print("*                                                             *")
    print("***************************************************************")
#}  // ===== end reports_helpscreen function =====

def main():
#{  
    os.system("cls")
    sys.stdout.flush()
    
    print("\n")
    sys.stdout.write("\u001b[37;1m\u001b[44;1m")
    
    print("***************************************")
    print("* Data Analysis, Proc & Visualisation *")
    print("* Sophie Reisenleitner <10-544-58>    *")
    print("*                                     *")
    print("* Utility Bill Management  -v3.14     *")
    print("*                                     *")
    print("*                          (2019-12)  *")
    
    sub_helpscreen()
    
    choice = ""

    while choice != "x":
        choice = input("\nPlease, type the letter of your choice...\n\n")
        choice = choice.lower()
        choice = switch(choice)
        
    print("\n\nThank you for using my program!\nSee you later...   :)\n")
    time.sleep(4.0)
    sys.stdout.flush() 
    exit() #system.exit(0);
#}  // ===== end main function ===== 
      
    
# ======================== START Exec.  ========================     

open_file()

bills_df.columns = ['company', 'customer', 'year', 'month', 'day', 'amount_eur', 'credit_debit']

if(bills==""):# (bills_df=="") | (bills_df.empty)):
    exit() #sys.exit(0)
    #bills.close() 
else:
    loading("Loading...")
    sys.stdout.write("Successfully Loaded..."+ "\r")
    main()