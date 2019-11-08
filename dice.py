import random
import tkinter as tk
from PIL import Image, ImageTk
import time


def gif_roll():
    #roll = ["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg"]
    roll = ["1.png","2.png","3.png","4.png","5.png","6.png"]
    #if u want use png or jpeg files comment one of two
    gif_list =[]
    for i in roll:
        roll = Image.open(i)
        roll = roll.resize((350,350),Image.ANTIALIAS)
        roll = ImageTk.PhotoImage(roll)
        gif_list.append(roll)
    for k in range(0,1):
        for gif in gif_list:
            canvas.delete(all)
            canvas.create_image(300,300,image=gif,anchor='center')
            canvas.update()
            #canvas.create_text(30,30,anchor=LEFT)   
            time.sleep(0.1)

def pressme():
    gif_roll()
    num = random.randint(1,6)
    print(num)
    #num = str(num)+'.jpg'
    num = str(num)+'.png'
    #if u want use png or jpeg files comment one of two
    img = Image.open(num)
    img = img.resize((350,350),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    canvas.delete(all)
    canvas.create_image(300,300,image=photo,anchor='center')
    window.update()
    canvas.create_text()
        

    

window = tk.Tk()
window.title('Dice')
canvas = tk.Canvas(window,width=500,height=500)
canvas.grid(row=5,column=5)
btn = tk.Button(window, text = "press!!",command=pressme)
btn.grid(column=5,row=1)
window.mainloop()
