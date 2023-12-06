# Escreva um código que verifique se uma pessoa é alfabetizada (sabe ler e escrever) e tem mais de 25 anos de idade.

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento


alfabetizado = int(input("Você é alfabetizado, sim ou não? Digite 1 para sim e 2 para não: "))
if alfabetizado == 1:
    print("Sim.")
elif alfabetizado == 2:
    print("Não.")
elif alfabetizado != 1 and 2:
    print("Não existe essa opção, marque novamente!")

if idade >= 25:
    print("Você tem 25 anos ou mais. Sua idade é: ", idade)
else:
    print("Você ainda não tem 25 anos. Sua idade é: ", idade)
