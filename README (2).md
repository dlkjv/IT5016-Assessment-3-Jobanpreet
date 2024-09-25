
# Software Design Principle

This document outlines the software design principles followed in the development of the password manager application.



# Single Responsibility Principle (SRP)

The Single Responsibility Principle (SRP) is aimed at that a given class or function can only change for one single reason. In the provided code, each function has a single responsibility:

write_key: This function is charged with the responsibility of creating a key through the Fernet algorithm and save the key to “key.key” file. It has a single reason for change; this is to change the way the key, or writing part is produced.

load_key: This function is also used to read the key from the file name key.key. It has only one reason to change namely to change the key loading process.

view: This function is actually used to read the encrypted passwords that are stored in a file known as “Password.txt” The only purpose which is provided in the algorithm is altering the method of password viewing.

add: This function is well targeted at creating a new password and converting the resultant value into a file format which will be in form of password.txt. It has been design to change solely for the aim of changing the password adding process.

For writing code in accordance with the SRP, the advantages which come out are It makes the code highly more modularity so that it is easier to manage and understand.

# Don't Repeat Yourself (DRY)
According to the principles, one of them is known as Don ‘t Repeat Yourself (DRY), and it implies that there should not be different code. In the provided code, the DRY principle is followed by:

•Using simple functions that are meant to do specific task such as write_key, load_key, view, add. This is the case because, it minimizes on code duplication as well as the management of the duplicated code in the long run.

Preventing code duplication of the view and add functions that makes use of the fer object to encrypt and decrypt passwords.

# Keep it Simple,Stupid (KISS)
 KISS is an acronym meaning keep it simple style, which means that the design should be as simple as possible. In the provided code, the KISS principle is followed by:

It will prevent making the execution of the functions too complicated by not using such equations and data types.

Properly naming of the variable and function so as to make it easier to relate to the written language.

# You Ain't Gonna Need It (YAGNI) 
YAGNI stands for You Ain’t Gonna Need It; it says an application should not be designed to have features or code that will not be needed. In the provided code, the YAGNI principle is followed by:

- Simply performing all the functional requirements of a password manager without going over the top on extra features.

Preventing either premature optimization or the addition of new features ad infinitum, narrowing down to the application’s key value proposition.

# Refractor
In a line, The Refractor Mercilessly principle is an Agile principle that states that the code with the team should always be refactored. In the provided code, the Refractor Mercilessly principle is followed by:

Once in a while to recap it and refactor where changing the code means making it more modular, readable, and maintainable.

Refactoring, as first step, can be defined as the action of turning the code into a more structured, better named, form that is easier to maintain.

# Clean Code
According to the Clean Code code should be clean to understand and follow, with no extra complications involved. In the provided code, the Clean Code principle is followed by:

Writing code using good assignment of variables names and the function names so that the code could be easily understandable.
Nevertheless, there is the specific responsibility of HMS to use spaces and tab stops so that such things do not occur making the script hardly readable.
It serves to prevent excessive usage of code, which overlaps, and a lot of logic that is undesirable when maintaining it.


# Open-Closed Principle (OCP)
The OCP can be explained as follows: Software artifacts; being classes, modules or functions, should be open to inclusion of new functionality but closed to alteration. In the provided code, the OCP principle is followed by:

Ensuring its easy to modify, that is the code aspect that it has to be designed in such a way that it is possible to add some new features in the future, without disturbing the existing code.

But, surprisingly, it is often possible to employ abstraction and interfaces to make the dependencies less evil and more innocent to the code.


# SOLID Principles
The SOLID principles are a list of principles of software design that are intended to help develop software that is easier to evolve than the existing software. In the provided code, the SOLID principles are followed by:

- Single Responsibility Principle (SRP): Every function serves one purpose, and it makes the codebase clean and easier to manage.

- Open-Closed Principle (OCP): The code should always be open for extension and closed for modification; this means that it is more flexible compared to the other.

- Liskov Substitution Principle (LSP): The given code comprises polymorphism and as to the type of polymorphism occurs in the specific example is abstraction and interfaces to use subtypes for the base types.

- Interface Segregation Principle (ISP): Randomness is reduced because the interfaces in the code suggest some contracts and minimum dependency between the objects.

- Dependency Inversion Principle (DIP): To increase modularity and maintainability the code applies Dependency Injection to take dependencies out of the classes and make them more flexible.

# Separation of Concerns (SoC)
Concern Separation (SoC) postulates that a system should be decomposed into several, independent yet interconnected parts each of which deals with a particular concern. In the provided code, the SoC principle is followed by:

- Dividing the code into separate functions, each handling a specific concern:
Key management (generation, loading and removing)
Passwords for viewing or adding (managing.)
The decision splits the creation and control of keys and passwords into two areas.

# Code Organization
The code is divided into separate sections – there are functions that accomplish certain and distinct operations. This is because it’s easier to comprehend and manage than an object-oriented design.

# Code Quality
The code follows best practices for coding standards and conventions, such as:

- Meaningful variable names and meaningful function names
Controlling using the concept of whitespace and indentation to make the code a little more readable.
– How to comment the code Just as a side note: I was really confused about what<E2/rd motivations> I was doing at the time, and I suggested using comments to explain the code.

# Security
For the passcode encryption/decryption in the code Fernet cryptography is employed. This makes it safe for passwords entered, and only the people that may wish to access it will do so safely.

Thus, through considering all these software design principles, the remained code is maintainable, scalable and efficient as well as provides password manager application security features.

--Code Detailed Explanation--

# Password Manager

It is a basic password manager that is a command line tool which uses symmetric encryption known as Fernet from the cryptography library. The application is basically an interface that can be used to securely store passwords for multiple accounts.

# Features
Creates an encryption key for passwords storage.

– Abuses are logged in a text file and passwords are stored encrypted on the local storage.

– The provided application enables users to create new passwords and also display the existing ones.

- Gives user interface through the command line interfaces.

# How To use
Start the application through the Python script.
- The application will prompt you to enter a mode: They are ‘add’ to give new password, ‘view’ to see the passwords or ‘q’ to exit.

If you choose ‘add’, type in the account name and password. The password will be stored in encrypted form in the password file.

: If you select ‘view’ the application shows the account names and decrypted passwords.
It will mean that you can leave the application by typing ‘q’.


# Security
Fernet is the chosen algorithm for creating an encryption key and this is stored under the file name “key.key”.

The passwords are saved into a file named “password.txt” and they are encrypted.

– The application uses Fernet Algorithm to perform both encryption and decryption of the passwords.


