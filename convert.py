''' This is a program that converts common units for you.
This program runs in the console and has no GUI. Have fun!'''

from convert_dependencies import *
import time

start = False




def end_program():
    global start
    start=False

def start_program():
    info()
    global start
    start=True

    while start:
        
        check_logged_file()
        set_pass()
        
        choices_allowed = ('1', '2', '3', '4', '5', '6')
        c = input("Enter your choice of conversion:")
        print(f'\nYou entered: {c}')

        if c.lower().strip() == 'exit':
            print("Convert program closed.\nEnter a new command or type help.")
            end_program()
            
        elif c.lower().strip() == 'help':
            info()  # This calls the function that lists the options
            continue
        elif c.lower().strip() == 'log':
            with open('logged_files.txt', 'r') as f:
                for line in f:
                    for i in  line.split(","):
                        print(i)
    
        elif c.lower().strip() == 'reset':
            change_pass()

        elif c.lower().strip() == 'clearlog':
            flag = True
            while flag:
                with open('new_program_flag.txt', 'r') as new_flag_file:
                    password = new_flag_file.read()
                check = input("Enter your password:\n")
                if check == password:
                    print("Password accepted.")
                    flag2 = True
                    a = "y"
                    b = "n"
                    while flag2:
                        admin = input("Confirm delete log. Enter Y or N:\n")
                        if admin.lower().strip() == a:
                            with open('logged_files.txt', 'w')as f:
                                f.write("")
                                print("log deleted")
                                flag = False
                                flag2 = False
                        elif admin.lower().strip() == b:
                            print("log NOT deleted")
                            flag = False
                            flag2 = False
                        elif admin.lower().strip() != a and admin.lower().strip() != b:
                            continue
                elif check != password:
                    print("Password not accepted. Unable to delete log")
                    continue
                elif check == 'exit':
                    flag = False
            del(password, check, flag, flag2, admin, a, b)
        elif c:
            if str(c.strip()) in choices_allowed:
                if len(str(c.strip())) == 1:
                    convert(c.strip())
                    continue
            elif str(c.strip()) not in choices_allowed or len(str(c.strip())) > 1:
                choice_error()
                continue
                
                
if __name__ == "__main__":
	start_program()
