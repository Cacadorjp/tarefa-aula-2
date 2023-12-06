# Escreva um programa que peça ao usuário inserir duas notas (entre 0 e 100) e determine se o aluno passou ou não.
# Um aluno passa se a soma das notas for maior ou igual a 60 e nenhuma nota é menor que 40.

tentativas = 1

print("Insira suas notas da 1° e 2° prova do 1° bimestre.")

while tentativas < 3:
    n1 = int(input("Informe sua 1° nota: "))
    if n1 >= 40 and n1 <= 100:
        n2 = int(input("Informe sua 2° nota: "))
        if n2 >= 40 and n2 <= 100:
            n1 + n2
            if n1 + n2 >= 60:
                print("Você foi aprovado(a)")
            else:
                print("Você foi reprovado(a)")
        else:
            tentativas += 1

    elif tentativas == 1:
        print("Você tem mais 2 chance de colocar a nota correta. Insira sua nota novamente: ")

    elif tentativas == 2:
        print("Você tem mais 1 chance de colocar a nota correta. Insira sua nota novamente: ")

    else:
        print("Acabaram suas tentativas. Tente novamente mais tarde.")
        tentativas += 1