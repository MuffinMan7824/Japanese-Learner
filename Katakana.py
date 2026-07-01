from functools import partial
import Helper
import tkinter as tk
import menu

Katakana = ["ア", "イ", "ウ", "エ", "オ",
    # K row
    "カ", "キ", "ク", "ケ", "コ",
    # S row
    "サ", "シ", "ス", "セ", "ソ",
    # T row
    "タ", "チ", "ツ", "テ", "ト",
    # N row
    "ナ", "ニ", "ヌ", "ネ", "ノ",
    # H row
    "ハ", "ヒ", "フ", "ヘ", "ホ",
    # M row
    "マ", "ミ", "ム", "メ", "モ",
    # Y row
    "ヤ", "ユ", "ヨ",
    # R row
    "ラ", "リ", "ル", "レ", "ロ",
    # W row
    "ワ", "ヲ",
    # N
    "ン"]

def display_Katakana(window):

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
    btn("ン",1,0,Hiraalt="ん")
    btn("ワ",1,1,Hiraalt="わ")
    btn("ラ",1,2,Hiraalt="ら")
    btn("ヤ",1,3,Hiraalt="や")
    btn("マ",1,4,Hiraalt="ま")
    btn("ハ",1,5,Hiraalt="は")
    btn("ナ",1,6,Hiraalt="な")
    btn("タ",1,7,Hiraalt="た")
    btn("サ",1,8,Hiraalt="さ")
    btn("カ",1,9,Hiraalt="か")
    btn("ア",1,10,Hiraalt="あ")
    #row 2
    btn("リ",2,2,Hiraalt="り")
    btn("ミ",2,4,Hiraalt="み")
    btn("ヒ",2,5,Hiraalt="ひ")
    btn("ニ",2,6,Hiraalt="に")
    btn("チ",2,7,Hiraalt="ち")
    btn("シ",2,8,Hiraalt="し")
    btn("キ",2,9,Hiraalt="き")
    btn("イ",2,10,Hiraalt="い")
    #row 3 
    btn("ル",3,2,Hiraalt="る")
    btn("ユ",3,3,Hiraalt="ゆ")
    btn("ム",3,4,Hiraalt="む")
    btn("フ",3,5,Hiraalt="ふ")
    btn("ヌ",3,6,Hiraalt="ぬ")
    btn("ツ",3,7,Hiraalt="つ")
    btn("ス",3,8,Hiraalt="す")
    btn("ク",3,9,Hiraalt="く")
    btn("ウ",3,10,Hiraalt="う")
    #row 4
    btn("レ",4,2,Hiraalt="れ")
    btn("メ",4,4,Hiraalt="め")
    btn("ヘ",4,5,Hiraalt="へ")
    btn("ネ",4,6,Hiraalt="ね")
    btn("テ",4,7,Hiraalt="て")
    btn("セ",4,8,Hiraalt="せ")
    btn("ケ",4,9,Hiraalt="け")
    btn("エ",4,10,Hiraalt="え")
    #row 5
    btn("ヲ",5,1,Hiraalt="を")
    btn("ロ",5,2,Hiraalt="ろ")
    btn("ヨ",5,3,Hiraalt="よ")
    btn("モ",5,4,Hiraalt="も")
    btn("ホ",5,5,Hiraalt="ほ")
    btn("ノ",5,6,Hiraalt="の")
    btn("ト",5,7,Hiraalt="と")
    btn("ソ",5,8,Hiraalt="そ")
    btn("コ",5,9,Hiraalt="こ")
    btn("オ",5,10,Hiraalt="お")

    #exit 
    btn("Exit",6,8,columnspan=3,command=lambda: (Helper.wipe_screen(frame),menu.display_menu(window)))
    
