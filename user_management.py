from app_content import *
from query_back import *
import getpass


class UserManagement:
    sql = QueryBack()
    content = AppContent()

    def __init__(self):
        pass

    def authenticate(self):
        print("<LOG IN WINDOW> \n=================\nEnter username/email-id: ", end="")
        email = input()
        result1 = self.sql.query_result("SELECT username FROM users ", "array")  # check if username is in user table
        if email in result1:
            pass
        else:
            print("Invalid username")
            self.start()  # return back to start() - shit, here we go again.....
        # if username exists then  match password......,
        pwd = getpass.getpass()  # getting password hidden with getpass module
        result2 = self.sql.query_result("SELECT passwd FROM users WHERE username = '%s'" % email, "array")
        if result2[0] == pwd:
            print("=================\nLogging you in....")
            self.content.login_options(email)  # authentication successful - then print
        else:
            print("Try again")
            self.authenticate()

    def new_user(self):
        print("Enter Name(Display name): ")
        name = input()
        print("Enter username/email-id: ")
        email = input()
        result = self.sql.query_result("SELECT username FROM users", "array")
        if email not in result:
            pass
        else:
            print("Username already exits... Try again")
            self.new_user()
        print("Enter password: ")
        pwd_1 = input()
        print("Re-enter password: ")
        pwd_2 = input()
        if pwd_1 == pwd_2:
            pass
        else:
            print("passwords don't match! try again....")
            self.new_user()  # control goes to first line again, lot of work, need to change....
        query = "INSERT INTO users(username, display_name, passwd, temporal_id) \
        VALUES('%s', '%s', '%s', now())" % (email, name, pwd_1)
        self.sql.query_result(query, "commit")
        print("User account created successfully....")
        self.authenticate()

    def start(self):  # Where the app initializes - non repetitive initial processes are defined here...
        print("1) New user \n2) Existing User")
        choice = int(input())
        if choice == 2:
            self.authenticate()
        elif choice == 1:
            self.new_user()
        else:
            print("Enter a valid choice....")
            self.start()
        self.sql.db.close()  # Closing the db connection at the end of start function

