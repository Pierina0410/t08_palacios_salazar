    #012345678901234567890123456789012345678901234567890123456789012345678901
    #         10        20        30        40         50        60       70
str="BUENAS NOCHES A TODOS LOS PRESENTES,ME TOCA EXPONER SOBRE  PROGRAMACIÓN"
    #56789098765432109876543210987654321
#mostrar la letra B
print(str[0])
#mostrar la palabra buenas
print(str [0]+ str[1]+ str[2]+str[3]+str[4]+str[5])
#mostrar la palabra programación
print(str[-12::])
#mostrar la palabra todos
print((str[16:21]))
#mostrar la frese BUENAS NOCHES A TODOS LOS PRESENTES
print(str[34::-1])
#mostrar la frase BUENAS NOCHES
print(str[0:13])
#mostrar la frase BUEN PRESENTE
print(str[0:4]+ " " + str[26:34])
#mostrar la frase NOCHE BUENA
print(str[7:12]+ " " + str[0:5])
#mostrar la frase PROGRAMACIÓN escrita al revés
print(str[-1:-13:-1])
#mostrar la frase ME TOCA EXPONER SOBRE PROGRAMACIÓN
print(str[36:71])
#mostrar la frase BUENAS NOCHES A TODOS ,ME TOCA EXPONER SOBRE PROGRAMACIÓN
print(str[71::-1])
#mostrar la frase BUEN PROGRAMA
print(str[0:4] + " " + str[58:67])
#mostrar la frase LA PRESENTE NOCHE
print(str[22]+ str[14] + str[25:34]+ str[6:12])
#mostrar la palabra EXPONER
print(str[-27:-20])
#mostrar la frase TODO PROGRAMACIÓN
print(str[15:20]+ " " + str[58:71])

