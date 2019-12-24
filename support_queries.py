from query_back import *


def list_of_groups():
    result = sql.query_result("SELECT DISTINCT group_name FROM groups_info", "array")
    return result

def list_of_users():
    result = sql.query_result()


