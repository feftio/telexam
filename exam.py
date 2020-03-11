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
    
    def _exist_(self):
        pass

    def create(self, table, fields):
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS {}({})".format(table, fields))
        self.connection.commit()

    def insert(self, query, values):
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        cursor.close()

class ExamDatabase(Database):

    def __init__(self, path="exam.db"):
        super().__init__(path)
        self.create("users", "id integer PRIMARY KEY, name text, date date")
        self.create("currents", "id integer, questions json, done json, start date, finish date")

    def insertUser(self, *args):
        self.insert("INSERT INTO users(id, name, date) VALUES(?, ?, ?)", list(args))

    def insertCurrent(self, *args):
        self.insert("INSERT INTO currents(id, questions, done, start, finish) VALUES(?, ?, ?, ?, ?)", list(args))

class Exam:

    def __init__(self, quiz={}, path="exam.db"):
        self.questions = dict(quiz["questions"])
        self.options = dict(quiz["options"])
        self.database = ExamDatabase(path)

    def __addUser__(self, user):
        start = datetime.now()
        finish = start + timedelta(minutes=self.options["time"])
        self.database.insertUser(user, json.dumps(dict(self.questions)), json.dumps({}), start, finish)

    def __checkUser__(self, user):

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