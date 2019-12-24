import pymysql


class QueryBack:
    db = pymysql.connect("localhost", "test", "tset", "splitwise_test")  # establishing a DB connection
    cursor = db.cursor()

    def query_result(self, query, out_type):
        #  give this func a query as a string , it will give you a result as array output
        #  Options: array - put the result in a array and return back
        #       raw - return the raw results - as tuple with commas...
        #       none - no output, only execute query
        #       commit - run a db.commit() to save changes
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        if out_type == "array":
            result = list(sum(res, ()))
            self.db.commit()
            return result
        elif out_type == "raw":
            self.db.commit()
            return res
        elif out_type == "commit":
            self.db.commit()  # saving the changes to db permanently...
            print("----Commit successfully-----")
        else:
            return 0

        # One time run, methods
        #   > transaction record table creation
        #   > cumulative table creation
    def new_group(self, creator):
        print("Enter the new group name: ", end='')
        group_name = input()
        try:
            self.query_result("INSERT INTO groups_info(group_name, creator, time_stamp)\
                              VALUES('%s', '%s', NOW())" % (group_name, creator), "commit")
                # Create a entry in group table, for new group creation..
            self.query_result("CREATE TABLE %s_transaction(\
                              trans_id INT NOT NULL AUTO INCREMENT PRIMARY KEY, \
                              Amount INT(100) NOT NULL,\
                              %s INT(100),\
                              TimeStamp DATETIME NOT NULL)" % (group_name, creator), "commit")
                # TRANSACTION TABLE QUERY
            self.query_result("CREATE TABLE %s_cumulative(\
                              username VARCHAR(100) NOT NULL PRIMARY KEY,\
                              %s INT(100) NOT NULL)" % (group_name, creator), "commit")
                # CUMULATIVE TABLE QUERY
            ''''
            self.query_result("INSERT INTO %s_cumulative (username) VALUES (%s)" % (group_name, creator), "commit")
                # Add creator to cumulative table
                # $ Nested Try & Except...
            '''
        except:
            self.db.rollback() # Don't rollback will occur for which commit above

        finally:
            self.add_to_group(group_name, creator)  # Creator added to group successfully...
            print("Group created successfully...\n Do you wanna add more members to group? Yes or No")
            response = input()
            if response.lower() == "yes":
               self.add_to_group(group_name)
            pass  # Add members to group...

    def add_to_group(self, group_name, username):
        print("Enter a valid username(email) to add: ")
        username = input().lower()
        if username == "null":
            #  add default user and user new user from outside ???
        elif username in list_of_users():
            pass
        else:
            print("Enter a valid username!")
            self.add_to_group(group_name)
        try:
            self.query_result("ALTER TABLE %s_transaction ADD %s INT(100) AFTER Amount" % \
                              (group_name, username), "commit")  # Add new users in a group as a column after Amount column
            self.query_result("ALTER TABLE %s_cumulative ADD %s INT(100) NOT NULL\
                              AFTER username" % (group_name, username), "commit") # Add new username to cumulative table
            self.query_result("INSERT INTO %s_cumulative (username) VALUES (%s)" % (group_name, username), "commit")
            # Add username as a first record since cumulative table...
        except:
            self.db.rollback()

    def group_users(self, group_name):
        try:
            result = self.query_result("SELECT username FROM %s_cumulative" % group_name, "array")
            return result
        except:
            self.db.rollback()


# Only one time run methods...



# main
sql = QueryBack()  # query back object...
 '''
    add_to_group() - adds new user to group, how to check user already in group or not
        > check in the cumulative table first column values...
        
        NEED FLAGS AND COUNTERS FOR NUMBER OF USERS CURRENTLY, NUMBER OF USERS in a group, number 
        NEW GROUP NEEDS group id - group id is unique - a separate table for group names and creator
 '''