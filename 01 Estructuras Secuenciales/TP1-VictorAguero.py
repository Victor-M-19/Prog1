#Práctico 1: Estructuras secuenciales
#Alumno: Victor Agüero
'''1) Crear un programa que imprima por pantalla 
el mensaje: “Hola Mundo!”.'''

print("Hola Mundo!")

'''2) Crear un programa que pida al usuario su nombre e imprima por pantalla
 un saludo usando el nombre ingresado. 
 Por ejemplo: si el usuario ingresa “Marcos”, 
 el programa debe imprimir por pantalla “Hola Marcos!”.'''

nombre=input("ingrese su nombre: ")
print(f"Hola!! {nombre}, como estas?")

'''3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima
por pantalla una oración con los datos ingresados.
Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”,
el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”.'''

nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=input("Ingrese su edad: ")
lugar_residencia=input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")

'''4) Crear un programa que pida al usuario el radio de un círculo e imprima
 por pantalla su área y su perímetro.'''

radio=float(input("Ingrese el radio del círculo: "))
area=3.14*radio**2
perimetro=2*3.14*radio
print("El área del círculo es: ", area)
print("El perímetro del círculo es: ", perimetro)

'''5) Crear un programa que pida al usuario una cantidad de segundos e imprima 
por pantalla a cuántas horas equivale.'''

seg=int(input("Ingrese una cantidad de segundos: "))
horas=seg/3600
print(f"{seg} segundos equivalen a {horas} horas.")

'''6) Crear un programa que pida al usuario un número e imprima 
por pantalla la tabla de multiplicar de dicho número.'''

n=int(input("Ingrese un número: "))
print(f"Tabla de multiplicar del {n}: ")
print(f"{n}*0 =",n*0,"\n", f"{n}*1 =",n*1,"\n", f"{n}*2 =",n*2,"\n", f"{n}*3 =",n*3,"\n", f"{n}*4 =",n*4,"\n", f"{n}*5 =",n*5,"\n",
       f"{n}*6 =",n*6,"\n", f"{n}*7 =",n*7,"\n", f"{n}*8 =",n*8,"\n", f"{n}*9 =",n*9,"\n", f"{n}*10 =",n*10)

'''7) Crear un programa que pida al usuario dos números enteros 
distintos del 0 y muestre por pantalla el resultado de sumarlos,
 dividirlos, multiplicarlos y restarlos.'''

m=int(input("Ingrese el primer número entero distinto de 0: "))
n=int(input("Ingrese el segundo número entero distinto de 0: "))
print(f"La suma de {m} y {n} es: {m+n}")
print(f"La resta de {m} y {n} es: {m-n}")
print(f"La multiplicación de {m} y {n} es: {m*n}")
print(f"La división de {m} y {n} es: {m/n}")

'''8) Crear un programa que pida al usuario su altura y 
su peso e imprima por pantalla su índice de masa corporal.'''

altura=float(input("Ingrese su altura en metros: "))
peso=float(input("Ingrese su peso en kilogramos: "))
imc=peso/(altura**2)
print(f"Su índice de masa corporal es: {imc:.2f} kg/m²")

'''9) Crear un programa que pida al usuario una temperatura
 en grados Celsius e imprima por pantalla 
 su equivalente en grados Fahrenheit.'''

c=float(input("Ingrese la temperatura en grados Celsius: "))
f=(c * 1.8) + 32
print(f"{c} grados Celsius equivalen a {f} grados Fahrenheit.")

'''10) Crear un programa que pida al usuario 3 números e imprima
 por pantalla el promedio de dichos números.'''

a=input("Ingrese el primer número: ")
b=input("Ingrese el segundo número: ")
c=input("Ingrese el tercer número: ")
promedio=((float(a) + float(b) + float(c)) / 3)
print(f"El promedio de los números {a}, {b} y {c} es: {promedio:.2f}")