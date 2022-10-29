from tkinter import *

class Casilla:
	""" docstring for Casilla """
	def __init__(self, row, col, root):
		self.__row = row # row of the case
		self.__col = col # column of the case
		self.__active = False # if it has been clicked
		self.__value = 0 # -1 if it is a mine or the number of mines surrounding it if it isn't
		self.__flag = False # if it has been marked by a flag
		self.__text = self.define_text()
		self.__graphics = Label(root, text=self.__text , borderwidth=2, relief="raised")
		
	def update_text(self):
		self.define_text()
		self.__graphics["text"] = self.__text

	@property
	def row(self):
		return self.__row

	@property
	def col(self):
		return self.__col

	@property
	def graphics(self):
		return self.__graphics

	@property
	def value(self):
		return self.__value

	@value.setter
	def value(self, val):
		if val in range(-1, 9):
			self.__value = val

	@property
	def active(self):
		return self.__active


	@active.setter
	def active(self, val):
		if val == True:
			self.__active = True
		else:
			self.__active = False


	def define_text(self):
		if self.__active == False and self.__flag:
			self.__text = ' F '
			
		elif self.__active and self.__value == -1:
			self.__text = " ● "

		elif self.__active and self.__value>-1:
			self.__text = " " + str(self.__value) + " "
		else:
			self.__text = "    "

	def put_flag(self):
		if not self.__active:
			self.__flag = not self.__flag
			self.update_text()

	def active_cell(self):
		if not self.__active and not self.__flag:
			self.__active = True
			self.update_text()

	def check_lost(self):
		if self.__active and self.__value == -1:
			return True
		return False

	


		