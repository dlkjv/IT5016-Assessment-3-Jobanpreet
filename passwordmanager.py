from cryptography.fernet import Fernet



def write_key():
    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)
    key_file.close()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key      

def view(fer):
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user, _, passw = data.partition('|')
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode() )

def add(fer):
    name = input("Account Name:")
    password = input("Enter your password:")
    with open('password.txt', 'a') as f:
        f.write(f"{name}|{fer.encrypt(password.encode()).decode()}\n")

try:
    key = load_key()
except FileNotFoundError:
    write_key()
    key = load_key()

fer = Fernet(key)

max_attempts = 3
attempts = 0

while True:
    mode = input("Whether you like to add new password or view existing one:")
    if mode == 'q':
        break
    if mode == "add":
        add(fer)
    elif mode == "view":
        view(fer)
    else:
        print("Invalid Option ")
        attempts += 1
        if attempts >= max_attempts:
            print("Too many invalid attempts. Exiting.")
            break