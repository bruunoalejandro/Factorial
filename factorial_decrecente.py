print("Ingrese un numero: ")
x = int(input())
if x >= 0:
    fact = 1
    i = x
    while i >= 1:
        fact = fact * i
        i = i - 1
        print(fact)
else:
            print("El valor debe ser positivo")
