import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("tic tac toe")

global bclick,drw
blclick = True
drw = 1


nu = 0
while nu < 9:
    for rowi in range (1,4):
        #nu = nu+1
        #print(nu)
        for coli in range(1,4):
            if nu<10:
                nu =  nu + 1
                print(nu)
                btn = 'btn' + str(nu)
                btn = tk.Button(window,text='',fg='black', height=3, width=15 , command = lambda : btnclick(btn)) 
                btn.grid(column=coli,row=rowi)
def reset():
    global bclick,drw
    nu = 0
    while nu < 9:
        for rowi in range (1,4):
        #nu = nu+1
        #print(nu)
            for coli in range(1,4):
                if nu<10:
                    nu =  nu + 1
                    print(nu)
                    btn = 'btn' + str(nu)
                    btn = tk.Button(window,text='',fg='black', height=3, width=15 , command = lambda : btnclick(btn)) 
                    btn.grid(column=coli,row=rowi)

    bclick = True
    lbl = tk.Label(window, text='Player 1 turn')
    lbl.grid(column = 2 , row = 6)
    drw = 1
    lbl = tk.Label(window, text='                     ')
    lbl.grid(column = 3 , row = 6)
    lbl = tk.Label(window, text='                     ')
    lbl.grid(column = 3 , row = 8)


def chkwin(letter): 
    for colum in range(1,4):
        for rowi in range(1,4):
            if(get_value(rowi,colum) == letter and get_value(rowi,colum+1) == letter and get_value(rowi,colum+2) == letter or
               get_value(colum,rowi) == letter and get_value(colum+1,rowi) == letter and get_value(colum+2,rowi) == letter or
               get_value(1,1) == letter and get_value(2,2) == letter and get_value(3,3) == letter or
               get_value(3,1) == letter and get_value(2,2) == letter and get_value(1,3) == letter ):
                if letter == 'X':
                    lbl = tk.Label(window, text='player 1 won')
                    lbl.grid(column = 2 , row = 6)
                    lbl = tk.Label(window, text='player 2 lost')
                    lbl.grid(column = 2 , row = 8)
                    butt_chnge_state('disable')
                elif letter == 'O':
                    lbl = tk.Label(window, text='player 2 won')
                    lbl.grid(column = 2 , row = 6)
                    lbl = tk.Label(window, text='player 1 lost')
                    lbl.grid(column = 2 , row = 8)
                    butt_chnge_state('disable')
                else :
                    if drw == 10:
                        lbl = tk.Label(window, text='its a draw')
                        lbl.grid(column = 2 , row = 6)
                        butt_chnge_state('disable')
                    

def get_value(x,y):
    return  (window.grid_slaves(row = x,column = y)[0])['text']                     
                
def butt_chnge_state(x):
    for i in range(10):
        btn = 'btn' + str(i)
        btn['state'] = x



def btnclick(butt):
    global bclick,drw
    print(butt)
    if butt['text'] == '' and bclick == True:
            butt['text'] = 'X'
            bclick = False
            lbl = tk.Label(window, text='Player 2 turn')
            lbl.grid(column = 2 , row = 6)
            drw = drw + 1
            chkwin('X')
    elif butt['text'] == '' and bclick == False:
            butt['text'] = 'O'
            bclick = True
            lbl = tk.Label(window, text='Player 1 turn')
            lbl.grid(column = 2 , row = 6)
            drw = drw + 1
            chkwin('O')
    else:
        messagebox.showinfo('tic tac toe','button already pressed')

 
        

reset()
lbl = tk.Label(window, text ='tic tac toe',font=('',30))
lbl.grid(column = 2 , row =0)
lbl = tk.Label(window, text='Player 1 turn')
lbl.grid(column = 2 , row = 6)
playr_won = tk.Label(window, text='')
playr_won.grid(column = 3 , row = 6)
playr_loss = tk.Label(window, text='')
playr_loss.grid(column = 3 , row = 8)
player1 = tk.Label(window, text='player1 - X')
player1.grid(column = 1 , row = 6)
player1 = tk.Label(window, text='player2 - O')
player1.grid(column = 1 , row = 8)

btn_reset = tk.Button(window,text = 'reset game',command=lambda : reset())
btn_reset.grid(column=2,row=10)

window.mainloop()

