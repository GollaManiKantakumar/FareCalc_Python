from models.user import User

class AuthService:
    def __init__(self):
        self.users = {}

    def register(self, acc_no, name, password):
        if acc_no in self.users:
            print("Account already exists")
            return None

        user = User(acc_no, name, password)
        self.users[acc_no] = user
        print("Account created successfully")
        return user

    def login(self, acc_no):

        user = self.users.get(acc_no)

        if not user:
            print("No credentials found, please create account")
            return None

        password = input("Enter Password: ")

        if user.password != password:
            print("Incorrect password")
            return None

        print("Login successful")
        return user