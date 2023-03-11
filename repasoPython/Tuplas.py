# Tuplas
# Son parecidas a las listas, pero estas son listas inmutables, es decir, no se pueden añadir, ni modificar elementos.
# Las tuplas van en parentesis, a diferencia de las listas que van en corchetes
print("Ejemplo de tupla")
tupla1 = (4, "Hola", 1, [1,2,3])
print(tupla1)

print("\nMostrar el elemento especifico de las tuplas")
print(tupla1[0])

print(f"\nMostrar varios elementos de las tuplas {tupla1}")
print(tupla1[0:3])

print(f"\nBuscar elementos de las tuplas {tupla1}")
print(tupla1.index("Hola"))

