from guizero import *
import string
import numpy as np
import matplotlib.pyplot as plt

def apri_file1():

    f=open("dati.txt")

    coordX = []
    coordY = []
    for riga in f:
        valori = str(f.readline())  # converto in stringa la riga
        Nval = len(valori)          # conto il numero di caratteri
        valori = valori.strip('\n') # elimino i lterminatore di riga
        valori = valori.split(',')  # separo la stringa in due numeri
        valori = list(valori)       # converto in lista
        print(valori)
        coordX.append(int(valori[0])) # aggiungo la coordinata X
        coordY.append(int(valori[1])) # aggiungo la coordinata Y

    f.close()  # chiudiamo il file

    print ("X: ",coordX)
    print ("Y: ",coordY)

    # ordiniamo le liste
    coordX.sort()
    coordY.sort()

    print("liste ordinate:") 
    print ("X: ",coordX)
    print ("Y: ",coordY)

    # stampo il tipo di dati delle coordinate
    print(type(coordX))
    print(type(coordY))

    # ora sono pronte per essere usate anche nei grafici

    plt.plot(coordX,coordY,)
    plt.ylabel('some numbers')
    plt.show()

def apri_file2():

    b=open("datii.txt")

    coordX = []
    coordY = []
    for riga in b:
        valori = str(b.readline())  # converto in stringa la riga
        Nval = len(valori)          # conto il numero di caratteri
        valori = valori.strip('\n') # elimino i lterminatore di riga
        valori = valori.split(',')  # separo la stringa in due numeri
        valori = list(valori)       # converto in lista
        print(valori)
        coordX.append(int(valori[0])) # aggiungo la coordinata X
        coordY.append(int(valori[1])) # aggiungo la coordinata Y

    b.close()  # chiudiamo il file

    print ("X: ",coordX)
    print ("Y: ",coordY)

    # ordiniamo le liste
    coordX.sort()
    coordY.sort()

    print("liste ordinate:") 
    print ("X: ",coordX)
    print ("Y: ",coordY)

    # stampo il tipo di dati delle coordinate
    print(type(coordX))
    print(type(coordY))

    # ora sono pronte per essere usate anche nei grafici

    plt.plot(coordX,coordY,)
    plt.ylabel('some numbers')
    plt.show()


def apri_file3():

    c=open("datiii.txt")

    coordX = []
    coordY = []
    for riga in c:
        valori = str(c.readline())  # converto in stringa la riga
        Nval = len(valori)          # conto il numero di caratteri
        valori = valori.strip('\n') # elimino i lterminatore di riga
        valori = valori.split(',')  # separo la stringa in due numeri
        valori = list(valori)       # converto in lista
        print(valori)
        coordX.append(int(valori[0])) # aggiungo la coordinata X
        coordY.append(int(valori[1])) # aggiungo la coordinata Y

    c.close()  # chiudiamo il file

    print ("X: ",coordX)
    print ("Y: ",coordY)

    # ordiniamo le liste
    coordX.sort()
    coordY.sort()

    print("liste ordinate:") 
    print ("X: ",coordX)
    print ("Y: ",coordY)

    # stampo il tipo di dati delle coordinate
    print(type(coordX))
    print(type(coordY))

    # ora sono pronte per essere usate anche nei grafici

    plt.plot(coordX,coordY,)
    plt.ylabel('some numbers')
    plt.show()

app = App(title="bottoni per aprire file", width=100, height=90, layout="grid")

button1 = PushButton(app, command=apri_file1, text="1° grafico", grid=[0,5])

button5 = PushButton(app, command=apri_file2, text="2° grafico", grid=[10,5])

button6 = PushButton(app, command=apri_file3, text="3° grafico", grid=[20,5])



def clicked(): #lets create a function that will update the title of main window

    if tbox1.value is "dati.txt":
        command=apri_file1
       

tbox1 = TextBox(app, grid=[10,40]) #create an empty textbox

but = PushButton(app, text='Scrivere quale file aprire e cliccarmi', command=clicked, grid=[10,60])



# da notare che posso fare un ciclo all'interno di un file
# direttamente sulle righe


app.display()
