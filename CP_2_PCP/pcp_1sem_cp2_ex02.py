#CP-2
def ordena_valor(a, b, c):
    if b > a:
        temp = a
        a = b
        b = temp

    if c > a:
        temp = a
        a = c
        c = temp

    if c > b:
        temp = b
        b = c
        c = temp
    return a,b,c

valorA = float(input("Digite o Valor de (A): "))
valorB = float(input("Digite o Valor de (B): "))
valorC = float(input("Digite o Valor de (C): "))

valorA, valorB, valorC = ordena_valor(valorA, valorB, valorC)


print('\n' + '='*30)
print(f"Ordenando em ordem Decrescente: A:{valorA} e B:{valorB} e C:{valorC}")
print()
if valorA >= valorB + valorC:
    print ("NAO FORMA TRIANGULO")
else:
    if valorA**2 == valorB**2 + valorC**2:
        print("TRIANGULO RETANGULO")
    elif valorA**2 > valorB**2 + valorC**2:
        print("TRIANGULO OBTUSANGULO")
    elif valorA**2 < valorB**2 + valorC**2:
        print("TRIANGULO ACUTANGULO")
    if valorA == valorB == valorC:
        print("TRIANGULO EQUILATERO")
    elif valorA == valorB or valorA == valorC or valorC == valorB:
        print("TRIANGULO ISOSCELES")
print('='*30)