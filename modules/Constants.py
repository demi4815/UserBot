import time

import pandas


class Constants:

	def __init__(self):
		self.__appHash = "HASH"
		self.__appId = 0
		self.__botUsername = "UserBot"
		self.__creator = 0
		self.__phoneNumber = "PHONE NUMBER WITH PREFIX AND WITHOUT +"

	@property
	def creator(self) -> int:
		return self.__creator

	@property.setter
	def creator(self, ID: int):
		self.__creator = ID

	@property.deleter
	def creator(self):
		self.__creator = 0

	@property
	def hash(self) -> str:
		return self.__appHash

	@property
	def id(self) -> int:
		return self.__appId

	@staticmethod
	def now() -> str:
		timer = time.localtime()
		return "{}:{}:{} of {}-{}-{}".format(timer.tm_hour, timer.tm_min, timer.tm_sec,
											 timer.tm_mday, timer.tm_mon, timer.tm_year)

	@property
	def phoneNumber(self) -> str:
		return self.__phoneNumber

	@property
	def username(self) -> str:
		return self.__botUsername
