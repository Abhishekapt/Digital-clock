from time import strftime
from tkinter import Label, Tk
window = Tk()
window.title("")
window.geometry("200x80")
window.configure(bg="red")
window.resizable(False,False)     

clocl_label = Label(window, bg= "red", fg = "white", font = ("Times",30,"bold"),relief='flat')
clocl_label.place(x = 20, y = 20)
def updating_label():
    current_time = strftime('%H: %M: %S')
    clocl_label.configure(text=current_time)
    clocl_label.after(80, updating_label)
updating_label()
window.mainloop()