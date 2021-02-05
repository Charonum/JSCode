from tkinter import *
import socket
from _thread import *



logged = open("Logged.txt", "r")
user = logged.read()
root = Tk()
root.title("JS")
root.iconbitmap('JS logo.ico')
s = socket.socket((socket.AF_INET), socket.SOCK_STREAM)
host = "50.113.72.248"
port = 8080
s.connect((host,port))
label = Label(root)
label.grid(row=3, column=3)
entry = Entry(root, width=40)
entry.grid(row=1, column=3)


def clicked():
    epic = f"{user}: {entry.get()}"
    message = epic
    s.send(message.encode("utf-8"))
    entry.delete(0, END)


btn = Button(root, text="Send", bg="green", fg="white", width=8, height=1, command=clicked)
btn.grid(row=1, column=4)


def recvevthread(s):
    while True:
        label['text'] = s.recv(1024).decode('utf-8')


start_new_thread(recvevthread, (s,))


def on_closing():
    f = open('Logged.txt', 'r+')
    f.truncate(0)
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.geometry("2000x1100")
root.mainloop()
