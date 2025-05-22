
from tkinter import *
from tkinter.ttk import *
import random as rand

root = Tk()
root.geometry("600x360")
root.title('Lets play!')

paperimg = PhotoImage(file="paper.png")
sciimg = PhotoImage(file="sci.png")
rockimg = PhotoImage(file="rock.png")

papercimg = PhotoImage(file="paperc.png")
scicimg = PhotoImage(file="scic.png")
rockcimg = PhotoImage(file="rockc.png")

paperpimg = PhotoImage(file="paperp.png")
scipimg = PhotoImage(file="scip.png")
rockpimg = PhotoImage(file="rockp.png")

rps = ['rock', 'paper', 'scissors']
player = StringVar()
computer = rand.choice(rps)
res = StringVar()
mes = StringVar()
col = StringVar()
col.set('blue')
def press(ch):
    global res, mes, player, computer,col
    player.set(ch)

def result():
    global res, mes, player, computer, col


    if computer == 'rock':
        l1.configure(image=paperimg)
        l2.configure(image=rockcimg)
        l3.configure(image=sciimg)
    elif computer == 'scissors':
        l1.configure(image=paperimg)
        l2.configure(image=rockimg)
        l3.configure(image=scicimg)
    elif computer == 'paper':
        l1.configure(image=papercimg)
        l2.configure(image=rockimg)
        l3.configure(image=sciimg)

    if player.get() == 'rock':
        button1.configure(image=paperimg)
        button2.configure(image=rockpimg)
        button3.configure(image=sciimg)
    elif player.get() == 'scissors':
        button1.configure(image=paperimg)
        button2.configure(image=rockimg)
        button3.configure(image=scipimg)
    elif player.get() == 'paper':
        button1.configure(image=paperpimg)
        button2.configure(image=rockimg)
        button3.configure(image=sciimg)

    if player.get() == computer:
        res.set('Its a tie!')
        computer = rand.choice(rps)
    elif player.get() == 'rock' and computer == 'paper':
        res.set('Paper beats rock. You lost!')
        computer = rand.choice(rps)
    elif player.get() == 'rock' and computer == 'scissors':
        res.set('Rock beats scissors. You won!')
        computer = rand.choice(rps)
    elif player.get() == 'paper' and computer == 'scissors':
        res.set('Scissors beat paper. You lost!')
        computer = rand.choice(rps)
    elif player.get() == 'paper' and computer == 'rock':
        res.set('Paper beats rock. You won!')
        computer = rand.choice(rps)
    elif player.get() == 'scissors' and computer == 'paper':
        res.set('Scissors beats paper. You won!')
        computer = rand.choice(rps)
    elif player.get() == 'scissors' and computer == 'rock':
        res.set('Rock beats scissors. You lost!')
        computer = rand.choice(rps)
    elif player.get() == 'quit':
        exit()
    col.set('blue')
def com(ch1):
    press(ch1)
    result()

button1 = Button(root, text='Paper', image=paperimg, command=lambda: com('paper'))
button1.grid(row=1, column=1)

button2 = Button(root, text='Rock', image=rockimg, command=lambda: com('rock'))
button2.grid(row=1, column=2)

button3 = Button(root, text='Scissors', image=sciimg, command=lambda: com('scissors'))
button3.grid(row=1, column=3)

Button(root, text='Quit the game !', command=lambda: com('quit')).grid(row=1, column=4)

l1 = Label(root, image=papercimg)
l1.grid(row=2, column=1)
l2 = Label(root, image=rockcimg)
l2.grid(row=2, column=2)
l3 = Label(root, image=scicimg )
l3.grid(row=2, column=3)

expr_field = Entry(root, textvariable=res)
expr_field.grid(columnspan=4, ipadx=70)


mainloop()