import Tkinter
import tkMessageBox

window = Tkinter.Tk()
window.wm_title("Igra - pogodi tajni broj")

label = Tkinter.Label(window, text="Unesi broj: ")
label.pack()

entry = Tkinter.Entry(window)
entry.pack()

def button_press():
    try:
        unos = int(entry.get())

        tocan_odgovor = 32
        odgovor_tekst = ""

        if unos == tocan_odgovor:
            odgovor_tekst = "Tocno"
        elif tocan_odgovor < unos:
            odgovor_tekst = "odgovor je manji od unesenog broja"
        else:
            odgovor_tekst = "odgovor je veci od unesenog broja"

        tkMessageBox.showinfo("Rezultat", odgovor_tekst)
    except:
        tkMessageBox.showwarning("greska", "unos nije broj")
        #print "Nije broj"

button = Tkinter.Button(window, text="provjeri", command=button_press)
button.pack()

window.mainloop()


