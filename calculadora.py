def soma(numero1, numero2):
    print("-=--=-=-=-==-=-=-=-=-=-=--=-=")
    print("O resultado é {}".format(numero1 + numero2))
    print("-=--=-=-=-==-=-=-=-=-=-=--=-=")
def subtracao(numero1, numero2):
    print("-=--=-=-=-==-=-=-=-=-=-=--=-=")
    print("O resultado é {}".format(numero1 - numero2))
    print("-=--=-=-=-==-=-=-=-=-=-=--=-=")
def divisao(numero1, numero2):
    print("-=--=-=-=-==-=-=-=-=-=-=--=-=")
    print("O resultado é {}".format(numero1 / numero2))
    print("-=--=-=-=-==-=-=-=-=-=-=--=-=")
def multiplicacao(numero1, numero2):
    print("-=--=-=-=-==-=-=-=-=-=-=--=-=")
    print("O resultado é {}".format(numero1 + numero2))
    print("-=--=-=-=-==-=-=-=-=-=-=--=-=")


while(1):
    print("Escolha uma das opções abaixo")
    print("[1]SOMA")
    print("[2]SUBTRAÇÃO")
    print("[3]DIVISÃO")
    print("[4]MULTIPLICAÇÃO")
    print("[5]SAIR")
    opcao = int(input("Sua escolha: "))

    if(opcao == 5):
        print("Saindo...")
        exit()
    elif(opcao<6):
        numero1 = int(input("Digite o primeiro valor: "))
        numero2 = int(input("Digite o segundo valor: "))
    else:
        print("-=--=-=-=-==-=-=-=-=-=-=--=-=")
        print("Valor invalido")
        print("-=--=-=-=-==-=-=-=-=-=-=--=-=")


    if(opcao == 1):
        soma(numero1, numero2)
    elif(opcao == 2):
        subtracao(numero1, numero2)
    elif(opcao == 3):
        divisao(numero1, numero2)
    elif(opcao == 4):
        multiplicacao(numero1, numero2)
        