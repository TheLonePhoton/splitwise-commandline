from query_back import *


def list_of_groups():
    result = sql.query_result("SELECT DISTINCT group_name FROM groups_info", "array")
    return result


def list_of_users():
    result = sql.query_result("SELECT DISTINCT username FROM users", "array")
    return result


def users_in_group(self, group_name):
    result = self.query_result("SELECT username FROM %s_cumulative" % group_name, "array")
    return result


