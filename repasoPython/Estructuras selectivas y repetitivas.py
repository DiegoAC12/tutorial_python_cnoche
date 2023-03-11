# ----Estructura selectiva simple-----
print("----------------Estructura selectiva simple-------------------")
numero1 = 200
numero2 = 100

def estructuraSelectivaSimple(num1, num2):
    if num1 > num2:

        return num1


mensaje=int(estructuraSelectivaSimple(numero1, numero2))
print("El numero mayor es: ", mensaje)

# ----Estructura selectiva doble-----
print("----------------Estructura selectiva doble-------------------")
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro numero: "))

def estructuraSelectivaDoble(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


mensaje=int(estructuraSelectivaDoble(numero1, numero2))
print("El numero mayor es: ", mensaje)

# ----Estructura selectiva multiple-----
print("----------------Estructura selectiva multiple-------------------")
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro numero: "))

def estructuraSelectivaMult(num1, num2):
    if num1 > num2:
        print("El numero mayor es, " + str(num1))
        return num1
    elif num1 < num2:
        print("El numero mayor es, " + str(num2))
        return num2
    else:
        return print("El numero es igual")


estructuraSelectivaMult(numero1, numero2)
