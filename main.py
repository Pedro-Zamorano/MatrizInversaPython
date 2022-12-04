# 1.- Definir el tamaño de la matriz (n*n)
n = int(input("Ingresa el tamaño de la matriz: "))

matriz = []
for i in range(n):
    matriz.append([0] * n)

print(f"\nEsta es la matriz:\n{matriz}")
print("\n")

# 2.- Pedir datos al usuario para crear la matriz
for j in matriz:
    print(j)


