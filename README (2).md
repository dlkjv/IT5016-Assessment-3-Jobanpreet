
# Software Design Principle

This document outlines the software design principles followed in the development of the password manager application.



# Single Responsibility Principle (SRP)

The Single Responsibility Principle (SRP) states that a class or function should have only one reason to change. In the provided code, each function has a single responsibility:

- write_key: This function is responsible for generating a key using the Fernet algorithm and writing it to a file named "key.key". It has a single reason to change, which is to modify the key generation or writing process.

- load_key: This function is responsible for loading the key from the "key.key" file. It has a single reason to change, which is to modify the key loading process.

- view: This function is responsible for viewing the encrypted passwords stored in the "password.txt" file. It has a single reason to change, which is to modify the password viewing process.

- add: This function is responsible for adding a new password to the "password.txt" file. It has a single reason to change, which is to modify the password adding process.

By following the SRP, the code is more modular, maintainable, and easier to understand.

# Don't Repeat Yourself (DRY)
The Don't Repeat Yourself (DRY) principle states that code should not be duplicated. In the provided code, the DRY principle is followed by:

- Using functions to perform specific tasks, such as write_key, load_key, view, and add. This avoids duplicating code and makes it more maintainable.

- Avoiding duplicated logic in the view and add functions, which both use the fer object to encrypt and decrypt passwords.

# Keep it Simple,Stupid (KISS)
 The Keep It Simple, Stupid (KISS) principle states that simplicity should be preferred over complexity. In the provided code, the KISS principle is followed by:

- Using simple and straightforward logic in the functions, avoiding complex algorithms or data structures.

- Using clear and concise variable names and function names, making it easy to understand the code.

# You Ain't Gonna Need It (YAGNI) 
The You Ain't Gonna Need It (YAGNI) principle states that features or code should not be added unless they are necessary. In the provided code, the YAGNI principle is followed by:

- Only implementing the necessary features for a password manager, without adding unnecessary complexity or functionality.

- Avoiding premature optimization or feature creep, focusing on the core functionality of the application.

# Refractor
The Refractor Mercilessly principle states that code should be continuously refactored to improve its quality and maintainability. In the provided code, the Refractor Mercilessly principle is followed by:

- Continuously reviewing and refactoring the code to ensure it is modular, readable, and maintainable.

- Improving the code organization, naming conventions, and coding standards to make it easier to understand and maintain.

# Clean Code
The Clean Code principle states that code should be written in a way that is easy to read, understand, and maintain. In the provided code, the Clean Code principle is followed by:

- Using clear and concise variable names and function names, making it easy to understand the code.
- Using whitespace and indentation to make the code readable.
- Avoiding duplicated code and logic, making it easier to maintain.

# Open-Closed Principle (OCP)
The Open-Closed Principle (OCP) states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. In the provided code, the OCP principle is followed by:

- Designing the code to be modular and extensible, allowing for new features to be added without modifying the existing code.

- Using abstraction and interfaces to decouple dependencies and make the code more flexible.

# SOLID Principles
The SOLID principles are a set of design principles that aim to promote simpler, more robust, and updatable code. In the provided code, the SOLID principles are followed by:

- Single Responsibility Principle (SRP): Each function has a single responsibility, making the code more modular and maintainable.

- Open-Closed Principle (OCP): The code is designed to be open for extension but closed for modification, making it more flexible and maintainable.

- Liskov Substitution Principle (LSP): The code uses abstraction and interfaces to ensure that subtypes can be used in place of base types, making it more flexible and maintainable.

- Interface Segregation Principle (ISP): The code uses interfaces to define contracts and decouple dependencies, making it more modular and maintainable.

- Dependency Inversion Principle (DIP): The code uses dependency injection to decouple dependencies and make it more modular and maintainable.

# Separation of Concerns (SoC)
The Separation of Concerns (SoC) principle states that a system should be divided into separate, independent components or modules, each handling a specific concern. In the provided code, the SoC principle is followed by:

- Dividing the code into separate functions, each handling a specific concern:
- Key management (generation, loading)
Password management (viewing, adding)
- Using separate files for storing the key ("key.key") and passwords ("password.txt"), which separates the concerns of key management and password management.

# Code Organization
The code is organized into logical sections, with each function performing a specific task. This makes it easier to understand and maintain.

# Code Quality
The code follows best practices for coding standards and conventions, such as:

- Using meaningful variable names and function names
- Using whitespace and indentation to make the code readable
- Using comments to explain the code

# Security
The code uses Fernet encryption to securely store and retrieve passwords. This ensures that the passwords are protected from unauthorized access.

By following these software design principles, the code is maintainable, scalable, and efficient, and ensures the security of the password manager application.

--Code Detailed Explanation--

# Password Manager

This password manager is a simple command-line application that uses the Fernet symmetric encryption algorithm from the cryptography library to store and retrieve passwords. The application is designed to provide a secure way to store and manage passwords for multiple accounts.

# Features
- Generates a unique encryption key for secure password storage

- Stores passwords in an encrypted file

- Allows users to add new passwords and view existing ones

- Provides a simple command-line interface for user interaction

# How To use
- Run the application by executing the Python script.
- The application will prompt you to enter a mode: 'add' to add a new password, 'view' to view existing passwords, or 'q' to quit.

- If you choose 'add', you will be prompted to enter the account name and password. The password will be encrypted and stored in the password file.

- If you choose 'view', the application will display the account names and decrypted passwords.
You can exit the application by entering 'q'.

# Security
- The encryption key is generated using the Fernet algorithm and stored in a file named "key.key".

- The passwords are stored in an encrypted file named "password.txt".

- The application uses the Fernet algorithm to encrypt and decrypt the passwords.

# Requirements
- Python 3.x
- cryptography library
