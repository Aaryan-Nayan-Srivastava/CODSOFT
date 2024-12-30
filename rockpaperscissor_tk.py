from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Rock Paper Scissor!!")
window.geometry("400x200")

l = Label(window, text="Welcome To The Rock Paper Scissor Game", font=("Helvetica", 12, "bold"), fg="blue", bg="lightyellow",bd=5)
l.pack()
#function for result
def results(user,computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or\
         (user == "paper" and computer == "rock") or\
         (user == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"
points=0
#function
def rps(user):
    import random
    global points 
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    result=results(user,computer)
    messagebox.showinfo("Result", f"Your choice: {user}\nComputer's choice: {computer}\n\nResult:{result}!")
    
    if result=="win":
        points+=1
        
    elif result=="lose":
        points-=1
        
    score_l.config(text=f"Score:{points}")

#Buttons for rock,paper and scissors 
b1=Button(window,text="Rock",width=12, height=3,command=lambda:rps("rock"))
b1.place(x=60,y=60)
b2=Button(window,text="Paper",width=12, height=3,command=lambda:rps("paper"))
b2.place(x=150,y=60)
b3=Button(window,text="Scissors",width=12, height=3,command=lambda:rps("scissors"))
b3.place(x=240,y=60)
#score (it'll change after every game)
score_l =Label(window, text="Score: 0", font=("Helvetica", 12))
score_l.place(x=150,y=150)


window.mainloop()