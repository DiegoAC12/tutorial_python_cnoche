# convertir tipos de datos
print("---conversion enteros en flotantes---")
entero =57
print(f"el entero es {entero} y su conversion a float es float(entero): {float(entero)}")


print("\n---conversion flotantes en enteros---")
flotante = 57.2
print(f"el flotante es {flotante} y su conversion a entero es int(flotante): {int(flotante)}")


print("\n---conversion de numero mediante division---")
a = 5/2
print(f"la division es 5/2, dando como resultado flotante {a}")


print("\n---conversion de numeros en cadenas usando str---")
#nombre = input("Escribe tu nombre: ")
#edad = int(input("Ingresa tu edad: "))
nombre = "Diego"
edad = 28
print(f"tu nombre es " + nombre + " y tu edad es " + str(edad) + " años")


print("\n---conversion de cadenas en numeros enteros---")
ano_actual = input("Ingresa el año actual: ")
ano_nacimiento = input("Ingresa el año de nacimiento: ")
edad = int(ano_actual) - int(ano_nacimiento)
print("tu edad es: ", edad)


print("\n---conversion de cadenas en numeros flotantes---")
ano_actual = input("Ingresa el año actual: ")
ano_nacimiento = input("Ingresa el año de nacimiento: ")
edad = float(ano_actual) - float(ano_nacimiento)
print("tu edad es: ", edad)
