# Estructura repetitiva while
print("----While----")

contador = 0
while contador < 4:
    contador += 1
    print(contador)

print("----------Otra forma de while-----------")
numero1 = int(input("Ingrese un numero maximo a contar: "))
contador = 0

def estructuraWhile(num1, cont):
    while cont < num1:
        cont += 1
        print(str(cont))


estructuraWhile(numero1, contador)

print("----------Otra forma de while-----------")

numero2 = int(input("Ingresa un numero menor a 30: "))
def estructuraWhile2(num2):
    while num2 > 30:
        num2 = int(input(("El numero ingresado es mayor a 30 \nIngrese un numero menor a 30: ")))
    print("Correcto, el numero '" + str(num2) + "' es menor o igual a 30 ") # una manera de concatenar
    print(f"Correcto, el numero '{num2}' es menor o igual a 30 ") # otra manera de concatenar


estructuraWhile2(numero2)

# Do while
print("----------for-----------")

coleccion = [1,2,8,10]
def estructuraFor(c):
    for i in c:
        print(i)


estructuraFor(coleccion)

print("----------tabla de multiplicar------------")
numero3 = int(input("Ingrese numero a multiplicar: "))
def tablaFor(num3):
    for i in range(0,11):
        tabla=num3 * i
        print(f" {num3} * {i} = ", tabla)


tablaFor(numero3)

print("\n---leer n triangulos---")
can1 = 0
can2 = 0
can3 = 0
numero4 = int(input("Ingrese la cantidad de triángulos: "))
def triangulo(num, cant1, cant2, cant3):
    for f in range(num):
        lado1 = int(input("Ingrese lado primer lado: "))
        lado2 = int(input("Ingrese lado segundo lado: "))
        lado3 = int(input("Ingrese lado tercer lado: "))
        if lado1 == lado2 and lado1 == lado3:
            print("Es un triangulo equilatero.")
            cant1 = cant1 + 1
        else:
            if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                print("Es un triángulo isosceles.")
                cant2 = cant2 + 1
            else:
                print("Es un triángulo escaleno.")
                cant3 = cant3 + 1

    print("Cantidad de triángulos equilateros: ", cant1)
    print("Cantidad de triángulos isósceles:   ", cant2)
    print("Cantidad de triángulos escalenos:   ", cant3)


triangulo(numero4, can1, can2, can3)