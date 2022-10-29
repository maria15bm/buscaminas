from tkinter import *
import cons_bm as cons
from board import Board

class Controller:
	''' Define la pantalla de selección de nivel. '''
	def __init__(self):
		self.__screen = None
		self.select_dificulty()

	def select_dificulty(self):
		self.__screen = Tk()
		buttonframe = Frame(self.__screen)
		buttonframe.grid(row=3, column=3, padx=5)
		self.__screen.title = 'buscaminas'
		difficulty = Label(buttonframe, text='Elige la dificultad.', pady=10)
		difficulty.config(font=("Calibri", 18))
		# modo fácil
		easy = Button(buttonframe, text='Fácil',pady=5,command=lambda rows=cons.EASY_VALS[0], 
			cols=cons.EASY_VALS[1], mines=cons.EASY_VALS[2]: self.start_game(rows, cols, mines))
		easy.config(font=("Arial", 12))
		# modo medio
		medium = Button(buttonframe, text='Medio',pady=5, command=lambda rows=cons.MEDIUM_VALS[0], 
			cols=cons.MEDIUM_VALS[1], mines=cons.MEDIUM_VALS[2]: self.start_game(rows, cols, mines))
		medium.config(font=("Arial", 12))
		# modo difícil
		hard = Button(buttonframe, text='Difícil',pady=5,command=lambda rows=cons.HARD_VALS[0], 
			cols=cons.HARD_VALS[1], mines=cons.HARD_VALS[2]: self.start_game(rows, cols, mines))
		hard.config(font=("Arial", 12))
		# botón de salir
		quit = Button(buttonframe, text='Cerrar', pady=5,command=self.__screen.destroy)
		quit.config(font=("Arial", 12), bg='#eb402d')
		difficulty.grid(row=0, column=0, columnspan=3, pady=10)
		easy.grid(row=1, column=0, pady=5)
		medium.grid(row=1, column=1, pady=5)
		hard.grid(row=1, column=2, pady=5)
		quit.grid(row=2, column=0, columnspan=3, pady=10)
		self.__screen.mainloop()

	def start_game(self, rows, cols, mines):
		self.__screen.destroy()
		self.__screen = Board(rows, cols, mines)
		self.select_dificulty()


if __name__ == "__main__":
	board = Controller()

