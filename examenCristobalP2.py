pregunta=str (input("si/no"))
while pregunta=="si":
    x1=int (input("x1")) 
    x2=int (input("x2")) 
    y1=int (input("y1")) 
    y2=int (input("y2"))
    y=y2-y1
    x=x2-x1
    m=y/x
    if x==0:
        print("es una pendiente es de una recta vertical")
    elif m==0:
        print("es una recta horizontal")
    elif m>0:
        print("es una recta con pendeinte positiva")
    elif m<0:
        print("es una recta con pendeinte negativa")
    print("la pendiente de la recta es m="+m)
    print("la ecuacion de la recta es y-"+y1+" = "+ m + "(x-"+x1+")")
    pregunta = input("quiere continuar calculando?")