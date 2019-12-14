from query_back import *


class AppContent:
    sql = QueryBack()

    def __int__(self):
        pass

    def group_mgmt(self, grp_name):
        self.sql.query_result("SELECT DISTINCT groups FROM users", "array")
        print("Do you want to join a existing group above?")
        response = input()

    def show_balances(self, user):
        # look for "user's" data in the database and show, how much he owe's to everyone
        pass
        print("Hello from app_content ", user)
        balances = {"Ethan": {"Siva": 0, "Nash": 0},
                    "Siva": {"Ethan": 0, "Nash": 0},
                    "Nash": {"Siva": 0, "Ethan": 0}
                    }
        print("Your current balances are")
        for i in balances:
            if i == user:
                for j in balances[i]:
                    print(user, " owes - ", j, " ", balances[i][j])

    def hello(self):
        print("Hello from AppContent")
