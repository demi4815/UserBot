import json
import time

import pandas


class Constants:

    def __init__(self):
        self.__appHash = "APP'S HASH"
        self.__appId = 1234567890
        self.__botLog = -1001234567890
        self.__botAdmins = None
        self.__chat = None
        self.__creator = 0
        self.__phoneNumber = "PHONE NUMBER WITH THE INTERNATIONAL CODE AND WITHOUT THE +"

    @property
    def admins(self) -> pandas.DataFrame:
        return self.__botAdmins

    @property
    def creator(self) -> int:
        return self.__creator

    @property
    def chats(self) -> pandas.DataFrame:
        return self.__chat

    @chats.setter
    def chats(self, chat: dict):
        self.__chat = self.__chat.append(chat, ignore_index=True)

    @property
    def hash(self) -> str:
        return self.__appHash

    @property
    def id(self) -> int:
        return self.__appId

    def loadCreators(self):
        with open("database.json", "r") as users:
            users = json.load(users)
        self.__botAdmins = pandas.DataFrame(data=users["admins"], columns=list(["id", "name"]))
        self.__chat = pandas.DataFrame(data=users["chat"], columns=list(["id", "name"]))
        rows = self.__botAdmins.shape[0]
        rows = range(rows)
        for i in rows:
            if self.__botAdmins.at[i, "name"] == "":
                self.__creator = self.__botAdmins.at[i, "id"]

    @property
    def log(self) -> int:
        return self.__botLog

    @staticmethod
    def now() -> str:
        timer = time.localtime()
        return "{0}:{1}:{2} of {3}-{4}-{5}".format(timer.tm_hour, timer.tm_min, timer.tm_sec,
                                                   timer.tm_mday, timer.tm_mon, timer.tm_year)

    @property
    def phoneNumber(self) -> str:
        return self.__phoneNumber
