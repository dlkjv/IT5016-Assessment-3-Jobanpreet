
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