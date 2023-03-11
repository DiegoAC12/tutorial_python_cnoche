# Diccionarios
# Estos diccionarios son otro tipo de colección donde los elementos se guardan desordenados
# Tiene dos elemetos principales: la clave y el valor.
print("--- Diccionario ---")
diccionario1 = {}
print(diccionario1)

print("\n--- Diccionario ejemplo ---")
diccionario2 = {"Azul":"blue", "Amarillo":"Yellow", "Rojo":"Red"}
print(diccionario2)

print("\n--- Buscar los elemento de un Diccionario con su valor ---")
print(diccionario2["Amarillo"])

print(f"\n--- Agregar nuevos elementos a un Diccionario {diccionario2} ---")
diccionario2["verde"] = "green"
print(diccionario2)

print(f"\n--- Modificar elementos a un Diccionario {diccionario2} ---")
diccionario2["Azul"] = "BLUE"
print(diccionario2)

print(f"\n--- Eliminar elementos a un Diccionario {diccionario2} ---")
del(diccionario2["Azul"])
print(diccionario2)

print("\n--- Crear diccionarios con listas ---")
diccionario3 = {"Diego":[28,1.75], "Fernando":[29,1.80]}
print(diccionario3)

print("\n--- Crear diccionarios con diccionarios dentro ---")
diccionario4 = {"Diego":{"edad":28,"Estatura":1.75}, "Fernando":{"edad":29,"Estatura":1.80}}
print(diccionario4)
print(diccionario4["Diego"])


