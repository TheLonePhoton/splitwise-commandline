from support_queries import *
from query_back import *


class AppContent:
    def __int__(self):
        pass

    def group_mgmt(self, grp_name):
        sql.query_result("SELECT DISTINCT groups FROM users", "array")
        print("Do you want to join a existing group above?")
        response = input()

    def show_balances(self, email):
        # look for "user's" data in the database and show, how much he owe's to everyone
        result = sql.query_result("SELECT display_name FROM user WHERE username='%s'" % email, "array")
        print("Hello %s", result[0])
        print("Your current balances are")

    def login_options(self, username):  # hello method for checking successful login
        print("Choose any option: \n1) Create group \n2) Choose existing group(type group name and enter) : ", end='')
        result = sql.query_result("SELECT user_groups FROM users WHERE username='%s'" % username, "array")
        for i in result: print(i, end=', ')
        response = input()
        if response == '1':
            sql.new_group(username)  # create group method, username = creator
            self.login_options(username)
        elif response in list_of_groups():
            pass  # Show balances in that group

        #  How to add more than group for if he's in more than one group??
