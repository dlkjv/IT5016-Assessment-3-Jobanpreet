def staff_info():
 counter_ids = []

 Requisition_Id = []
 Approval_ID = []
 while True:
        print("Printing Staff Information:")
        Staff_ID = str(input("Enter Staff ID:"))
        Name = input("Enter Staff Name:")
        Date = input("Enter Date:")
        if  Staff_ID == "finish" or  Name == "finish" or Date == "finish":
            break
        else:
            counter_id = int(input("Enter Counter ID:"))
            counter_ids.append(counter_id)
            counter_id =  counter_id + 1
            (Requisition_Id) = counter_id
            print(f"Requisition ID: {str(Requisition_Id)}")

            Approval_ID = str(Staff_ID) + str(Requisition_Id)[-3]  # Generate the Approval ID
            print(f"Approval ID is: {Approval_ID}")

            user_data = {
                "Staff_ID": Staff_ID,
                "Staff_Name": Name,
                "Date": Date,
                "Requisition_ID": Requisition_Id,
                "Approval_ID": Approval_ID  # Add the Approval ID to the dictionary
            }
              # Add user data to the list

            return user_data
print()        
        


def requisitions_total():
    item_details = []
    prices = []
    total = 0
    while True:
              item = input("Enter your  item('finish ' to stop):")
              
              
              if item.lower()  == 'finish':
               print("Your order will be ready soon")
               break
             
              else:
               price = int(input("Enter the price of the item:$"))
              
               item_details.append(item)
               prices.append(price)
               total += price
            
               print(f"Your total is ${total}")

               return total
            
               
         
def requisition_approval(total):
    
    while True:
        
        
        if total < 500:
            print("Status = Approved")
            return "Approved"

        else:
            print("Status = Pending")
            return "Pending"
            
            
user_info = staff_info()
print() 
print(user_info)
user_total_amt = requisitions_total()
print(user_total_amt)       
user_Status =  requisition_approval(user_total_amt)
print(f"Your status is {user_Status}")

print(f"Display Requisitions:")
print(f"Date: {user_info['Date']}")
print(f"Requisition ID: {user_info['Requisition_ID']}")
print(f"Staff ID: {user_info['Staff_ID']}")
print(f"Staff Name: {user_info['Staff_Name']}")
print(f"Total :  ${user_total_amt}")
print(f"Status:  {user_Status}")

print(f"Approval ID is: {user_info['Approval_ID']}")



            


    