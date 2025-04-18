"""
assessment2 part B
author: Ran Tominaga

"""


class RequisitionSystem():
    # Softwere Design Principle: Don't repeat yourself
    #using a counter to avoid repeat write code.
    requisition_counter = 10000

    def __init__(self,name="",staff_id="",date="",status=""):
    #Initializes objects with default staff information.
        self.date = date
        self.staff_id = staff_id
        self.staff_name =name
        self.status = status
        self.total = 0.0
        self.approval_reference_number = ""
        
        #provide a requisitio number each requisition 
        RequisitionSystem.requisition_counter += 1
        self.requisition = RequisitionSystem.requisition_counter
        
    
    def staff_info(self):
    # Softwere Design Principle: Single Responsibility , KISS
    # collecting input from the staff their information.
        self.date = input("Date (DD/MM/YYYY): ")        
        self.staff_id = input("Staff ID: ")       
        self.staff_name = input("Staff Name: ")
        return self.date,self.staff_id,self.staff_name,self.requisition
    
    
    def requisition_detail(self):
    # Softwere Design Principle: Single Responsibility
    # Staff input items and each price and calculate the total amount.

        items ={}
       
        chosen_item = input("what would you like to buy?\n (or 'done' if you want to finish):")
        while chosen_item.lower() != "done":
            price = float(input("Enter the price $:"))
            items[chosen_item] = price

            self.total += price

            chosen_item = input("what whould you like to buy?\n (or 'done' if you want to finish):")
        print(f"total is ${self.total}\n")
        return self.total
    
    
    
    def requisition_approval(self):
    # Software Design Principle: Separation of concern,  Single Responsibility
    # could be improved by separating decision porocess and putting in the lists approve and pending.
    
        if self.total < 500:
            self.status = "Approved"
            approve.append(self.status)
        
        elif self.total >=500:
            self.status = "Pending"
            pending.append(self.status)
       
        else:
            print("Error!")
           
            return self.status
    
    def respond_requisition(self):
    # Software Design Principle: Separation of concern,  Single Responsibility
    #mixed with manager's decisions and putting the list based on the status.
        if self.status == "Pending":
            
            while True:
                
                decision = input("type(1:Approved or 2:NotApproved or 3:Pending):")
                if decision == "1":
                    self.status = "Approved"
                    self.approval_reference_number = str(self.staff_id) + str(self.requisition)[-3:]
                    pending.pop()
                    approve.append(self.status)
                    break
                elif decision == "2":
                    self.status = "NotApproved"
                    self.approval_reference_number = "Not available"
                    pending.pop()
                    not_approve.append(self.status)
                    break
                    
                elif decision =="3":
                    self.approval_reference_number = "Pending"
                    break
                
                else:

                    print("oops something wrong! try it again")

        elif self.status == "Approved":
            self.approval_reference_number = str(self.staff_id) + str(self.requisition)[-3:]


    def display_requisition(self):
    # Softwere Design Principle: Single Responsibility Principle.
    # output the result based on staff information, total amount, status approval reference number and requisition number.
        print("\nPrinting Requisitions:")
        print(f"DATE:{self.date}")
        print(f"Requisition:{self.requisition}")
        print(f"Staff ID:{self.staff_id}")
        print(f"Staff Name:{self.staff_name}")
        print(f"Total:${self.total}")
        print(f"Status:{self.status}")
        print(f"Approval Reference Number:{self.approval_reference_number}")

    def requisition_statistic(self):
    # Softwere Design Principle: Single Responsibility Principle.
    #display the result of statistic
        requisitions_submitted = len(list_requisition)
        requisition_approve = len(approve)
        requisition_pending = len(pending)
        requisition_not_approve = len(not_approve)

        print("Displaying the Requisition Statistics")
        print(f"The total number of requisitions submitted: {requisitions_submitted}")
        print(f"The total number of approved requisitions: {requisition_approve}")
        print(f"The total number of pending requisitions:  {requisition_pending}")
        print(f"The total number of not approved requisitions:   {requisition_not_approve}")

# can be improved to make a class to manage
list_requisition = []
approve = []
not_approve = []
pending =[]
            
while True:
    
    user_input = input("\nStart to register? ('done' to finish):")
    if user_input.lower() == "done":
        break

    else:
        requisition = RequisitionSystem()
        requisition.staff_info()
        requisition.requisition_detail()
        requisition.requisition_approval()
        requisition.respond_requisition()
        requisition.display_requisition()
        list_requisition.append(requisition)

requisition.requisition_statistic()
