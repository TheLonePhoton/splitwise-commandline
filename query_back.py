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


# main
sql = QueryBack()  # query back object...

'''
add_to_group() - adds new user to group, how to check user already in group or not
    > check in the cumulative table first column values...
    
    NEED FLAGS AND COUNTERS FOR NUMBER OF USERS CURRENTLY, NUMBER OF USERS in a group, number 
    NEW GROUP NEEDS group id - group id is unique - a separate table for group names and creator
 '''