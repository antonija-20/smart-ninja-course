import Tkinter
import tkMessageBox

window = Tkinter.Tk()
window.wm_title("Zaigraj lutriju - sretni brojevi")

label1= Tkinter.Label(window, text = "unesi prvi broj")
label1.pack()

entry1 = Tkinter.Entry(window)
entry1.pack()

label2= Tkinter.Label(window, text = "unesi operator +, -, * ili /")
label2.pack()

entry2 = Tkinter.Entry(window)
entry2.pack()

label3= Tkinter.Label(window, text = "unesi drugi broj")
label3.pack()

entry3 = Tkinter.Entry(window)
entry3.pack()

def racunaj():
    try:
        prvi = int(entry1.get())
        drugi = int(entry3.get())
        operator = entry2.get()
        if operator == "+":
            rezultat = prvi + drugi
        elif operator == "-":
            rezultat = prvi - drugi
        elif operator == "*":
            rezultat = prvi * drugi
        elif operator == "/":
            rezultat = prvi / drugi
        else:
            rezultat = "pogresan unos operatora"
        tkMessageBox.showinfo("rezultat", racunaj)
    except:
        tkMessageBox.showwarning("Greska", "pogresan unos")

button = Tkinter.Button(window, text="Racunaj", command=racunaj)
button.pack()

window.mainloop()


