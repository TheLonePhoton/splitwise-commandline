from app_content import *
from query_back import *
import support_queries


def new_group(creator):
    print("Enter the new group name: ", end='')
    group_name = input()
    try:
        sql.query_result("INSERT INTO groups_info(group_name, creator, time_stamp)\
                          VALUES('%s', '%s', NOW())" % (group_name, creator), "commit")
        # Create a entry in group table, for new group creation..
        sql.query_result("CREATE TABLE %s_transaction(\
                          trans_id INT NOT NULL AUTO INCREMENT PRIMARY KEY, \
                          Amount INT(100) NOT NULL,\
                          %s INT(100),\
                          TimeStamp DATETIME NOT NULL)" % (group_name, creator), "commit")
        # TRANSACTION TABLE QUERY
        sql.query_result("CREATE TABLE %s_cumulative(\
                          username VARCHAR(100) NOT NULL PRIMARY KEY,\
                          %s INT(100) NOT NULL)" % (group_name, creator), "commit")
        # CUMULATIVE TABLE QUERY
        ''''
        self.query_result("INSERT INTO %s_cumulative (username) VALUES (%s)" % (group_name, creator), "commit")
            # Add creator to cumulative table
            # $ Nested Try & Except...
        '''
    except:
        sql.db.rollback()  # Don't rollback will occur for which commit above

    finally:
        add_to_group(group_name, creator)  # Creator added to group successfully...
        print("Group created successfully...\n Do you wanna add more members to group? Yes or No")
        response = input()
        if response.lower() == "yes":
            add_to_group(group_name, creator)
        else:
            login_obj = AppContent()
            login_obj.login_options(creator)


def add_to_group(group_name, username):
    result = support_queries.list_of_users()
    print(result)
    if username not in result:
        print("Enter a valid username(email) to add: ")
        username = input().lower()
        add_to_group(group_name, username)
    else:
        pass  # Add username to group
    # ADD USERS QUERY >
    try:
        sql.query_result("ALTER TABLE %s_transaction ADD %s INT(100) AFTER Amount" % (group_name, username), "commit")
        #  Add new users in a group as a column after Amount column
        sql.query_result("ALTER TABLE %s_cumulative ADD %s INT(100) NOT NULL\
                          AFTER username" % (group_name, username), "commit")  # Add new username to cumulative table
        sql.query_result("INSERT INTO %s_cumulative (username) VALUES (%s)" % (group_name, username), "commit")
        # Add username as a first record since cumulative table...
    except:
        sql.db.rollback()
    finally:
        print("User added successfully...\nDo you wanna add more members to group? Yes or No")
        response = input()
        if response.lower() == "yes":
            add_to_group(group_name, username)
        else:
            login_obj = AppContent()
            login_obj.login_options(username)
