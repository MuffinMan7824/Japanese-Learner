from functools import partial
import Helper
import tkinter as tk
import menu

Hiragana = ["あ", "い", "う", "え", "お",
    # K row
    "か", "き", "く", "け", "こ",
    # S row
    "さ", "し", "す", "せ", "そ",
    # T row
    "た", "ち", "つ", "て", "と",
    # N row
    "な", "に", "ぬ", "ね", "の",
    # H row
    "は", "ひ", "ふ", "へ", "ほ",
    # M row
    "ま", "み", "む", "め", "も",
    # Y row
    "や", "ゆ", "よ",
    # R row
    "ら", "り", "る", "れ", "ろ",
    # W row
    "わ", "を",
    # N
    "ん"]

def display_Hiragana(window):

    #making widget 
    frame = tk.Frame(window)
    #giving a normal pack to give grid location
    frame.pack(fill='x')

    #so we dont have to define frame everyime for both the button and text 
    btn = partial(Helper.make_button, frame=frame)
    txt = partial(Helper.make_text, frame=frame)

    #configing the columns
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

    #exit 
    btn("Exit",6,8,columnspan=3,command=lambda: (Helper.wipe_screen(frame),menu.display_menu(window)))
    
