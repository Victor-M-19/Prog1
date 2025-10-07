#Práctico 3: Estructuras condicionales.
#Alumno: Victor Agüero
'''1) Escribir un programa que solicite la edad del usuario.
Si el usuario es mayor de 18 años,deberá mostrar un mensaje
en pantalla que diga “Es mayor de edad”.'''
# Ingresamos la edad  usuario.
edad = int(input("Ingrese su edad: "))
# Verificamos si la edad es mayor a 18
if edad > 18:
    print("Es mayor de edad")

'''2) Escribir un programa que solicite su nota al usuario. 
Si la nota es mayor o igual a 6, deberá mostrar por pantalla 
un mensaje que diga “Aprobado”;en caso contrario deberá 
mostrar el mensaje “Desaprobado”.'''

nota= float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

'''3) Escribir un programa que permita ingresar solo números pares.
 Si el usuario ingresa un número par, imprimir por en pantalla el 
 mensaje "Ha ingresado un número par"; en caso contrario, imprimir por
pantalla "Por favor, ingrese un número par".'''
n=int(input("Ingrese un número: "))
if n % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

'''4) Escribir un programa que solicite al usuario su edad e imprima 
por pantalla a cuál de las siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años.'''
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("La edad ingresada corresponde a la categoría: Niño")
elif 12 <= edad and edad < 18:
    print("La edad ingresada corresponde a la categoría: Adolescente")
elif 18 <= edad and edad < 30:
    print("La edad ingresada corresponde a la categoría: Adulto joven")
else:
    print("La edad ingresada corresponde a la categoría: Adulto")

'''5) Escribir un programa que permita introducir contraseñas de entre 8 y 14
caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de 
longitud adecuada, imprimir por en pantalla el mensaje 
"Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
 Nota: investigue el uso de la función len() en Python para evaluar la 
 cantidad de elementos que tiene un iterable tal como una lista o un string.'''

contraseña=input("Ingrese una contraseña (entre 8 y 14 caracteres): ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

'''6) El paquete statistics de python contiene funciones que permiten tomar
una lista de números y calcular la moda, la mediana y la media de dichos 
números. Un ejemplo de su uso es el siguiente: from statistics import mode,
median, mean mi_lista = [1,2,5,5,3] mean(mi_lista) 
En la documentación oficial se puede encontrar más información sobre este 
paquete: https://docs.python.org/es/3.8/library/statistics.html. 
La moda (mode), la mediana (median) y la media (mean) son parámetros 
estadísticos que se pueden utilizar para predecir la forma de una 
distribución normal a partir del siguiente criterio: 
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y,
a su vez, la mediana es mayor que la moda. 
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y,
 a su vez, la mediana es menor que la moda. 
● Sin sesgo: cuando la media, la mediana y la moda son iguales.
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la
lista numeros_aleatorios, calcule su moda, su mediana y su media y las
compare para determinar si hay sesgo positivo, negativo o no hay sesgo.
Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma: import random
 numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y
 100 elegidos de forma aleatoria.'''
import random
from statistics import mode, median, mean  
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios) 
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print("Números aleatorios: ", numeros_aleatorios)
print("Moda: ", moda) 
print("Mediana: ", mediana)
print("Media: ", media)
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda:
    print("Sin sesgo")

'''7) Escribir un programa que solicite una frase o palabra al usuario.
Si el string ingresado termina con vocal, añadir un signo de exclamación 
al final e imprimir el string resultante por pantalla; en caso contrario,
dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.'''
frase = input("Ingrese una frase o palabra: ")
largo= len(frase)
ultima= frase[largo-1].lower()
if ultima in "aeiou":
    print(frase + "!")
else:
    print(frase)

'''8) Escribir un programa que solicite al usuario que ingrese su nombre y
 el número 1, 2 o 3 dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción
seleccionada por el usuario e imprimir el resultado por pantalla.'''

nom=input ("Ingrese su nombre: ")
print("Ingrese numero 1 si quiere su nombre en mayusculas: ","\n",
            "Ingrese numero 2 si quiere su nombre en minusculas: ","\n",
            "Ingrese numero 3 si quiere su nombre con la primer letra en mayuscula: ")
n=int(input("Ingrese numero: "))
if n==1:
    print(nom.upper())
elif n==2:
    print(nom.lower())
elif n==3:
    print(nom.title())
else:
    print("Opcion incorrecta")

'''9) Escribir un programa que pida al usuario la magnitud de un terremoto,
clasifique la magnitud en una de las siguientes categorías según la escala 
de Richter e imprima el resultado por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).'''

mag=float(input("Ingrese la magnitud del sismo: "))
if mag < 3:
    print("E sismo fue muy leve casi imperceptible")
elif 3 <= mag and mag < 4:
    print("El sismo fue leve, ligeramente perceptible")
elif 4 <= mag and mag < 5:
    print("El sismo fue moderado, sentido por personas, pero generalmente no causa daños")
elif 5 <= mag and mag < 6:
    print("El sismo fue fuerte, puede causar daños en estructuras débiles")
elif 6 <= mag and mag < 7:
    print("El sismo fue muy fuerte, puede causar daños significativos")
elif mag >= 7:
    print("El sismo fue extremo, puede causar graves daños a gran escala")

'''10) Utilizando la información aportada en la siguiente tabla sobre las 
estaciones del año Periodo del año. Escribir un programa que pregunte al
usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y
qué día es. El programa deberá utilizar esa información para imprimir por 
pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.'''

print("Ingrese en que hemisferio se encuentra (Norte/Sur): ")
hem=input().upper()
mes=input("Ingrese el mes actual: ").lower()
dia=int(input("Ingrese el día del mes: "))
if hem=="NORTE":
    if (mes=="marzo" and dia>=21) or (mes=="abril") or (mes=="mayo") or (mes=="junio" and dia<=20):
        print("Usted se encuentra en primavera")
    elif (mes=="junio" and dia>=21) or (mes=="julio") or (mes=="agosto") or (mes=="septiembre" and dia<=20):
        print("Usted se encuentra en verano")
    elif (mes=="septiembre" and dia>=21) or (mes=="octubre") or (mes=="noviembre") or (mes=="diciembre" and dia<=20):
        print("Usted se encuentra en otoño")
    elif (mes=="diciembre" and dia>=21) or (mes=="enero") or (mes=="febrero") or (mes=="marzo" and dia<=20):
        print("Usted se encuentra en invierno")
    else:
        print("El mes ingresado o dia, no es válido")
elif hem=="SUR":
    if (mes=="marzo" and dia>=21) or (mes=="abril") or (mes=="mayo") or (mes=="junio" and dia<=20):
        print("Usted se encuentra en otoño")
    elif (mes=="junio" and dia>=21) or (mes=="julio") or (mes=="agosto") or (mes=="septiembre" and dia<=20):
        print("Usted se encuentra en invierno")
    elif (mes=="septiembre" and dia>=21) or (mes=="octubre") or (mes=="noviembre") or (mes=="diciembre" and dia<=20):
        print("Usted se encuentra en primavera")
    elif (mes=="diciembre" and dia>=21) or (mes=="enero") or (mes=="febrero") or (mes=="marzo" and dia<=20):
        print("Usted se encuentra en verano")
    else:
        print("El mes ingresado o dia, no es válido")
else:
    print("Hemisferio incorrecto")



