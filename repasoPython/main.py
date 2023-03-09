# Tipos de datos
# Numero enteros
# Tipado estático
numero1: int = 70
# Tipado dinamico
numero2 = 45
print("--------Enteros-----")
print(numero1)
print(numero2)

# numeros reales
# tipado estatico
numero3: float = 4.9

# tipado dinamico
numero4 = 5.0

print("--------Reales-----")
print(numero3)
print(numero4)

# Booleanos
esColombiano: bool = True
esArgentino = False

print("--------Booleanos-----")
print(esColombiano)
print(esArgentino)

# Caracter y cadena de caracteres
print("--------Cadena de caracteres-----")
mensaje = "cadena con una casilla simple', una comilla doble\", y una diagonal invertida\\"
print(mensaje)

# ----------------------------------------------------------
# Operadores
# Aritmeticos
numero5 = 100
numero6 = 50
suma = numero5 + numero6
resta = numero5 - numero6
multiplicacion = numero5 * numero6
division = numero5 / numero6
modulo = numero5 % numero6

print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicación es: ", multiplicacion)
print("La division es: ", division)
print("El modulo es: ", modulo)

# Asignacion
x = 5
y = 7
z = 3

# Lógicos
# AND = Y
print("---------Lógicos AND-------------")
p = 5
print(p > 4 and p < 9)
print("---------Lógicos OR-------------")
p = 5
print(p < 7 or p < 9)
print("---------Lógicos NOT-------------")
p = 5
print(not(p > 2 and p < 7))
print("---------------------------------")

# Relacionales o de comparacion
edad1 = 23
edad2 = 18

print(edad1 == edad2) # igualdad
print(edad1 > edad2) # mayor que
print(edad1 < edad2) # menor que
print(edad1 >= edad2) #mayor igual que
print(edad1 <= edad2) #menor igual que
print(edad1 != edad2) #diferente o no igual


