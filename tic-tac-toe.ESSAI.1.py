import tkinter
import tkinter as tk #importer le nom du module
from tkinter import font # servira plus tard à mofifier la police

class TicTacToeBoard(tk.Tk):

    def _init_(self): # méthode de la superclasse pour initialiser la classe parent 
        super()._init_() # utiliser la fonction intégrée
        self.title("Tic-Tac-Toe Game") # titre du jeu : chaine
        self._cells = {} # non public, contient un dictionnaire : il mappera les boutons ou les cellules du plateau
        self._create_board_display()
        self._create_board_grid()


    def create_board_display(self): # creation d'un tableau d'affichage
        display_frame = tk.Frame(master=self) # crée un Frameobjet pour contenir l'affichage du jeu
        display_frame.pack(fill=tk.X) # gestionnaire de géométrie pour placer l'objet cadre sur la bordure supérieure de la fenêtre principale
        self.display = tk.Label(master=display_frame, text="Le jeu va commencer!", font=font.font(size=28, weight="bold",))
        self.diplay.pack()

    def create_board_grid(self): # créer la grille des cellules
        grid_frame = tk.Frame(master=self) # créer l'objet pour contenir la grille de cellules du jeu
        grid_frame.frame.pack()
        for row in range(3): # definir 3 lignes
            self.rowconfigure(row, weiht=1, minsize=75) # ses dimensions
            for col in range(3): # definir les 3 colonnes
                button = tk.Button(master=grid_frame, text="", font=font.Font(size=36, weight="bold"), fg="black",width=3, height=2, highlightbackground="lightblue",)
            self._cells[button] = (row, col) # ajoute chaque nouveau bouton au ._cellsdictionnaire
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew") # grid = gestionnaire de geometrie


TicTacToeBoard.mainloop











# def main():
#     board = TicTacToeBoard()
#     board.mainloop()

# if_name_ == "_main_":

# main()
    


    # def main():
    #     board = TicTacToeBoard()
    #     board.mainloop()








# window = tk.Tk()
# frame = tk.Frame()
# frame.pack()

# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=1)
#         frame.grid(ligne=i, colonne = j)
#     label = tk.Label(master=frame)
#     label.pack()


# window.mainloop()

