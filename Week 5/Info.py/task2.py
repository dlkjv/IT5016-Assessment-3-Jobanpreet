



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
            
               
         
requisitions_total() 



