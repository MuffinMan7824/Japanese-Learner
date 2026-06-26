import pygame
import tkinter as tk
import Hiragana
pygame.mixer.init()

window = tk.Tk()


window.geometry("1000x700")


Hiragana.display_Hiragana(window)
window.mainloop()

