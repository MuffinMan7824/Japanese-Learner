import pygame
import os
import tkinter as tk

def Meow():
    print("Meow")
def play_sound(buttonname):
    sound_path = os.path.join("audio", f"{buttonname}.mp3")
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()

def make_button(buttontext,row,column,frame,command=None):
    if command == None:
        command = lambda: play_sound(buttontext)
    buttonname =tk.Button(frame, text=buttontext,padx=10, pady=10, font=('Arial', 18), command=command)
    buttonname.grid(row=row,column=column,padx=10,pady=10, sticky = tk.W+tk.E)
def make_text(textname,row,column,frame):
    textname =tk.Label(frame,text=textname,font=('Arial',18))
    textname.grid(row=row,column=column,padx=10,pady=10, sticky = tk.W+tk.E)