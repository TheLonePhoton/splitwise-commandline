import pymysql


class QueryBack:
    db = pymysql.connect("localhost", "root", "Vaaariable", "splitwise_test")  # establishing a DB connection
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
            return result
        elif out_type == "raw":
            return res
        elif out_type == "commit":
            self.db.commit()  # saving the changes to db permanently...
            print("----Commit successfully-----")
        else:
            return 0

        # One time run, methods
        #   > transaction record table creation
        #   > cumulative table creation
    def new_group(self, grp_name, creater):
        try:
            self.query_result("CREATE TABLE %s_transaction(\
                              trans_id INT NOT NULL AUTO INCREMENT PRIMARY KEY, \
                              Amount INT(100) NOT NULL,\
                              %s INT(100),\
                              TimeStamp DATETIME NOT NULL)" % (grp_name, creater), "commit") # TRANSACTION TABLE QUERY
            self.query_result("CREATE TABLE %s_cumulative(\
                              username VARCHAR(100) NOT NULL PRIMARY KEY,\
                              %s INT(100) NOT NULL)" % (grp_name, creater), "commit")  # CUMULATIVE TABLE QUERY
            self.query_result("INSERT INTO %s_cumulative (username) VALUES (%s)" % (grp_name, creater), "commit") # Add creater to cumulative table
        finally:
            #  self.db.commit()
            pass

    def add_to_group(self, group, username):
        try:
            self.query_result("ALTER TABLE %s_transaction ADD %s INT(100) AFTER Amount" % \
                              (group, username), "commit")  # Add new users in a group as a column after Amount column
            self.query_result("ALTER TABLE %s_cumulative ADD %s INT(100) NOT NULL\
                              AFTER username" % (group, username), "commit") # Add new username to cumulative table
            self.query_result("INSERT INTO %s_cumulative (username) VALUES (%s)" % (group, username), "commit")
        finally:
            pass


# main
sql = QueryBack()  # query back object...
 '''
    add_to_group() - adds new user to group, how to check user already in group or not
        > check in the cumulative table first column values...
        
        NEED FLAGS AND COUNTERS FOR NUMBER OF USERS CURRENTLY, NUMBER OF USERS in a group, number 
 '''