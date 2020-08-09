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
        self._create("tests", "id_test INTEGER NOT NULL PRIMARY KEY, name TEXT NOT NULL PRIMARY KEY, test JSON, minutes INTEGER, points INTEGER")
        self._create("users", "id_user INTEGER PRIMARY KEY, name TEXT, date DATE, admin BOOL")
        self._create("units", "id_test INTEGER, id_user TEXT, questions JSON, answers JSON, start DATE, finish DATE")

    def insert_test(self, *args):
        self._insert("INSERT INTO tests(id_test, name, test, minutes, points) VALUES(?, ?, ?, ?, ?)", list(args))

    def insert_user(self, *args):
        self._insert("INSERT INTO users(id_user, name, date, admin) VALUES(?, ?, ?, ?)", list(args))

    def insert_unit(self, *args):
        self._insert("INSERT INTO units(id_test, id_user, questions, answers, start, finish) VALUES(?, ?, ?, ?, ?, ?)", list(args))

    def exist_test(self, id):
        return self._exist("tests", "id_test", "id_test={}".format(id))
    
    def exist_user(self, id):
        return self._exist("users", "id_user", "id_user={}".format(id))

    def exist_unit(self, id):
        return self._exist("units", "id_test, id_user", "id_test={} AND id_user={}".format(id_test, id_user))


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
    def get_question(self, user):
        self.__add_user(user)
        self.__add_unit(user)
        # finish

    def send_answer(self, user, answer):
        pass


class TestManager:

    def __init__(self, path="exam.db"):
        self.__database = ExamDatabase(path)

    def add_test(self, test_object):
        if type(test) is dict:
            id = 34324
            self.__database.insert_test(test_object)