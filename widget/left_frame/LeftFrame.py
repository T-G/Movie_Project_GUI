import tkinter as tk
from data.colors import COLORS
from data.menus import MENU


class LeftFrame:
    '''
    Class for Left Frame to hold the menu items.
    '''

    def __init__(self, window, name):
        self.frame = tk.Frame(master=window, name=name, bg=COLORS.GRAY)
        self.master = window # this is needed to be able to be able to stare the main window object throughout the class.
        self.add_frame()
        self.add_menus()

    def add_frame(self):
        self.frame.pack(side=tk.LEFT, fill=tk.Y, pady=(62, 0))

    def add_menus(self):
        # add menus in loop
        for menu_key, menu_text in MENU.items():
            self.add_button(menu_text)

    def add_button(self, text):
        btn = tk.Button(master=self.frame, text=text)
        btn.pack()