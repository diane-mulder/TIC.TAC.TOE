from tkinter import *
from tkinter import messagebox


count=0
board=[['','','',],
        ['','','',],
        ['','','',]]


# Chaque fois que le joueur selectionne l'option "quitter", ce message s'affiche: 
def Quit():
    global t    
    msg=messagebox.askquestion("Confirmez","Voulez-vous quitter le jeu? Vous avez une nouvelle chance!")
    if msg=='oui': 
        t.destroy()

# Détruit la fenêtre du gagnant et la fenêtre du jeu
def destruct():
    global t,winnerWindow
    t.destroy()
    winnerWindow.destroy()

    

# Afficher une fenetre pour annoncer la gagnat ou match nul : 
def displayWinner(winner):
    global t,winnerWindow,ID    
    winnerWindow=Tk()
    winnerWindow.title("jeu gagnant")
    winnerWindow.configure(bg="green")
    l1=Label(winnerWindow,text="LE GAGNANT EST: ",font=("ARIAL BLACK",12),bg="green",fg="black")
    l1.pack()
    l2=Label(winnerWindow,text=winner,font=("ARIAL BLACK",20),bg="green",fg="black")
    l2.pack()
    bproceed=Button(winnerWindow,text="QUITTER",font=("ARIAL BLACK",10,"bold"),command=destruct)
    bproceed.pack()

# Conditions pour le gagnant :       
def checkWinner():
    global count,board
    if (board[0][0]==board[0][1]==board[0][2]=="X" or board[1][0]==board[1][1]==board[1][2]=="X" or board[2][0]==board[2][1]==board[2][2]=="X" or
        board[0][0]==board[1][0]==board[2][0]=="X" or board[0][1]==board[1][1]==board[2][1]=="X" or board[0][2]==board[1][2]==board[2][2]=="X" or
        board[0][0]==board[1][1]==board[2][2]=="X" or board[0][2]==board[1][1]==board[2][0]=="X"):
            displayWinner("Player X")
    elif (board[0][0]==board[0][1]==board[0][2]=="O" or board[1][0]==board[1][1]==board[1][2]=="O" or board[2][0]==board[2][1]==board[2][2]=="O" or
          board[0][0]==board[1][0]==board[2][0]=="O" or board[0][1]==board[1][1]==board[2][1]=="O" or board[0][2]==board[1][2]==board[2][2]=="O" or
          board[0][0]==board[1][1]==board[2][2]=="O" or board[0][2]==board[1][1]==board[2][0]=="O"):
            displayWinner("Player O")
    elif count==9:
        displayWinner("MATCH NUL!!!")

# Changer les valeurs des boutons
def changeVal(button,boardValRow,boardValCol):
    global count

    # vérifier que les boutons sont dispo
    if button["text"]=="":
        if count%2==0:
            button["text"]="X"
            l1=Label(t,text="JOUEUR.2(O)",height=3,font=("ARIAL BLACK",10,"bold"),bg="blue").grid(row=0,column=0)
            board[boardValRow][boardValCol]="X"
        else:
            button["text"]="O"
            l1=Label(t,text="JOUEUR.1(X)",height=3,font=("ARIAL BLACK",10,"bold"),bg="red").grid(row=0,column=0)
            board[boardValRow][boardValCol]="O"
        count=count+1
        if count>=5:
            checkWinner()
    else:
        messagebox.showerror("ERREUR","CETTE CASE N'EST PLUS DISPONIBLE!")

# afficher l'interface graphique (GUI : Graphical User Interface)
def TicTacToeGUI():
    global t
    t=Tk()
    t.title("JEU DU TIC.TAC.TOE")
    t.configure(bg="white") 
    

    # afficher le joueur
    l1=Label(t,text="PLAYER: 1(X)",height=3,font=("ARIAL BLACK",10,"bold"),bg="white")
    l1.grid(row=0,column=0)

    # bouton quitter : 
    exitButton=Button(t,text="QUITTER",command=Quit,font=("ARIAL BLACK",8,"bold"), bg="grey")
    exitButton.grid(row=0,column=2)

    
    # la grille des boutons : 
    b1=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b1,0,0))
    b2=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b2,0,1))
    b3=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b3,0,2))
    b4=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b4,1,0))
    b5=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b5,1,1))
    b6=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b6,1,2))
    b7=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b7,2,0))
    b8=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b8,2,1))
    b9=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b9,2,2))

    b1.grid(row=2,column=0)
    b2.grid(row=2,column=1)
    b3.grid(row=2,column=2)

    b4.grid(row=3,column=0)
    b5.grid(row=3,column=1)
    b6.grid(row=3,column=2)

    b7.grid(row=4,column=0)
    b8.grid(row=4,column=1)
    b9.grid(row=4,column=2)



TicTacToeGUI()

mainloop()