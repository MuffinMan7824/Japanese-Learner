import tkinter as tk
from functools import partial
import pygame
pygame.mixer.init()
window = tk.Tk()

def play_sound(buttonname):
    pygame.mixer.music.load(f"audio/{buttonname}.mp3")
    pygame.mixer.music.play()

def make_button(buttontext,row,column,frame):
    buttonname =tk.Button(frame, text=buttontext,padx=10, pady=10, font=('Arial', 18), command=lambda: play_sound(buttontext))
    buttonname.grid(row=row,column=column,padx=10,pady=10, sticky = tk.W+tk.E)
def make_text(textname,row,column,frame):
    textname =tk.Label(frame,text=textname,font=('Arial',18))
    textname.grid(row=row,column=column,padx=10,pady=10, sticky = tk.W+tk.E)
window.geometry("1000x700")

def display_Hiragana():
    frame = tk.Frame(window)
    frame.pack(fill='x')

    btn = partial(make_button, frame=frame)
    txt = partial(make_text, frame=frame)

    frame.columnconfigure(0, weight=2)
    frame.columnconfigure(1, weight=2)
    frame.columnconfigure(2, weight=2)
    frame.columnconfigure(3, weight=2)
    frame.columnconfigure(4, weight=2)
    frame.columnconfigure(5, weight=2)
    frame.columnconfigure(6, weight=2)
    frame.columnconfigure(7, weight=2)
    frame.columnconfigure(8, weight=2)
    frame.columnconfigure(9, weight=2)
    frame.columnconfigure(10, weight=2)
    frame.columnconfigure(11, weight=2)

    #title row 
    txt("n",0,0)
    txt("w",0,1)
    txt("r",0,2)
    txt("y",0,3)
    txt("m",0,4)
    txt("h",0,5)
    txt("n",0,6)
    txt("t",0,7)
    txt("s",0,8)
    txt("k",0,9)

    #title column 
    txt("-a",1,11)
    txt("-i",2,11)
    txt("-u",3,11)
    txt("-e",4,11)
    txt("-o",5,11)
    #row 1
    btn("ん",1,0)
    btn("わ",1,1)
    btn("ら",1,2)
    btn("や",1,3) 
    btn("ま",1,4)
    btn("は",1,5)
    btn("な",1,6)
    btn("た",1,7)
    btn("さ",1,8)
    btn("か",1,9)
    btn("あ",1,10)
    #row 2


    btn("di",2,1)
    btn("り",2,2)
    btn("み",2,4)
    btn("ひ",2,5)
    btn("に",2,6)
    btn("ち",2,7)
    btn("し",2,8)
    btn("き",2,9)
    btn("い",2,10)
    #row 3 
    btn("る",3,2)
    btn("ゆ",3,3)
    btn("む",3,4)
    btn("ふ",3,5)
    btn("ぬ",3,6)
    btn("つ",3,7)
    btn("す",3,8)
    btn("く",3,9)
    btn("う",3,10)
    #row 4
    btn("れ",4,2)
    btn("め",4,4)
    btn("へ",4,5)
    btn("ね",4,6)
    btn("て",4,7)
    btn("せ",4,8)
    btn("け",4,9)
    btn("え",4,10)
    #row 5
    btn("を",5,1)
    btn("ろ",5,2)
    btn("よ",5,3)
    btn("も",5,4)
    btn("ほ",5,5)
    btn("の",5,6)
    btn("と",5,7)
    btn("そ",5,8)
    btn("こ",5,9)
    btn("お",5,10)

    






display_Hiragana()
window.mainloop()