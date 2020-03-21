from random import shuffle, choice, randint
import sqlite3
from sqlite3 import Error
from datetime import datetime, timedelta
import json





#################################################
################ Class: Database ################
#################################################
class Database:

    def __init__(self, path="database.db"):
        try:
            self.connection = sqlite3.connect(path)
            print("Connection is established: Database is created in memory")
        except Error:
            print(Error)
    
    def _exist_(self, table, field, where):
        cursor = self.connection.cursor()
        cursor.execute("SELECT {} FROM {} WHERE {}".format(field, table, where))
        self.connection.commit()
        if len(cursor.fetchall()) == 0:
            return False
        return True

    def _create_(self, table, fields):
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS {}({})".format(table, fields))
        self.connection.commit()

    def _insert_(self, query, values):
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()





#################################################
############## Class: ExamDatabase ##############
#################################################
class ExamDatabase(Database):

    def __init__(self, path="exam.db"):
        super().__init__(path)
        self._create_("exams", "name text PRIMARY KEY, exam json, minutes integer, points integer")
        self._create_("users", "id integer PRIMARY KEY, nick text, date date, admin bool")
        self._create_("units", "id integer, name text, questions json, answers json, start date, finish date")

    def insertExam(self, *args):
        self._insert_("INSERT INTO exams(name, exam, minutes, points) VALUES(?, ?, ?, ?)", list(args))

    def insertUser(self, *args):
        self._insert_("INSERT INTO users(id, name, date) VALUES(?, ?, ?)", list(args))

    def insertUnit(self, *args):
        self._insert_("INSERT INTO units(id, questions, done, start, finish) VALUES(?, ?, ?, ?, ?)", list(args))

    def existExam(self, name):
        return self._exist_("exams", "name", "name={}".format(name))
    
    def existUser(self, id):
        return self._exist_("users", "id", "id={}".format(id))





#################################################
################## Class: Exam ##################
#################################################
class Exam:

##  Constructor Method

    def __init__(self, path="exam.db"):
        self.__database__ = ExamDatabase(path)

##  Private Methods

    def __addUser__(self, user):
        self.__database__.insertUser(user["id"], user["nick"], datetime.now())

    def __addUnit__(self, name, nick):
        start = datetime.now()
        finish = start + timedelta(minutes=30)
        self.__database__.insertUnit(name, json.dumps(dict(self.__questions__)), json.dumps({}), start, finish)

    def __existUser__(self, id):
        return self.__database__.existUser(id)

##  Public Methods

    def loader(self, uid):
        return Loader(self.__database__, uid)

    def register(self, uid, nick):
        if not(self.__existUser__(uid)):
            self.__database__.insertUser(uid, nick, datetime.now())
            return True
        return False

    def send(self, id, answer):
        pass





#################################################
################# Class: Loader #################
#################################################
class Loader:

    def __init__(self, database, uid):
        self.__uid = uid
        self.__database = database
    
    def export(self, name, exam, minutes, points):
        if not(self.__database.existExam(name)):
            self.__database.insertExam(name, exam, minutes, points)
            return True
        return False













'''   
    def __checkAnswer__(self, user, answer):
        answers = list(self.users[user]["current"][1])
        return answers[0] == answer

    def __shiftQuestion__(self, user):
        if not(self.users[user]["quiz"]):
            return False
        key = choice(list(self.users[user]["quiz"].keys()))
        value = self.users[user]["quiz"][key]
        del self.users[user]["quiz"][key]
        self.users[user]["current"] = (key, value)
        return self.users[user]["current"]
    
    def getUsers(self):
        return self.users.keys()

    def getUserInfo(self, user):
        return {
            "still": len(self.users[user]["quiz"]),
            "done": self.users[user]["done"],
            "current": self.users[user]["current"],
            "points": self.users[user]["points"]
        }

    def getQuestion(self, user):
        if not(self.__checkUser__(user)):
            self.__addUser__(user)
            self.__shiftQuestion__(user)
        current = self.users[user]["current"]
        return Point(current)
    
    def sendAnswer(self, user, answer):
        if not(self.__checkUser__(user)):
            return "The user didn't start the test."
        if not(self.__shiftQuestion__(user)):
            return "The quiz is finished."
        if self.__checkAnswer__(user, answer):
            self.users[user]["points"] += 1
        self.users[user]["done"] += 1
        return True
  

class Point():

    def __init__(self, item=None):
        self.item = tuple(item)

    def question(self):
        return self.item[0]

    def answers(self):
        answers = list(self.item[1])
        shuffle(answers)
        return answers

    def __answer__(self):
        return self.item[1][0]
''' 