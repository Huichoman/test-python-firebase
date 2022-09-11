import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
import random

from tkinter import *

ws = Tk()
ws.title("PythonGuides")
ws.config(bg="#5f734c")
ws.geometry("400x300")

# seed(1)


def generate_fakeTemp():
    fakeTemp = random.uniform(36, 40)
    lbl.config(text=fakeTemp)


lbl = Label(ws, bg="#5f734c", font=(18))
lbl.pack(expand=True)

btn = Button(ws, text="Generate Fake Temp", padx=10, pady=5, command=generate_fakeTemp)
btn.pack(expand=True)

# def message():
#     print('Keep yourself hyderated.')
#     ws.after(2000, message)

# ws.after(2000, message)
ws.mainloop()


# cred = credentials.Certificate("./biosmart-walker-86ad7de34046.json")
# firebase_admin.initialize_app(
#     cred, {"databaseURL": "https://biosmart-walker-default-rtdb.firebaseio.com/"}
# )

# ref = db.reference("/temp")
# ref.push().set({"value": 25, "time": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
