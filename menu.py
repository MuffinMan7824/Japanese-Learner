from functools import partial
import Helper
import tkinter as tk
import Hiragana
def display_menu(window):
    
     #making widget 
    frame = tk.Frame(window,width=1000, height=700)

    frame.pack(fill='x', expand=True)
    btn = partial(Helper.button_freep,frame=frame)
    txt = partial(Helper.text_freep,frame=frame)

    txt("日本語を学ぶ",500,200,font=60)
    txt("Learn Japanese",500,280,font=30)
    btn("あ",333,380,lambda: (Helper.wipe_screen(frame),Hiragana.display_Hiragana(window)))
    txt("Hiragana",333,435)

    