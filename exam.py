from random import shuffle, choice, randint
from datetime import datetime, timedelta
from sqlite3 import Error
import string
import sqlite3
import json

def get_random_test_id():
    return string.digits

class Database:

    def __init__(self, path="database.db"):
        try:
            self.connection = sqlite3.connect(path)
            print("Connection is established: Database is created in memory")
        except Error:
            print(Error)

    def _select(self, table, fields, where=None):
        cursor = self.connection.cursor()
        cursor.execute("SELECT {} FROM {}".format(fields, table))
        return cursor.fetchall()

    def _exist(self, table, field, where):
        cursor = self.connection.cursor()
        cursor.execute("SELECT {} FROM {} WHERE {}".format(field, table, where))
        self.connection.commit()
        if len(cursor.fetchall()) == 0:
            return False
        return True

    def _create(self, table, fields):
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS {}({})".format(table, fields))
        self.connection.commit()

    def _insert(self, query, values):
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()


class ExamDatabase(Database):

    def __init__(self, path="exam.db"):
        super().__init__(path)
        self._create("tests", "test_id INTEGER NOT NULL PRIMARY KEY, test_name TEXT NOT NULL PRIMARY KEY, test JSON, minutes INTEGER, points INTEGER")
        self._create("users", "user_id INTEGER PRIMARY KEY, user_name TEXT, reg_date DATE, is_admin BOOL")
        self._create("units", "test_id INTEGER, user_id TEXT, questions JSON, answers JSON, start DATE, finish DATE")

    def insert_test(self, *args):
        self._insert("INSERT INTO tests(test_id, test_name, test, minutes, points) VALUES(?, ?, ?, ?, ?)", list(args))

    def insert_user(self, *args):
        self._insert("INSERT INTO users(user_id, user_name, reg_date, is_admin) VALUES(?, ?, ?, ?)", list(args))

    def insert_unit(self, *args):
        self._insert("INSERT INTO units(test_id, user_id, questions, answers, start, finish) VALUES(?, ?, ?, ?, ?, ?)", list(args))

    def exist_test(self, test_id):
        return self._exist("tests", "test_id", "test_id={}".format(test_id))
    
    def exist_user(self, user_id):
        return self._exist("users", "user_id", "user_id={}".format(user_id))

    def exist_unit(self, test_id, user_id):
        return self._exist("units", "test_id, user_id", "test_id={} AND user_id={}".format(test_id, user_id))

    def get_testlist(self):
        return self._select("tests", "test_name")


class Exam:

    # Constructor
    def __init__(self, path="exam.db"):
        self.__database = ExamDatabase(path)
    
    # Private
    def __add_user(self, user, is_admin=False):
        if not self.__database.exist_user(user["id"])
            self.__database.insert_user(user["id"], user["name"], datetime.now(), is_admin)
    
    def __add_unit(self, test):
        if not self.__database.exist_unit():
            start = datetime.now()
            finish = start + timedelta(minutes=30)
            self.__database__.insert_unit(name, json.dumps(dict(self.__questions__)), json.dumps({}), start, finish)

    # Public
    def get_testlist(self):
        return self.__database.get_testlist()

    def choose_test(self, user, test_name):
        self.__add_user(user)

    def get_question(self, user):
        self.__add_user(user)
        self.__add_unit(user)
        # finish

    def send_answer(self, user, answer):
        pass


class TestManager:

    def __init__(self, path="exam.db"):
        self.__database = ExamDatabase(path)

    def add_test(self, test_dict):
        id = 12345
        name = test_dict["name"]
        test = test_dict["test"]
        time = test_dict["time"]
        point = test_dict["point"]
        self.__database.insert_test(test_dict)

class Validator:

    def __init__(self):
        pass

    def __new__(self):
        pass

    