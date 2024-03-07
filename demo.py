import secrets

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class LoginSystem:
    def __init__(self):
         # This is a hard-coded password, which is a bad practice. 

        self.user = User("admin", "password123") 

    def login(self, username, password):
        if username == self.user.username and password == self.user.password:
            print("Login successful!")
        else:
            print("Login failed!")

# Create a login system
login_system = LoginSystem()

# Try to login
login_system.login("admin", "password123")

SENSITIVE_TOKEN = secrets.token_hex(16)  # Generate a random hexadecimal string (32 characters)