import tkinter as tk
from data.colors import COLORS
from data.menus import MENU
from widget.button.Button import Button


class LeftFrame:
    '''
    Class for Left Frame to hold the menu items.
    '''

    def __init__(self, window, name):
        self.frame = tk.Frame(master=window, name=name, bg=COLORS.GRAY)
        # this is needed to be able to be able to stare the main window object throughout the class.
        self.master = window
        self.add_frame()
        self.add_menus()

    def add_frame(self):
        self.frame.pack(side=tk.LEFT, fill=tk.Y, pady=(62, 0))

    def add_menus(self):
        # add menus in loop
        for menu_key, menu_text in MENU.items():
            # self.add_button(menu_text)
            button = Button(master=self.frame, name=menu_key, text=menu_text,
                            fg=COLORS.ORANGE, bg=COLORS.BLACK, width=18, height=2, handle_click=None)

    # def add_button(self, text):
    #     btn = tk.Button(master=self.frame, text=text)
    #     btn.pack()
