import tkinter as tk
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.board = [" "] * 9
        self.current_player = "X"
        self.create_widgets()

    def create_widgets(self):
        # Creation des boutons pour la planche de jeu
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, text=" ", font=("Arial black", 30), width=4, height=2,
                               command=lambda i=i: self.play_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        # Créer l'affichage du statut du jeu
        self.status_label = tk.Label(self.master, text="JOUEUR X", font=("Arial black", 16))
        self.status_label.grid(row=3, column=0, columnspan=3)

    def play_move(self, i):
        # Verifier si le jeu est terminé : 
        if self.check_game_over():
            return

        # verifier si le mode selectionné est valide : 
        if self.board[i] != " ":
            return

        # mettre à jour le tableau de jeu et le texte des boutons : 
        self.board[i] = self.current_player
        self.buttons[i].config(text=self.current_player)

        # vérifier si le jeu est fini après  :
        if self.check_game_over():
            return

        # changer de joueur : 
        self.current_player = "X" if self.current_player == "O" else "O"
        self.status_label.config(text="AU TOUR DU JOUEUR {}".format(self.current_player))

        # Si c'est au tour de l'ordianateur : faire jouer
        if self.current_player == "O":
            i = self.ia(self.board, "O")
            if i is not False:
                self.play_move(i)

    def check_game_over(self):
        # pour le combinasons gagnantes :  
        for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                self.status_label.config(text="JOUEUR {} A GAGNE!".format(self.board[a]))
                return True

        # Check for a tie game
        if " " not in self.board:
            self.status_label.config(text="MATCH NUL!")
            return True

        return False

    def ia(self, board, signe):
        # verifier si l'ordianateur peut gagner : 
        for i in range(9):
            if board[i] == " ":
                board_copy = board[:]
                board_copy[i] = signe
                if self.check_win(board_copy, signe):
                    return i

        # verifier si le joueur peut gagner : 
        other_signe = "X" if signe == "O" else "O"
        for i in range(9):
            if board[i] == " ":
                board_copy = board[:]
                board_copy[i] = other_signe
                if self.check_win(board_copy, other_signe):
                    return i

        # choisir un coup au hazard : 
        while True:
            i = random.randint(0, 8)
            if board[i] == " ":
                return i
            
    def check_win(self, board, signe):
        # vérifier pour une combinaison gagnante : 
        for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if board[a] == board[b] == board[c] == signe:
                return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    root.title("JEU : TIC TAC TOE")
    TicTacToe(root)

    root.mainloop()        