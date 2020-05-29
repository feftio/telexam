from random import shuffle, choice, randint
import sqlite3
from sqlite3 import Error
from datetime import datetime, timedelta
import json


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
        self._create("exams", "id integer PRIMARY KEY, name text, exam json, minutes integer, points integer")
        self._create("users", "id integer PRIMARY KEY, name text, date date, admin bool")
        self._create("units", "id integer PRIMARY KEY, name text, questions json, answers json, start date, finish date")

    def insertExam(self, *args):
        self._insert("INSERT INTO exams(id, name, exam, minutes, points) VALUES(?, ?, ?, ?, ?)", list(args))

    def insertUser(self, *args):
        self._insert("INSERT INTO users(id, name, date, admin) VALUES(?, ?, ?, ?)", list(args))

    def insertUnit(self, *args):
        self._insert("INSERT INTO units(id, name, questions, answers, start, finish) VALUES(?, ?, ?, ?, ?, ?)", list(args))

    def existExam(self, name):
        return self._exist("exams", "id", "id={}".format(name))
    
    def existUser(self, id):
        return self._exist("users", "id", "id={}".format(id))

    def existUnit(self, id):
        return self._exist("units", "id", "id={}".format(id))


class Exam:

    # Constructor
    def __init__(self, path="exam.db"):
        self.__database = ExamDatabase(path)
    
    # Private
    def __addUser(self, user, isAdmin=False):
        if not self.__database.existUser(user["id"])
            self.__database.insertUser(user["id"], user["nick"], datetime.now(), isAdmin)
    
    def __addUnit(self, user):
        if not self.__database.existUnit():
            start = datetime.now()
            finish = start + timedelta(minutes=30)
            self.__database__.insertUnit(name, json.dumps(dict(self.__questions__)), json.dumps({}), start, finish)

    # Public
    def getQuestion(self, user):
        self.__addUser(user)
        self.__addUnit(user)
        # finish

    def sendAnswer(self, user, answer):
        pass











"""
class Exam:

##  Constructor Method

    def __init__(self, path="exam.db"):
        self.__database__ = ExamDatabase(path)

##  Private Methods

    def __addUser(self, user):
        self.__database__.insertUser(user["id"], user["nick"], datetime.now())

    def __addUnit(self, name, nick):
        start = datetime.now()
        finish = start + timedelta(minutes=30)
        self.__database__.insertUnit(name, json.dumps(dict(self.__questions__)), json.dumps({}), start, finish)

    def __existUser(self, id):
        return self.__database__.existUser(id)

##  Public Methods

    def loader(self, uid):
        return Loader(self.__database__, uid)

    def register(self, uid, nick):
        if not(self.__existUser(uid)):
            self.__database__.insertUser(uid, nick, datetime.now())
            return True
        return False

    def send(self, id, answer):
        pass


class Loader:

    def __init__(self, database, uid):
        self.__uid = uid
        self.__database = database
    
    def export(self, name, exam, minutes, points):
        if not(self.__database.existExam(name)):
            self.__database.insertExam(name, exam, minutes, points)
            return True
        return False
"""