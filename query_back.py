import pymysql


class QueryBack:
    #  def __init__(self):
    db = pymysql.connect("localhost", "root", "Vaaariable", "splitwise_test")  # establishing a DB connection
    cursor = db.cursor()

    # def create_connection(self):
    #     db = pymysql.connect("localhost", "root", "Vaaariable", "splitwise_test")  # establishing a DB connection
    #     cursor = db.cursor()

    def query_result(self, query, out_type):
        #  give this func a query as a string , it will give you a result as array output
        #  Options: array - put the result in a array and return back
        #       raw - return the raw results - as tuple with commas...
        #       none - no output, only execute query
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        if out_type == "array":
            result = list(sum(res, ()))
            return result
        elif out_type == "raw":
            return res
        else:
            return 0



# main
# sql = QueryBack()  # query back object...
