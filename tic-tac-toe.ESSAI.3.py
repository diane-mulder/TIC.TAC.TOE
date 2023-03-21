from tkinter import *

root = Tk()
root.title("TIC TAC TOE")

X_wins = 0
O_wins = 0
X_turn = True
game_over = False

def newGame():
    global X_turn, game_over

    b1["text"] = ""
    b2["text"] = ""
    b3["text"] = ""
    b4["text"] = ""
    b5["text"] = ""
    b6["text"] = ""
    b7["text"] = ""
    b8["text"] = ""
    b9["text"] = ""

    b1["bg"] = "white"
    b2["bg"] = "white"
    b3["bg"] = "white"
    b4["bg"] = "white"
    b5["bg"] = "white"
    b6["bg"] = "white"
    b7["bg"] = "white"
    b8["bg"] = "white"
    b9["bg"] = "white"

    X_turn = True
    status_label["text"] = "X's Turn"
    game_over = False


newGameButton = Button(text="NEW GAME", command=newGame)
status_label = Label(text="X's Turn")
score_label = Label(text="X:[] O:[]".format(X_wins, O_wins))

newGameButton.grid(row=0, column=0)
newGameButton.grid(row=0, column=1)
newGameButton.grid(row=0, column=2)


def checkGame_status(X_turn):
    if(X_turn):
        check = "X"
    else : 
        check = "O"
# 3 lignes
    if(b1["text"] == b2["text"] == b3["text"] == check):
        return b1,b2,b3
    if(b4["text"] == b5["text"] == b6["text"] == check):
        return b4,b5,b6
    if(b7["text"] == b8["text"] == b9["text"] == check):
        return b7,b8,b9
# 3 colonnes
    if(b1["text"] == b4["text"] == b7["text"] == check):
        return b1,b4,b7
    if(b2["text"] == b5["text"] == b8["text"] == check):
        return b2,b5,b8
    if(b3["text"] == b6["text"] == b9["text"] == check):
        return b3,b6,b9
# 2 diagonales
    if(b1["text"] == b5["text"] == b9["text"] == check):
        return b1,b5,b9
    if(b3["text"] == b5["text"] == b7["text"] == check):
        return b3,b5,b7
    
    return None



def on_click(button):
    global X_turn, game_over, X_wins, O_wins
    if(button["text"] !="" or game_over):
        return
    button["text"] = "X" if X_turn else "O"
    b=checkGame_status(X_turn)
    if(b != None):
        b[0]["bg"] = "green"
        b[1]["bg"] = "green"
        b[2]["bg"] = "green"
        if(X_turn):
            status_label["text"] = "X wins"
            X_wins += 1
        else:
            status_label["text"] = "O wins"
            O_wins += 1
            score_label["text"] = "X:[] O:[]".format(X_wins, O_wins)
            game_over = True
            return
        X_turn = not X_turn
        status_label["text"] = "X's Turn" if X_turn else "O's Turn"


b1 = Button(width=10, height=5, bg="white", command=lambda: on_click(b1))
b2 = Button(width=10, height=5, bg="white", command=lambda: on_click(b2))
b3 = Button(width=10, height=5, bg="white", command=lambda: on_click(b3))

b4 = Button(width=10, height=5, bg="white", command=lambda: on_click(b4))
b5 = Button(width=10, height=5, bg="white", command=lambda: on_click(b5))
b6 = Button(width=10, height=5, bg="white", command=lambda: on_click(b6))

b7 = Button(width=10, height=5, bg="white", command=lambda: on_click(b7))
b8 = Button(width=10, height=5, bg="white", command=lambda: on_click(b8))
b9 = Button(width=10, height=5, bg="white", command=lambda: on_click(b9))

b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)




root.mainloop()


