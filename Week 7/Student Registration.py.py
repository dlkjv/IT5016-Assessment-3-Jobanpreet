class Student:
    def __init__(self, student_id, last_name, programme):
        self.student_id = student_id
        self.last_name = last_name
        self.programme = programme

    def __str__(self):
        return f"{self.last_name} ({self.student_id}) - {self.programme}"


class MembershipSystem:
    def __init__(self):
        self.members = []
        self.withdrawn_members = 0
        self.diploma_students = 0
        self.bachelor_students = 0

    def register_member(self, student_id, last_name, programme):
        if programme not in ["Diploma", "Bachelor"]:
            print("Invalid programme. Please enter 'Diploma' or 'Bachelor'.")
            return
        student = Student(student_id, last_name, programme)
        self.members.append(student)
        if programme == "Diploma":
            self.diploma_students += 1
        else:
            self.bachelor_students += 1
        print(f"Member {last_name} ({student_id}) registered successfully.")

    def withdraw_member(self, membership_id, last_name):
        for student in self.members:
            if student.student_id == membership_id and student.last_name == last_name:
                self.members.remove(student)
                self.withdrawn_members += 1
                if student.programme == "Diploma":
                    self.diploma_students -= 1
                else:
                    self.bachelor_students -= 1
                print(f"Member {last_name} ({membership_id}) withdrawn successfully.")
                return
        print("Member not found.")

    def display_members(self):
        print("Registered Members:")
        for student in self.members:
            print(student)
        print(f"Number of registered members: {len(self.members)}")
        print(f"Number of Diploma students: {self.diploma_students}")
        print(f"Number of Bachelor students: {self.bachelor_students}")
        print(f"Number of withdrawn members: {self.withdrawn_members}")


def main():
    system = MembershipSystem()
    while True:
        print("\nMembership Registration System Menu")
        print("1. Register a member")
        print("2. Withdraw a member")
        print("3. Display registered members")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            student_id = input("Enter student ID: ")
            last_name = input("Enter student last name: ")
            programme = input("Enter student programme (Diploma or Bachelor): ")
            system.register_member(student_id, last_name, programme)
        elif choice == "2":
            membership_id = input("Enter membership ID: ")
            last_name = input("Enter student last name: ")
            system.withdraw_member(membership_id, last_name)
        elif choice == "3":
            system.display_members()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


class Student():
    def __init__(self,Student_id,last_name,Programme):
        self.Student_id = Student_id
        self.last_name = last_name
        self.Programme = Programme

    def __str__(self):
        return f"{self.Student_id} ({self.last_name} - {self.Programme})"

    def Membershipsystem(self):
        self.members = []
        self.withdrawn_members = 0
        self.diploma_members = 0
        self.bachelor_members = 0

    def register_member(self,Student_id,last_name,Programme):
        if Programme not in ("Diploma","Bachelor"):
            print("Invalid programme. Please enter either Diploma or Bachelor.")
            return
        student =  Student(Student_id,last_name,Programme)
        self.members.append(student)
        if  Programme == "Diploma":
            self.diploma_members += 1
        else:
            self.bachelor_members += 1
            print(f"Member {last_name} {Student_id} has been registered successfully.")

    def withdraw_member(self, membership_id, last_name):
        for student in self.members:
            if student.student_id == membership_id and student.last_name == last_name:
                self.members.remove(student)
                self.withdrawn_members += 1
                if student.programme == "Diploma":
                    self.diploma_students -= 1
                else:
                    self.bachelor_students -= 1
                print(f"Member {last_name} ({membership_id}) withdrawn successfully.")
                return
        print("Member not found.")
        return  
 


