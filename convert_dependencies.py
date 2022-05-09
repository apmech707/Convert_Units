import os

def value_error():
    print('Enter only numbers. No other characters.')

def choice_error():
    print('Not a valid entry - type help to see the list of options again.')

def info():
    
    print('\n--Convert Common Units Application--')
    print('\nEnter 1 for converting Pounds to kilograms.')
    print('Enter 2 for converting Kilograms to Pounds.')
    print('Enter 3 for converting Celsius to Fahrenheit.')
    print('Enter 4 for converting Fahrenheit to Celsius.')
    print('Enter 5 for converting Miles to Kilometers.')
    print('Enter 6 for converting Kilometers to Miles.')
    print('Enter log to view a list of your recent conversions')
    print('Enter clearlog to delete log')
    print('Enter reset to change your password')
    print('Enter exit at any time to exit')

def check_logged_file():
    try:
        with open('logged_files.txt') as f:
            pass
    except FileNotFoundError:
        with open('logged_files.txt', 'w') as f:
            pass

def change_pass():

    while True:
        verify = input("Enter your old password:\n")
        with open('new_program_flag.txt', 'r') as new_flag_file:
            old_pass = new_flag_file.read()
        if verify == old_pass:
            os.remove('new_program_flag.txt')
            set_pass()
            break
        elif verify != old_pass:
            continue
        elif verify == 'exit':
            break

def set_pass():
    try:
        with open('new_program_flag.txt', 'r') as new_flag_file:
            contents = new_flag_file.read()
    except FileNotFoundError:
        with open('new_program_flag.txt', 'w+') as new_flag_file:
            x = input("Welcome developer. Enter a password to manage log:\n")
            new_flag_file.write(x)

def convert(choice):
    if choice == '1':
        lbs = input('Convert lbs to kg. Enter number(lbs) here: ')
        if lbs.lower().strip() == 'exit':
            quit()
        while lbs != 'exit':
            try:
                lbs = float(lbs)  # this tests if user input is a base 10 number
            except ValueError:
                value_error()  # this calls the value_error() I created above
                lbs = input('Convert lbs to kg. Enter number(lbs) here: ')
                continue
            lbs = float(lbs)  
            kg = lbs / 2.2
            rounded_kg = (round(kg)) 
            with open('logged_files.txt', 'a') as file:
                file.write(f'{lbs} (lbs) = {kg} kg,')# this will write your entry to the .txt file in your dir
            print(f'\n\n{rounded_kg}kg')
            print(f'Exact: {kg}kg')
            break  # this breaks out of the while loop and, as a result finishes the convert() function.

    elif choice == '2':
        kilograms = input('Convert kg to lbs. Enter number(kg) here: ')
        if kilograms.lower().strip() == 'exit':
            quit()
        while kilograms != 'exit':
            try:
                kilograms = float(kilograms)
            except ValueError:
                value_error()
                kilograms = input('Convert kg to lbs. Enter number(kg) here: ')
                continue
            kilograms = float(kilograms)
            pounds = kilograms * 2.2
            rounded_pounds = (round(pounds))
            with open('logged_files.txt', 'a') as file:
                file.write(f'{kilograms} kg = {pounds} (lbs),')
            print(f'\n\n{rounded_pounds}(lbs)')
            print(f'Exact: {pounds}lbs')
            break

    elif choice == '3':
        c_temp = input('Convert Celsius to Fahrenheit. Enter number(temp.) in Celsius here: ')
        if c_temp.lower().strip() == 'exit':
            quit()
        while c_temp != 'exit':
            try:
                c_temp = float(c_temp)
            except ValueError:
                value_error()
                c_temp = input('Convert Celsius to Fahrenheit. Enter number(temp.) in Celsius here: ')
                continue
            c_temp = float(c_temp)
            f_temp = (c_temp * 1.8) + 32
            rounded_f_temp = (round(f_temp))
            with open('logged_files.txt', 'a') as file:
                file.write(f'{c_temp} C = {f_temp} F,')
            print(f'\n\n{rounded_f_temp}F')
            print(f'Exact: {f_temp}F')
            break

    elif choice == '4':
        fahrenheit_temp = input('Convert Fahrenheit to Celsius. Enter number(temp.) in Fahrenheit here: ')
        if fahrenheit_temp.lower().strip() == 'exit':
            quit()
        while fahrenheit_temp != 'exit':
            try:
                fahrenheit_temp = float(fahrenheit_temp)
            except ValueError:
                value_error()
                fahrenheit_temp = input('Convert Fahrenheit to Celsius. Enter number(temp.) in Fahrenheit here: ')
                continue
            fahrenheit_temp = float(fahrenheit_temp)
            celsius_temp = (fahrenheit_temp - 32) / 1.8
            rounded_ct = round(celsius_temp)
            with open('logged_files.txt', 'a') as file:
                file.write(f'{fahrenheit_temp} F = {celsius_temp} C,')
            print(f'\n\n{rounded_ct}C')
            print(f'Exact: {celsius_temp}C')
            break

    elif choice == '5':
        miles = input('Convert Miles to Kilometers. Enter number of miles here: ')
        if miles.lower().strip() == 'exit':
            quit()
        while miles != 'exit':
            try:
                miles = float(miles)
            except ValueError:
                value_error()
                miles = input('Convert Miles to Kilometers. Enter number of miles here: ')
                continue
            miles = float(miles)
            kilometers = (miles * 1.609344)
            rounded_kilometers = round(kilometers)
            with open('logged_files.txt', 'a') as file:
                file.write(f'{miles} Miles={kilometers} Kilometers,')
            print(f'\n\n{rounded_kilometers} Kilometers')
            print(f'Exact: {kilometers} Kilometers')
            break

    elif choice == '6':
        km = input('Convert Kilometers to Miles. Enter number of Kilometers here: ')
        if km.lower().strip() == 'exit':
            quit()
        while km != 'exit':
            try:
                km = float(km)
            except ValueError:
                value_error()
                km = input('Convert Kilometers to Miles. Enter number of Kilometers here: ')
                continue
            km = float(km)
            m = km * 0.6213712
            rounded_m = round(m)
            with open('logged_files.txt', 'a') as file:
                file.write(f'{km} Kilometers = {m} Miles,')
            print(f'\n\n{rounded_m} Miles')
            print(f'Exact: {m} Miles')
            break