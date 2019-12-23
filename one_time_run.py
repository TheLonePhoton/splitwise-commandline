from query_back import *


class OneTimeRun:
    def __init__(self):
        self._flag_group = False  # flag values to ensure that below queries run only once
        self._flag_users = False
    '''
    ONE TIME RUN:
        SERVER SIDE:
            _group_table
            _users_table
        CLIENT SIDE:
            _
    '''

    def group_table(self):
        try:
            sql.query_result("DROP TABLE IF EXISTS groups_info\
                              CREATE TABLE groups_info(\
                              group_id INT NOT NULL PRIMARY KEY AUTO INCREMENT,\
                              group_name VARCHAR(100) NOT NULL,\
                              creator VARCHAR(100) NOT NULL,\
                              time_stamp DATETIME NOT NULL")  # create group
        except:
            sql.db.rollback()
        finally:
            self._flag_group = True

    def users_table(self):
        try:
            sql.query_result("CREATE TABLE users(\
                                display_name VARCHAR(100) NOT NULL,\
                                username VARCHAR(100) NOT NULL PRIMARY KEY,\
                                passwd VARCHAR(100) NOT NULL,\
                                user_groups VARCHAR(100),\
                                temporal_id DATETIME\
                                )", "commit")  # create users
        except:
            sql.db.rollback()

        finally:
            self._flag_users = True
