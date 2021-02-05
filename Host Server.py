from socket import *
from _thread import *
from tkinter import *

root = Tk()
root.title("JS Host Server")
root.iconbitmap('JS logo.ico')
root.geometry("2000x1100")
s = socket((AF_INET), SOCK_STREAM)
host = gethostname()
print(" server will start on host : ", host)
port = 8080
s.bind((host,port))
s.listen(50)
label = Label(root)
label.grid(row=3, column=3)
entry = Entry(root, width=40)
entry.grid(row=1, column=3)
sessions = []


def clicked():
    message = f"Charonum: {entry.get()}"
    for c in sessions:
        c.send(message.encode('utf-8'))
    entry.delete(0, END)


btn = Button(root, text="Send", bg="green", fg="white", width=8, height=1, command=clicked)
btn.grid(row=1, column=4)


def recvevthread(c, ad):
    while True:
        label['text'] = str(ad[1]) + ":" + c.recv(1024).decode('utf-8')


def mainthread(s):
    while True:
        c, ad = s.accept()
        sessions.append(c)
        label["text"] = "New connection from " + str(ad[1])
        start_new_thread(recvevthread, (c, ad))


start_new_thread(mainthread, (s,))

root.mainloop()