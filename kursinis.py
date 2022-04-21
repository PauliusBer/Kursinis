from tkinter import filedialog
from tkinter import *
import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt

x_reiksme = 0
y_reiksme = 0

# pradinio lango sukūrimas
pradinis = Tk()

# matmenų mustatymas

pradinis.geometry("200x200")

#failo nuskaitymas, jo pavadinimo ir stulpelių paėmimas
def failo_stulpeliai(failo_vieta):
    global stulpeliai, failo_pavad, failas
    failas = pd.read_csv(failo_vieta)
    failo_pavad = Path(failo_vieta).name
    stulpeliai = failas.columns.values.tolist()


#funkcija priskirianti stulpelį x ašiai
def reiksmes_suteikimas_x(reiksme):
    global x_reiksme
    x_reiksme = reiksme

#funkcija priskirianti stulpelį y ašiai
def reiksmes_suteikimas_y(reiksme):
    global y_reiksme
    y_reiksme = reiksme

#funkcija nuskaitanti failo vietą
def failo_vieta():
    failo_vieta = filedialog.askopenfilename()
    return failo_vieta

#funkcija piešianti grafiką, pagal nutylėjimą y stulpelio reikšmės yra sumuojamos
def piesti_grafika(x,y,failo_pavad):
    plt.title(f"Failo {failo_pavad} analizė")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.plot(failas.groupby([x]).sum()[y])
    plt.show()


# funkcija, kuri paspaudus mygtuką pirmajame lange atidaro antrąjį langą
def asys(langas):
    langas.withdraw()
# antrojo lango kūrimas perdavus pirmąjį langą kaip kintamąjį
    asys = Toplevel(langas)

# lango pavadinimo nustatymas
    asys.title("Ašys")

# ikonos pridėjimas
    asys.iconbitmap(r'C:\Users\Paulius\PycharmProjects\kursinis\ikona.ico')

 # lango matmenų nustatymas
    asys.geometry("370x150")

 # dinamiškas x-ašies stulpelių generavimas, paleidžiant funkciją perduodamas stulpelių sąrašas ir kiekvienam sąrašo įrašui sugeneruojamas atitinkamas mygtukas
    i=0
    Label(asys,
          text=f"Pasirinkite stulpelį x-ašiai").grid(row=i, column = 2)
    for a in stulpeliai:
        i += 1
        '''lambda funkcijoje papildomai sukurimas kintamasis x, 
        be jo visą laiką būtų naudojama paskutinė a reikšmė ir paspaudus ant mygtuko jis visad vykdytų paskutinio sąrašo mygtuko funkciją.
        Taip pat lambda funkcija priskiria kintamojo reikšmę grafiko x ašiai.'''
        mygtukas= Button(asys, text = a, command= lambda x=a:[reiksmes_suteikimas_x(x)])
        mygtukas.grid(row=i, column = 2)
    i=0
# dinamiškas y-ašies stulpelių generavimas
    Label(asys,
          text=f"Pasirinkite stulpelį y-ašiai").grid(row=i, column = 0)
    for a in stulpeliai:
        i+=1
        mygtukas= Button(asys, text = a,command= lambda y=a :[reiksmes_suteikimas_y(y)])
        mygtukas.grid(row=i, column = 0)
# lambda funkcija priskiria kintamojo reikšmę grafiko y ašiai
    iseiti = Button(asys, text="Piešti grafiką", command=lambda: [asys.destroy,piesti_grafika(x_reiksme,y_reiksme,failo_pavad)])
    iseiti.grid(row=i+2, column = 1)

# pavadinimo suteikimas pradiniam langui
pradinis.title("Pradinis langas")

pradinis.iconbitmap(r'C:\Users\Paulius\PycharmProjects\kursinis\ikona.ico')
label = Label(pradinis,
              text="Sveiki atvykę!")

label.pack(pady=10)

#pradinio lango mygtukas iškviečiantis funkciją nuskaitančią pasirinkto failo stulpelius bei iškviečiantis antrąjį langą
btn = Button(pradinis,
             text="Pasirinkite failą",
             command=lambda:[failo_stulpeliai(failo_vieta()),asys(pradinis)])
btn.pack(pady=10)

# tkinter lago paleidimas
mainloop()