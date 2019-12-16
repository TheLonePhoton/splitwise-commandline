from query_back import *


class AppContent:
    sql = QueryBack()

    def __int__(self):
        pass

    def group_mgmt(self, grp_name):
        self.sql.query_result("SELECT DISTINCT groups FROM users", "array")
        print("Do you want to join a existing group above?")
        response = input()

    def show_balances(self, email):
        # look for "user's" data in the database and show, how much he owe's to everyone
        result = self.sql.query_result("SELECT display_name FROM user WHERE username='%s'" % email, "array")
        print("Hello %s", result[0])
        print("Your current balances are")
        for i in balances:
            if i == user:
                for j in balances[i]:
                    print(user, " owes - ", j, " ", balances[i][j])

    def hello(self):  # hello method for checking successful login
        print("Hello from AppContent")
