import math
figura=str (input("para calcular el area de una piramide escribir P, C para el cono"))
if figura=="P":
    ancho=int (input("ancho")) 
    largo=int (input("largo"))
    h=int (input("altura"))
    print("el volumen de la piramide es "+(ancho*largo*h)/3)
elif figura=="C":
    h=int (input("altura"))
    r=int (input("radio"))
    print("el volumen del cono es de "+(math.pi*r*r*h)/3)
else:
    print("dulce o truco")

