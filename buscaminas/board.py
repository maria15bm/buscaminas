from random import randrange
from tkinter import *
from tkinter import messagebox as mb
from mina import Casilla
import cons_bm as cons

class Board:
	def __init__(self, rows: int, cols: int, minas: int):
		self.__rows = rows # número de filas
		self.__cols = cols # número de columnas
		self.__root = Tk()
		self.__root.title = 'buscaminas'
		self.__mines = minas # número de minas
		self.__mines_list = self.__define_mines() # list of mines positions
		self.__board = self.__generate_board() # tablero
		self.__active_num = 0
		self.__define_values() # define the numerical value for each case.
		self.__define_graphs() # define the graphical board
		self.binding()
		self.__root.mainloop()
		

	def __define_mines(self):
		""" defines the positions of the mines """
		mines_list = []
		for i in range(self.__mines):
			limit = self.__cols * self.__rows # max position is the last case in the board
			number = randrange(0, limit)
			while number in mines_list:
				number = randrange(0, limit)
			mines_list.append(number) # The mines are in random positions.
		return mines_list

	def __generate_board(self):
		""" Generates the list of cases that will form the board."""
		board = []
		counter = 0
		for row in range(self.__rows):
			for col in range(self.__cols):
				case = Casilla(row, col, self.__root)
				if counter in self.__mines_list:
					# If a mine should be in a case we set its value to -1.
					case.value = -1
				board.append(case)
				counter+=1
		return board

	def __define_values(self):
		""" defines the value atribute for each case """
		for case in self.__board:
			# for each mined case
			if case.value == -1:
				colindantes = self.colindantes(case.row, case.col)
				for col_case in colindantes:
					# If there is already a mine in a colindant case we cannot increase its value.
					if col_case.value != -1:
						# If the colindant case is not mined we increase its value.
						col_case.value+=1


	def search_case(self, row: int, col: int):
		""" returns a case in a board given its row and its column"""
		for case in self.__board:
			if case.row == row and case.col == col:
				return case
		return -1

	def colindantes(self, row: int, col: int):
		""" returns a list of cases with the colindants of a case """
		colindants = []
		coordinates = ((row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1),
			(row+1, col-1), (row+1, col), (row+1, col+1))
		for coordinate in coordinates:
			case = self.search_case(coordinate[0], coordinate[1])
			if case != -1:
				colindants.append(case)
		return colindants

	def __define_graphs(self):
		""" builds the grid for the board """
		for case in self.__board:
			case.update_text()
			case.graphics.grid(pady = 2, padx = 2, row = case.row, column = case.col)

	def binding(self):
		for case in self.__board:
			case.graphics.bind("<Button-1>", lambda event, case = case: self.active_cell(case))
			case.graphics.bind("<Button-3>", lambda event, case = case: self.put_flag(case))

	def active_cell(self, case):
		case.active_cell()
		if case.check_lost():
			for cell in self.__board:
				cell.active = True
				cell.update_text()
			mb.showinfo(message="Has perdido", title=":(")
			self.__root.destroy()
		else:
			if case.value == 0:
				self.reveal_colindants(case)
			non_mined = len(self.__board)-self.__mines
			if self.__active_num == non_mined:
				mb.showinfo(message="Has ganado", title=":)")
				self.__root.destroy()

	def reveal_colindants(self, case):
		case.active_cell()
		self.__active_num+=1
		if case.value == 0:
			colindantes = self.colindantes(case.row, case.col)
			for i in colindantes:
				if i.active == False:
					self.reveal_colindants(i)
		return False


	def put_flag(self, case):
		case.put_flag()

	def show_cells(self):
		print('checking...')
		return True







