# funciones

def miFuncion():
    print("Hola Mundo")


miFuncion()

def mostrarNombre(nombre, apellido):
    print("Su nombre es: " + nombre + " " + apellido)


mostrarNombre("Diego", "Alzate")

# datos de entrada = b y h
base = 9
altura = 12
#proceso
def calcularAreaTriangulo(b, h):
    area = (b * h)/2
    return area

# Salida
resultado = calcularAreaTriangulo(base, altura)
print("El área del triangulo es: ", resultado)

# ----------------------------------------
# Datos de entrada por teclado
# ----------------------------------------

# datos de entrada = b y h
base = float(input("Ingrese una base: ")) # De esta manera pedimos por teclado
altura = float(input("Ingrese la altura: "))
#proceso
def calcularAreaTriangulo(b, h):
    area = (b * h)/2
    return area

# Salida
resultado = calcularAreaTriangulo(base, altura)
print("El área del triangulo es: ", resultado)

def mostrarMensaje(pais="Colombia"):
    print("Yo soy: ", pais)

# Las funciones a las cuales no se les pasa ningun valor, toma el valor por defecto
mostrarMensaje("Suiza")
mostrarMensaje("Ecuador")
mostrarMensaje()
mostrarMensaje("Bolivia")