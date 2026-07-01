import pygame
import tkinter as tk
import menu
pygame.mixer.init()

#making the window at the start 
window = tk.Tk()

#Window Size
window.geometry("1000x700")

menu.display_menu(window)
#calling method to display Hiragana

#Hiragana.display_Hiragana(window)
#closing loop for the window
window.mainloop()

