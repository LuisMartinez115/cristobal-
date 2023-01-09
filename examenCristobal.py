import turtle
turtle.shape("turtle")
lados=int (input("cantidad de lados deseados "))
if lados>=3 :
    largo=int (input("longitud de los lados "))
    if largo>=20:
        aumento=int (input("aumento entre figuras "))
        figuras=int (input("numero de figuras "))
        nidos=int (input("cantidad de nidos "))
        distancia=int (input("distancia entre nidos "))
        for i in range (0,nidos):
            largo2=largo
            for j in range (0,figuras):
                for k in range(0,lados):
                    turtle.forward(largo2)
                    turtle.right(360/lados)
                largo2=largo2 + aumento
            turtle.right(360/nidos)
            turtle.penup()
            turtle.forward(distancia)
            turtle.pendown()
            