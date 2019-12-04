import bs4
import requests
from tkinter import *
from tkinter import Scrollbar


win = Tk()
# win.config(bg="")
win.title("WebScapper by Hari")
win.geometry("600x600")

scrollbar = Scrollbar(win, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbarHor = Scrollbar(win, orient=HORIZONTAL)
scrollbarHor.pack(side=BOTTOM, fill=X)

entryField = Entry(win, font=('', 15))

entryField.pack(ipadx=300)
def btnClick():
    try:
        url = Entry.get(entryField)
        data = requests.get(url)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        # for tag in soup.find_all('html'):
        text.insert(END, soup.prettify())
    except:
        print("Check your internet connection !")


btn = Button(win, text="Get code", command=btnClick).pack()
text = Text(win, font=('', 18), yscrollcommand=scrollbar.set, xscrollcommand=scrollbarHor.set)
text.pack(fill=BOTH, expand=1)
scrollbar.config(command=text.yview)
scrollbarHor.config(command=text.xview)
win.mainloop()