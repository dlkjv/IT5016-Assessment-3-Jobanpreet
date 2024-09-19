class RequisitionSystems:
    requests = []
    counter_id = 10000

    def __init__(self):
        self.Requisition_id = RequisitionSystems.counter_id
        RequisitionSystems.counter_id += 1
        RequisitionSystems.requests.append(self)
        self.approval_status = None
        self.total = 0
        self.date = None
        self.name = None
        self.staff_id = None
        self.items = []
        self.prices = []

    def staff_info(self):
        self.date = input("Enter date: ")
        self.name = input("Enter name: ")
        self.staff_id = input("Enter staff ID: ")

    def requisition_info(self):
        self.staff_info()
        self.requisition_details()

    def requisition_details(self):
        self.total = 0
        while True:
            item = input("Enter item name (or 'done' to finish): ")
            if item.lower() == 'done':
                break
            price = float(input("Enter item price: "))
            self.items.append(item)
            self.prices.append(price)
            self.total += price

    def requisition_approval(self):
        if self.total >= 100:
            self.approval_status = "Approved"
        else:
            self.approval_status = "Pending"

    def respond_requisition(self):
        if self.approval_status == "Pending":
            response = input("Do you want to approve or reject this request? (approve/reject): ")
            if response.lower() == "approve":
                self.approval_status = "Approved"
            elif response.lower() == "reject":
                self.approval_status = "Rejected"
            else:
                print("Invalid input. Please enter 'approve' or 'reject'.")
        else:
            print("This request is already responded to.")

    def reference_number(self):
        if self.approval_status == "Approved":
            Approval_reference = self.name + str(self.Requisition_id)[-3:]
            return Approval_reference
        elif self.approval_status == "Rejected":
            return "Rejected"
        else:
            return "NOT AVAILABLE"

    def display_requisition(self):
        print(f"Date: {self.date}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.name}")
        print(f"Unique ID: {self.Requisition_id}")
        print(f"Category: {self.approval_status}")
        print(f"Approval Reference: {self.reference_number()}")
        
        print(f"Total Amount: {self.total}")
        print()
        print("Request Items")
        for i in range(len(self.items)):
            print(f"Item {i+1}: {self.items[i]} - Price: {self.prices[i]}")

    def requisition_statistic(self): 
        total_requests = len(RequisitionSystems.requests)
        pending_requests = sum(1 for request in RequisitionSystems.requests if request.approval_status == 'Pending')
        approved_requests = sum(1 for request in RequisitionSystems.requests if request.approval_status == 'Approved')
        not_approved_requests = sum(1 for request in RequisitionSystems.requests if request.approval_status == 'Rejected')

        print(f"Total requests: {total_requests}")
        print(f"Pending requests: {pending_requests}")
        print(f"Approved requests: {approved_requests}")
        print(f"Not Approved requests: {not_approved_requests}")


def main():
    while True:
        print("1. Register")
        print("3. Request approval")
        print("4. Respond to request")
        print("5. Display all information")
        print("6. View statistics")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            request_system = RequisitionSystems()  # Create a new instance for each registration
            request_system.requisition_info()
        elif choice == "3":
            for request in RequisitionSystems.requests:
                request.requisition_approval()
                print(f"Requisition ID: {request.Requisition_id}, Status: {request.approval_status}")
        elif choice == "4":
            if not RequisitionSystems.requests:
                print("No pending requests to respond to.")
            else:
                for request in RequisitionSystems.requests:
                    if request.approval_status == "Pending":
                        print(f"Requisition ID: {request.Requisition_id}, Status: {request.approval_status}")
                        request.respond_requisition()
                        print(f"Requisition ID: {request.Requisition_id}, Status: {request.approval_status}")
                    else:
                        print(f"Requisition ID: {request.Requisition_id}, Status: {request.approval_status} (Already responded to)")
        elif choice == "5":
            for request in RequisitionSystems.requests:
                request.display_requisition()
                print("-" * 50)
        elif choice == "6":
            RequisitionSystems().requisition_statistic()  # Use a new instance to view statistics
        elif choice == "7":
            break


if __name__ == "__main__":
    main()