n =int(input("Ingrese el termino de la serie a mostrar: "))
a, b = 0, 1
contador = 0
while contador < n:
    print(a)
    a, b = b, a + b
    contador += 1