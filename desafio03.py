# Verifique se uma pessoa é maior ou igual a 18 anos ou se ela tem autorização dos pais.

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento

digite = int(input("Tem autorização dos pais? Digite 1 para sim e 2 para não."))

if idade >= 18:
    print("Você é maior de idade. Sua idade é:", idade)
else:
    print("Você não é maior de idade. Sua idade é:", idade)
    if digite == 1:
        print("Sim.")
    elif digite == 2:
        print("Não.")
    else:
        print("Não tem essa opção. Recomece!")