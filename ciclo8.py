numero = int(input("Ingrese el numero a calcular: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
    
print(f"El factorial de {numero} es:", factorial)