def staff_info():
    counter_ids = []

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
            Requisition_Id = counter_id
            print(f"Requisition ID: {Requisition_Id}")
            user_data = {
                "Staff_ID": Staff_ID,
                "Staff_Name": Name,
                "Date": Date,
                "Requisition _ID": Requisition_Id


            }

            return  user_data
print()        
        
user_info = staff_info()
print() 
print(user_info)


