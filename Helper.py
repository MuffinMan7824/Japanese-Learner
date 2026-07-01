import pygame
import os
import tkinter as tk


#playing sound 
def play_sound(buttonname):
    sound_path = os.path.join("audio", f"{buttonname}.mp3")
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
#making button 
def make_button(buttontext,row,column,frame,command=None,columnspan=None,Hiraalt=None):
    if command == None:
        if Hiraalt == None:
            command = lambda: play_sound(buttontext)
        else:
            command = lambda: play_sound(Hiraalt)

        
    buttonname =tk.Button(frame, text=buttontext,padx=10, pady=10, font=('Arial', 18), command=command)
    buttonname.grid(row=row,column=column,padx=10,pady=10, sticky = tk.W+tk.E, columnspan=columnspan)
#making text 
def make_text(textname,row,column,frame,font=18):
    textname =tk.Label(frame,text=textname,font=('Arial',font))
    textname.grid(row=row,column=column,padx=10,pady=10, sticky = tk.W+tk.E)
#making button that is not locked to a grid 
def button_freep(buttonname,x,y,command,frame):
    buttonname=tk.Button(frame,text=buttonname,command=command,padx=10, pady=10,font=('Arial',18))
    buttonname.place(x=x,y=y,anchor='center')
#making text that is not locked to a grid 
def text_freep(textname,x,y,frame,font=18):
    textname=tk.Label(frame,text=textname,font=('Arial',font))
    textname.place(x=x,y=y,anchor='center')
#erasing the frame
def wipe_screen(frame):
    frame.destroy()