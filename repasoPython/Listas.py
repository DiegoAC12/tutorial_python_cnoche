# Listas
print("Lista 1")
lista1 = [1,1,2,2,3,4,5]
print(lista1)

print("\nLista 2")
lista2 = ["Lunes", "Martes", "Miercoles", "Jueves", "Vernes"]
print(lista2)

print("\nLista 3")
lista3 = ["Lunes", 1, "Miercoles", 2, "Vernes"]
print(lista3)

print("\n---Impresión el primer elemento de la lista 2---")
print(lista2[1])

print("\n---Impresión de dos elementos especificos de la lista 2---")
print(lista2[1], lista2[3])

print("\n---Impresión de varios elementos de la lista 2---")
print(lista2[0:4])

print("\n---Listas dentro de otra lista---")
lista4 = [1,2,3,[1,2,3]]
print(lista4)
print(len(lista4))

print("\n---Agregar elementos a una lista---")
print("Agregar elementos a la ultima posicion de la lista")
lista5 = [1,2,4,5]
lista5.append(6)
print(lista5)
print("\nAgregar elementos a una posicion especifica de la lista")
lista5.insert(2,3)
print(lista5)
print("\nAgregar elementos concatenando a la lista")
lista5.extend([7,8,9])
print(lista5)

print("\nSumar listas")
lista6 = [1,2,3]
lista7 = [1,2,3]

sumaListas = lista6 + lista7
print(sumaListas)

print(f"\n--Buscar elementos de las lista1 {lista1}--")
print(3 in lista1)

print(f"\nBuscar en qué índice se encuentra un elemento de la lista1 {lista1}")
print(lista1.index(4))

print(f"\n--Contar cuantas veces aparece un elemento de las lista1 {lista1}--")
print(lista1.count(1))
print(lista1.count(2))

print(f"\n--Eliminar un elemento de las lista1 {lista1}--")
lista1.pop(3)
print(lista1)

print(f"\n--Eliminar un elemento de las lista1 {lista1} en un lugar especifico--")
lista1.remove(3)
print(lista1)

print(f"\n--Eliminar toda la lista1 {lista1}--")
lista1.clear()
print(lista1)


