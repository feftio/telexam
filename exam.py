from random import shuffle, choice, randint
from datetime import datetime, timedelta
from sqlite3 import Error
import string
import sqlite3
import json

MINUTES_FOR_TEST_SOLUTION = 30

def get_random_test_id():
    return string.digits

class Database:

    # CONSTRUCTOR
    def __init__(self, path):
        try:
            self.connection = sqlite3.connect(path)
            print("Connection is established: Database is created in memory")
        except Error:
            print(Error)
    
    # PUBLIC
    def select(self, table, fields, where=None):
        cursor = self.connection.cursor()
        if where is None:
            cursor.execute("SELECT {} FROM {}".format(fields, table))
        else:
            cursor.execute("SELECT {} FROM {} WHERE {}".format(fields, table, where))
        return cursor.fetchall()
    
    def exist(self, table, field, where):
        cursor = self.connection.cursor()
        cursor.execute("SELECT {} FROM {} WHERE {}".format(field, table, where))
        self.connection.commit()
        if len(cursor.fetchall()) == 0:
            return False
        return True

    def create(self, table, fields):
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS {}({})".format(table, fields))
        self.connection.commit()

    def insert(self, query, values):
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()

'''

exam.db structure

======================== tests ========================
=======================================================
|| test_id || test_name || test || minutes || points ||
=======================================================


====================== users =====================
==================================================
|| user_id || user_name || reg_date || is_admin ||
==================================================


==================================== units ===================================
==============================================================================
|| test_id || user_id || current || questions || answers || start || finish ||
==============================================================================

'''

class ExamDatabase(Database):

    # CONSTRUCTOR
    def __init__(self, path="exam.db"):
        super().__init__(path)
        self.create("tests", "test_id INTEGER NOT NULL PRIMARY KEY, test_name TEXT NOT NULL PRIMARY KEY, test JSON, minutes INTEGER, points INTEGER")
        self.create("users", "user_id INTEGER PRIMARY KEY, user_name TEXT, reg_date DATE, is_admin BOOL")
        self.create("units", "test_id INTEGER, user_id TEXT, questions JSON, answers JSON, start DATE, finish DATE")
    
    # INSERT
    def insert_test(self, *args):
        self.insert("INSERT INTO tests(test_id, test_name, test, minutes, points) VALUES(?, ?, ?, ?, ?)", list(args))

    def insert_user(self, *args):
        self.insert("INSERT INTO users(user_id, user_name, reg_date, is_admin) VALUES(?, ?, ?, ?)", list(args))

    def insert_unit(self, *args):
        self.insert("INSERT INTO units(test_id, user_id, questions, answers, start, finish) VALUES(?, ?, ?, ?, ?, ?)", list(args))

    # EXIST
    def exist_test(self, test_id):
        return self.exist("tests", "test_id", "test_id={}".format(test_id))
    
    def exist_user(self, user_id):
        return self.exist("users", "user_id", "user_id={}".format(user_id))

    def exist_unit_by_id(self, test_id, user_id):
        return self.exist("units", "test_id, user_id", "test_id={} AND user_id={}".format(test_id, user_id))
    
    def exist_unit_by_name(self, test_name, user_id):
        return self.exist("units", "test_name, user_id", "test_name=")
    
    # GENERAL
    def get_testlist(self):
        return self.select("tests", "test_name")


class Exam:

    # CONSTRUCTOR
    def __init__(self, path="exam.db"):
        self.database = ExamDatabase(path)

    # PRIVATE
    def add_user(self, user, is_admin=False):
        if not self.database.exist_user(user["id"])
            self.database.insert_user(
                user["id"], 
                user["name"],
                datetime.now(), 
                is_admin)
    
    def add_unit(self, user, test_name):
        if not self.database.exist_unit(test):
            start  = datetime.now()
            finish = start + timedelta(minutes=MINUTES_FOR_TEST_SOLUTION)
            self.database.insert_unit(
                name, 
                json.dumps(dict(self.__questions__)), 
                json.dumps({}), 
                start, 
                finish)

    # PUBLIC
    def get_testlist(self):
        return self.database.get_testlist()

    def choose_test(self, user, test_name):
        self.add_user(user)
        
        
    def get_question(self, user):
        self.add_user(user)
        self.add_unit(user)
        # todo

    def send_answer(self, user, answer):
        pass


class TestManager:
    
    # CONSTRUCTOR
    def __init__(self, path="exam.db"):
        self.database = ExamDatabase(path)
    
    # PUBLIC
    def add_test(self, test_dict):
        id    = 12345
        name  = test_dict["name"]
        test  = test_dict["test"]
        time  = test_dict["time"]
        point = test_dict["point"]
        self.database.insert_test(test_dict)
    
    def modify_test(self, test_name):
        pass

    def delete_test(self, test_name):
        pass

class Validator:
    
    # CONSTRUCTOR
    def __init__(self):
        pass

    def __new__(self):
        pass

    