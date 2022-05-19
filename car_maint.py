''' This project is a work in progress. It runs and can use the convert.py program, but is functionally incomplete. I am not sure
at this point which direction I want to take it so I have put it up here and will work with it in public. If you would like to take it in 
another direction as I add to it you are free to fork it.'''

import datetime
import convert


maint_schedule={}
work_order={}
date = datetime.datetime.now()

class car():
    """ Represents my car, gives methods to use when performing maintenance, and leaves room to expand if I own more cars in the future """
    
    def __init__(self, year, make, mileage):
        self.year=year
        self.mileage=mileage
        self.maint_history = {}
        self.wishlist= []
    
    def request_maint(self, maint):
        """ Adds a maintenance event to the work_order dict """
        global work_order
        work_order[maint]=date.strftime('%m-%d-%Y    %H:%M:%S')
        print(f"Maintenance event due: {maint}\n")

    def close_maint_item(self, maint):
        """ Adds current maintenance event to maint_history dict, and clears applicicable maintenance event from work_order dict """
        self.maint_history[maint]= date.strftime('%Y-%m-%d    %H:%M:%S')
        global work_order
        del work_order[maint]
        print(f"Closed maintenance item {maint}")
        
    def print_work_order(self):
        global work_order
        print(work_order)
        print("\n")
        
    def update_mileage(self, new_mileage):
        self.mileage=new_mileage
        print("Mileage updated\n")
            
    def print_history(self):
        x=0
        for i in maint_history:
            x+=1
        if x>0:
            print(f"Maintenance History: {self.maint_history}\n")
        else:
            print("None")
            
    def wishlist_add(self, item):
        self.wishlist.append(item)
        print("Wishlist item added\n")
        
    def print_wishlist(self):
        print(self.wishlist)

miles= 63000
barry_baluga= car(2014, "Subaru", miles)
flag=False


while True:
    my_car= barry_baluga
    
    if flag==False:
        print("\nWelcome.\nUse this app to assist with your car's maintnenance schedule.\nType help for a list of available commands.\nRead the \"README\" file for more indepth description of how to use the commands.\nEnjoy, and happy wrenching.")
        flag=True
    command=input()
    
    if command == "help":
        # adding \n new_car(year, make, mileage) soon
        print("\nType command first, then on next input prompt enter the appropriate item in brackets'()'\nIf brackets are empty no secondary input is required\n")
        print("Commands: \n request_maint  (a maintenance request) \n close_maint_item  (which maintenance event to close) \n update_mileage  (new mileage) \n print_history  () \n print_work_order  () \n wishlist_add  (item) \n print_wishlist  () \n convert  () \n exit  ()")
        continue

    if command == "request_maint":
        maint=input()
        my_car.request_maint(maint)
        continue
        
    elif command == "close_maint_item":
        maint=input()
        my_car.close_maint_item(maint)
        continue
    
    elif command == "update_mileage":
        new_mileage=input()
        new_mileage=int(new_mileage)
        my_car.update_mileage(new_mileage)
        continue
    
    elif command == "print_history":
        my_car.print_history()
        continue
    
    elif command == "print_work_order":
        my_car.print_work_order()
        continue
        
    elif command == "wishlist_add":
        item=input()
        my_car.wishlist_add(item)
        continue
        
    elif command == "print_wishlist":
        my_car.print_wishlist()
        continue
        
    elif command == "convert":
        convert.start_program()
        continue
    
    elif command == "new_car":
        # still working on it
        pass
    
    elif command == "exit":
        exit()
    
    else:
        print("No output. Type help")
        continue

