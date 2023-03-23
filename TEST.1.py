from tkinter import *
import random
    
global player

def nextTurn(row, column):

    

    if buttons[row][column]["text"] == "" and checkWinner() is False:
        if player[X] == player[0]: 
            buttons[row][column]["text"] = player
            if checkWinner() is False:
                players=players[1]
                Label.config(text=(players[1]+"turn"))
        elif checkWinner() is True:
            Label.config(text=(players[0]+"wins"))
        elif checkWinner() == "tie":
            Label.config(text=("Tie!"))
    else : 
        buttons[row][column]["text"] = player

        if checkWinner() is False:
            players=players[0]
            Label.config(text=(players[0]+"turn"))
        elif checkWinner() is True:
            Label.config(text=(players[1]+"wins"))
        elif checkWinner() == "tie":
            Label.config(text=("Tie!"))


def checkWinner():
    
    for row in range(3):
        if buttons [row][0]["text"] == buttons [row][1]["text"] == buttons [row][2]["text"] !="":
           return True 
    for column in range(3):
        if buttons [0][column]["text"] == buttons [1][column]["text"] == buttons [2][column]["text"] !="":
           return True 
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] !="":
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] !="":
        return True  
    elif emptySpaces() is False:
        return "Tie"
    else : 
        return False



def emptySpaces():
    pass
    # spaces = 9

    # for row in range(3):
    #     for column  

def newGame():
    pass

window = Tk()
window.title("tic-tac-toe")
players = ["X", "0"]
player = random.choice(players)
buttons =  [[0,0,0],
            [0,0,0],
            [0,0,0]]

Label = Label(text=player + "turn", font=('consolas',40))
Label.pack(side="top")

reset_button = Button(text="restart", font=('consolas',20), command=newGame)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas',40), width=5, height=2, command=lambda row=row, column=column: nextTurn(row, column))                          
        buttons[row][column].grid(row=row, column=column)


window.mainloop()