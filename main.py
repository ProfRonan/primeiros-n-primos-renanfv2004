numero = input("digite um número inteiro")
numero = int(numero)
contador = 0
a = 2
while contador != numero:
    b = 2
    primo = True
    while b < a:
        if a % b == 0 and a != b:
            primo = False
            break
        b = b + 1
    if primo:
        contador += 1
        print(a)
    a = a + 1
