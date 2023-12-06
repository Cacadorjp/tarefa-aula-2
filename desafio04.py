# Escreva um código que verifique se um número é par ou divisível por 3.

numero = int(input("Digite um número para verificar se é divisível por 3: "))
if numero == 0:
    print("0 é divisível por todos os números")
elif numero % 3 == 0:
    print("O número é divisível por 3.")
else:
    print("O número não é divisível por 3.")