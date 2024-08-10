n = int(input("Ingrese el largo de la piramide: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))