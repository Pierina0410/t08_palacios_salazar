#Ejercicio1
msg="Hola {} tu nota es {}"
print(msg.format("Juan","15"))

#Ejercicio2
msg="Rosaura {}  mascota es {}"
print(msg.format("tu","Kay"))

#Ejercicio3
msg="Tienes {}  grandes {}"
print(msg.format("muchos","amigos"))

#Ejercicio4
msg="nota"
print(msg.rjust(20))


#Ejercicio4
msg="tecnologia"
print(msg.rjust(100))


#Ejercicio5
msg="wifi"
print(msg.rjust(60))

#ejercicio6
portentaje="20"
print(portentaje.zfill(5))

#ejercicio7
probabilidad="87"
print(probabilidad.zfill(3))
#ejercicio8
msg="Pierina{0:>30}"
print(msg.format("chida"))

#ejercicio9
msg="Ropa{0:>30}"
print(msg.format("vegero"))

#ejercicio10
msg="Hay {:d} personas"
print(msg.format(32))

#ejercicio11
msg="Tengo {:d}  perros"
print(msg.format(12))

#ejercicio11
msg="voy {:d}  minutos tarde"
print(msg.format(30))

#ejercicio12
pi=3.141592
msg="El valor de Pi es {} "
print(msg.format(pi))

#ejercicio12
X=345
msg="El valor de X es {} "
print(msg.format(X))

#EJERCICIO13
#Ejercicio1
msg="Roxana {} de nota  {}"
print(msg.format("tiene","20"))

#ejercicio14

msg="Tengo {:d} clases en la tarde"
print(msg.format(2))

#ejercicio15
msg="precio de {producto}"
item="pollo"
print(msg.format(producto=item))
