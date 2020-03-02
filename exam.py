from random import shuffle, choice, randint
import sqlite3
from sqlite3 import Error

class Database:

    def __init__(self, path="exam.db"):
        try:
            self.connection = sqlite3.connect(path)
            print("Connection is established: Database is created in memory")
        except Error:
            print(Error)
        finally:
            self.connection.close()
    
    def __exist__(self, table):
        cursor = self.connection.cursor()
        cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}'".format(table))
        if cursor.fetchone()[0] == 1: 
            return True
        return False

    def create(self):
        if self.__exist__("users"):
            cursor = self.connection.cursor()
            cursor.execute("CREATE TABLE users(id integer PRIMARY KEY, quiz text, done text, start date, finish date)")
            self.connection.commit()

    def insert(self, data):
        cursor = self.connection.cursor()
        cursor.execute(data)
        self.connection.commit()


class Exam:

    def __init__(self, quiz=None):
        self.quiz = dict(quiz)
        self.database = Database("exam.db").create()

    def __addUser__(self, user):
        self.database.insert("INSERT INTO users(id, quiz, done, start, finish) VALUES({}, {}, {}, {}, {})".format(
            user, 
            dict(self.quiz),
            {},
            
            )

    def __checkUser__(self, user):
        if self.users and user in self.users:
            return True
        return False
    
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

class Point:

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
