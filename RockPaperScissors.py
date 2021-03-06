import tkinter as tk
import tkinter 
from tkinter import messagebox
import random



# Developer : Hamdy Abou El Anein

top = tk.Tk() 
top.title("Rock - Paper - Scissor")

ciseaux_tk = tk.PhotoImage(file="./images/scissors.gif")
caillou_tk = tk.PhotoImage(file="./images/rock.gif")
feuille_tk = tk.PhotoImage(file="./images/paper.gif")


user_score = 0
comp_score = 0
def Rock():
    global user_score, comp_score
    
    comp = random.randint(1,3)

    if comp == 3:
        comp = "Scissors"
        user_score+=1
        messagebox.showinfo("Congratulation!", "YOU WIN!\n"+"Your Choice:Rock"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    elif comp==1:
        comp = "Rock"
        messagebox.showinfo("Same choice!", "EGUALITY!\n"+"Your Choice:Rock"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
        
    else:
        comp = "Paper"
        comp_score+=1
        messagebox.showinfo("Unlucky!", "YOU LOOSE!\n"+"Your Choice:Rock"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    
    
def paper():
    global user_score, comp_score
    
    comp = random.randint(1,3)

    if comp == 1:
        comp = "Rock"
        user_score+=1
        messagebox.showinfo("Congratulation!", "YOU WIN!\n"+"Your Choice:Paper"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    elif comp==2:
        comp = "Paper"
        messagebox.showinfo("Same choice!", "EGUALITY!\n"+"Your Choice:Paper"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
        
    else:
        comp = "Scissors"
        comp_score+=1
        messagebox.showinfo("Unlucky!", "YOU LOOSE!\n"+"Your Choice:Paper"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
def scissor():
    global user_score, comp_score
    
    comp = random.randint(1,3)

    if comp == 2:
        comp = "Paper"
        user_score+=1
        messagebox.showinfo("Congratulation!", "YOU WIN!\nYour Choice: Scissors\n"+"Comp choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    elif comp==3:
        comp = "Scissors"
        messagebox.showinfo("Same choice!", "EGUALITY!\nYour Choice: Scissors\n"+"Comp choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
        
    else:
        comp = "Rock"
        comp_score+=1
        messagebox.showinfo("Unlucky!", "YOU LOOSE!\nYour Choice: Scissors\n"+"Comp choice:"+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))


    
B1 = tkinter.Button(top, image = caillou_tk ,height="200",width="180", command = Rock)
B2 = tkinter.Button(top, image = feuille_tk ,height="200",width="180", command = paper)
B3 = tkinter.Button(top, image = ciseaux_tk ,height="200",width="180", command = scissor)

B1.pack(side='left')
B2.pack(side='left')
B3.pack(side='left')

top.mainloop()
