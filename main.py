# import window and frames
from widget import Window, LeftFrame


if __name__ == '__main__':
    # Root Window
    root = Window('Movie Library')

    # Left Frame
    left_frame = LeftFrame(root.window, 'leftFrame')
    # Right Frame

    # start root window -> mainloop()
    root.start_method()
