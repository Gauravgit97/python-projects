import time
import pyautogui   #this module holds an method which can click the screen shot
import tkinter as tk

def screen_shot():
    rand_no = int(round(time.time()*1000))
    path = f'S:\project\python projects\screenshot_from_py\{rand_no}.png'
    time.sleep(1)
    img = pyautogui.screenshot(path)
    img.show()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = 'Screen-Shot',
    command=screen_shot
)

button.pack(side= tk.LEFT)
close = tk.Button(
    frame,
    text = 'Quit',
    command=quit
)
close.pack(side= tk.LEFT)

root.mainloop()