import json
import time
import subprocess

import pandas


class Constants:

	def __init__(self):
		self.__appHash = "HASH"
		self.__appId = 0
		self.__botLog = 0
		self.__botAdmins = None
		self.__chat = None
		self.__creator = 0
		self.__phoneNumber = "PHONE NUMBER WITH PREFIX AND WITHOUT +"

	@property
	def admins(self) -> pandas.DataFrame:
		return self.__botAdmins

	@admins.setter
	def admins(self, newAdmin: dict):
		self.__botAdmins = self.__botAdmins.append(newAdmin, ignore_index=True)
		element = "{\"admins\":" + self.__botAdmins.to_json(orient="records").replace("\":", "\": ").replace(",\"", ", \"") + ",\"chat\":" + \
				  self.__chat.to_json(orient="records").replace("\":", "\": ").replace(",\"", ", \"") + "}"
		"""
			Saving the database
		"""
		pwd = str(subprocess.check_output("pwd", shell=True))
		pwd = pwd.replace("b\'", "")
		pwd = pwd.replace("\\n\'", "")
		if pwd == "/":
			path = "home/USER/Documents/gitHub/UserBot/database.json"
		elif pwd == "/home":
			path = "USER/Documents/gitHub/UserBot/database.json"
		elif pwd == "/home/USER":
			path = "Documents/gitHub/UserBot/database.json"
		elif pwd == "/home/USER/Documents":
			path = "gitHub/UserBot/database.json"
		elif pwd == "/home/USER/Documents/gitHub":
			path = "UserBot/database.json"
		elif pwd == "/root":
			path = "/home/USER/Documents/gitHub/UserBot/database.json"
		elif pwd == "/data/data/com.termux/files/home":
			path = "downloads/UserBot/database.json"
		elif pwd == "/data/data/com.termux/files/home/downloads":
			path = "UserBot/database.json"
		else:
			path = "database.json"
		with open(path, "w") as users:
			users.write(element)

	@admins.deleter
	def admins(self):
		self.__botAdmins = pandas.DataFrame(data=dict(), columns=list(["id", "is_self", "is_contact",
																	   "is_mutual_contact", "is_deleted",
																	   "is_bot", "is_verified", "is_restricted",
																	   "is_scam", "is_support", "first_name",
																	   "last_name", "username", "language_code",
																	   "phone_number"]))
		element = "{\"admins\": [],\"chat\":" + self.__chat.to_json(orient="records").replace("\":", "\": ").replace(",\"", ", \"") + "}"
		"""
			Saving the database
		"""
		pwd = str(subprocess.check_output("pwd", shell=True))
		pwd = pwd.replace("b\'", "")
		pwd = pwd.replace("\\n\'", "")
		if pwd == "/":
			path = "home/USER/Documents/gitHub/UserBot/database.json"
		elif pwd == "/home":
			path = "USER/Documents/gitHub/UserBot/database.json"
		elif pwd == "/home/USER":
			path = "Documents/gitHub/UserBot/database.json"
		elif pwd == "/home/USER/Documents":
			path = "gitHub/UserBot/database.json"
		elif pwd == "/home/USER/Documents/gitHub":
			path = "UserBot/database.json"
		elif pwd == "/root":
			path = "/home/USER/Documents/gitHub/UserBot/database.json"
		elif pwd == "/data/data/com.termux/files/home":
			path = "downloads/UserBot/database.json"
		elif pwd == "/data/data/com.termux/files/home/downloads":
			path = "UserBot/database.json"
		else:
			path = "database.json"
		with open(path, "w") as users:
			users.write(element)

	@property
	def creator(self) -> int:
		return self.__creator

	@property
	def chats(self) -> pandas.DataFrame:
		return self.__chat

	@chats.setter
	def chats(self, newChat: dict):
		self.__chat = self.__chat.append(newChat, ignore_index=True)
		element = "{\"admins\":" + self.__botAdmins.to_json(orient="records").replace("\":", "\": ").replace(",\"", ", \"") + ",\"chat\":" + \
				  self.__chat.to_json(orient="records").replace("\":", "\": ").replace(",\"", ", \"") + "}"
		"""
			Saving the database
		"""
		pwd = str(subprocess.check_output("pwd", shell=True))
		pwd = pwd.replace("b\'", "")
		pwd = pwd.replace("\\n\'", "")
		if pwd == "/":
			path = "home/USER/Documents/gitHub/UserBot/database.json"
		elif pwd == "/home":
			path = "USER/Documents/gitHub/UserBot/database.json"
		elif pwd == "/home/USER":
			path = "Documents/gitHub/UserBot/database.json"
		elif pwd == "/home/USER/Documents":
			path = "gitHub/UserBot/database.json"
		elif pwd == "/home/USER/Documents/gitHub":
			path = "UserBot/database.json"
		elif pwd == "/root":
			path = "/home/USER/Documents/gitHub/UserBot/database.json"
		elif pwd == "/data/data/com.termux/files/home":
			path = "downloads/UserBot/database.json"
		elif pwd == "/data/data/com.termux/files/home/downloads":
			path = "UserBot/database.json"
		else:
			path = "database.json"
		with open(path, "w") as users:
			users.write(element)

	@chats.deleter
	def chats(self):
		self.__chat = pandas.DataFrame(data=dict(), columns=list(["id", "type", "is_verified", "is_restricted",
																  "is_scam", "is_support", "title", "username",
																  "first_name", "last_name", "invite_link"]))
		element = "{\"admins\":" + self.__botAdmins.to_json(orient="records").replace("\":", "\": ").replace(",\"", ", \"") + ",\"chat\": []}"
		"""
			Saving the database
		"""
		pwd = str(subprocess.check_output("pwd", shell=True))
		pwd = pwd.replace("b\'", "")
		pwd = pwd.replace("\\n\'", "")
		if pwd == "/":
			path = "home/USER/Documents/gitHub/UserBot/database.json"
		elif pwd == "/home":
			path = "USER/Documents/gitHub/UserBot/database.json"
		elif pwd == "/home/USER":
			path = "Documents/gitHub/UserBot/database.json"
		elif pwd == "/home/USER/Documents":
			path = "gitHub/UserBot/database.json"
		elif pwd == "/home/USER/Documents/gitHub":
			path = "UserBot/database.json"
		elif pwd == "/root":
			path = "/home/USER/Documents/gitHub/UserBot/database.json"
		elif pwd == "/data/data/com.termux/files/home":
			path = "downloads/UserBot/database.json"
		elif pwd == "/data/data/com.termux/files/home/downloads":
			path = "UserBot/database.json"
		else:
			path = "database.json"
		with open(path, "w") as users:
			users.write(element)

	@property
	def hash(self) -> str:
		return self.__appHash

	@property
	def id(self) -> int:
		return self.__appId

	def loadCreators(self):
		"""
			Reading the database
		"""
		pwd = str(subprocess.check_output("pwd", shell=True))
		pwd = pwd.replace("b\'", "")
		pwd = pwd.replace("\\n\'", "")
		if pwd == "/":
			path = "home/USER/Documents/gitHub/UserBot/database.json"
		elif pwd == "/home":
			path = "USER/Documents/gitHub/UserBot/database.json"
		elif pwd == "/home/USER":
			path = "Documents/gitHub/UserBot/database.json"
		elif pwd == "/home/USER/Documents":
			path = "gitHub/UserBot/database.json"
		elif pwd == "/home/USER/Documents/gitHub":
			path = "UserBot/database.json"
		elif pwd == "/root":
			path = "/home/USER/Documents/gitHub/UserBot/database.json"
		elif pwd == "/data/data/com.termux/files/home":
			path = "downloads/UserBot/database.json"
		elif pwd == "/data/data/com.termux/files/home/downloads":
			path = "UserBot/database.json"
		else:
			path = "database.json"
		with open(path, "r") as users:
			files = json.load(users)
			"""
		Setting the database
		"""
			self.__botAdmins = pandas.DataFrame(data=files["admins"], columns=list(["id", "is_self", "is_contact",
																					"is_mutual_contact", "is_deleted",
																					"is_bot", "is_verified", "is_restricted",
																					"is_scam", "is_support", "first_name",
																					"last_name", "username", "language_code",
																					"phone_number"]))
			self.__chat = pandas.DataFrame(data=files["chat"], columns=list(["id", "type", "is_verified", "is_restricted",
																			 "is_scam", "is_support", "title", "username",
																			 "first_name", "last_name", "invite_link"]))
		"""
			Setting the parameters
		"""
		rows = self.__botAdmins.shape[0]
		rows = range(rows)
		for i in rows:
			if self.__botAdmins.at[i, "username"] == "USERNAME":
				self.__creator = int(self.__botAdmins.at[i, "id"])

	@property
	def log(self) -> int:
		return self.__botLog

	@staticmethod
	def now() -> str:
		timer = time.localtime()
		return "{}:{}:{} of {}-{}-{}".format(timer.tm_hour, timer.tm_min, timer.tm_sec,
											 timer.tm_mday, timer.tm_mon, timer.tm_year)

	@property
	def phoneNumber(self) -> str:
		return self.__phoneNumber
