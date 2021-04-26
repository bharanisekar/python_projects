from tkinter import *

window = Tk()

window.title("Mile to Km Converter")
window.minsize(width=500, height=400)
window.config(padx=100,pady=100)

entry1 = Entry(width=10)
# entry.insert(END, string="0")
print(entry1.get())
entry1.grid(column=1,row=0)

def action():
    mile = float(entry1.get())
    val = mile * 1.689
    entry2.config(text=f"{val}") #changing the entry2 labels new value that why using .config()

lable = Label(text="Miles")
lable.grid(column=2,row=0) #grid is table view we are seting this label in column-2 and row-0..row and column starts with 0


lable = Label(text="is equal to")
lable.grid(column=0,row=1)

entry2 = Label(text="0")
entry2.grid(column=1,row=1)

lable = Label(text="Km")
lable.grid(column=2,row=1)



button = Button(text="Calculate", command=action)
button.grid(column=1,row=2)





window.mainloop()