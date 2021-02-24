from tkinter import *
import tkinter
from PIL import Image, ImageTk

rocketX = 225

window = Tk(className = "Rocket")
window.title("Rocket")
window.geometry("500x500")
window.resizable(height = False, width = False)
window.call("wm", "iconphoto", window, tkinter.Image("photo", file = "resources/images/rocket.png"))

rocket_image = Image.open("resources/images/rocket.png")
rocket_image = rocket_image.resize((50, 50), Image.ANTIALIAS)
rocket_image = ImageTk.PhotoImage(rocket_image)
rocket = tkinter.Label(image = rocket_image)

def loop():
	if window.state() != "normal":
		return
	global rocketX
	rocket.place(x = rocketX, y = 450)
	rocketX -= 1
	window.after(10, loop)
loop()

window.mainloop()