import random
import math
import string


def GeradorDeSenha():
    print('----GERADOR DE SENHA----')
    tamanho = int(input('Informe quantos digitos a sua senha deve ter: '))
    caracteres = string.ascii_letters + string.digits + string.punctuation

    senha = ""

    for i in range(tamanho):
        senha += random.choice(caracteres)
    print(f'Senha gerada: {senha}\n')
    return MenuInterativo()


def Fibonacci():
    print('\n---- FIBONACCI ----')
    fibo = int(input('Insira até qual posição da sequencia fibonacci você quer ver: '))
    a = 0
    b = 1

    for i in range(fibo):
        print(a)
        a, b = b, a + b
    MenuInterativo()


def Jokenpo():
    print('\n---- JOKENPÔ ----')

    opcoes = ["pedra", "papel", "tesoura"]
    jogador_p = 0
    cpu_p = 0
    empates = 0

    while True:
        print(f'Vitorias do player: {jogador_p} || Vitorias do computador: {cpu_p} || Empates: {empates}\n')
        jogador = input('Escolha pedra, papel ou tesoura: \n').lower()

        if jogador not in opcoes:
            print('Digite apenas pedra, papel ou tesoura!\n')
            continue

        cpu = random.choice(opcoes)

        print(f'\nComputador escolheu: {cpu}')

        if jogador == cpu:
            print('\nEmpate!\n')
            empates += 1
        elif jogador == "pedra" and cpu == "tesoura":
            print('\nVocê ganhou essa rodada!\n')
            jogador_p += 1
        elif jogador == "tesoura" and cpu == "papel":
            print('\nVocê ganhou essa rodada!\n')
            jogador_p += 1
        elif jogador == "papel" and cpu == "pedra":
            print('\nVocê ganhou essa rodada!\n')
            jogador_p += 1
        else:
            print('\nO computador ganhou essa rodada!\n')
            cpu_p += 1

        if jogador_p == 3:
            print('Parabens! Você ganhou a partida! :)')
            print(f'Placar final: {jogador_p} a {cpu_p}')
            print(f'Empates totais: {empates}\nAté a próxima!')
            return MenuInterativo()
            break
        if cpu_p == 3:
            print('Que pena! talvez na próxima partida você ganhe! :(')
            print(f'Placar final: {jogador_p} a {cpu_p}')
            print(f'Empates totais: {empates}\nAté a próxima!')
            return MenuInterativo()
            break


def CalcularPrimo():
    print('\n---- CALCULAR SE É PRIMO ----')

    while True:
        try:
            np = int(input('Informe um número inteiro: '))
            break
        except ValueError:
            print('Informe apenas números inteiros!')

    if np <= 1:
        return False

    for i in range(2, int(math.sqrt(np)) + 1):
        if np % i == 0:
            return False

    return True


def CalcularParOuImpar():
    print('\n---- PAR ou IMPAR ----')
    while True:
        try:
            npi = int(input('Informe um número para saber se é par ou impar: '))
            break
        except ValueError:
            print('Insira apenas números!')

    if npi % 2 == 0:
        print(f'O número {npi} é Par!')
        MenuInterativo()
    else:
        print(f'O número {npi} é Impar!')
        MenuInterativo()


def NomePalindromo():
    print('\n---- PALINDROMO ----')
    while True:

        nome = str(input('Insira um nome: '))

        if nome.replace(" ", "").isalpha():
            break
        else:
            print('Insira apenas Letras!')

    nome_limpo = nome.replace(" ", "").lower()

    if nome_limpo == nome_limpo[::-1]:
        print(f'O nome {nome} é um palindromo!')
        MenuInterativo()

    else:
        print(f'O nome {nome} não é um palindromo!')
        MenuInterativo()


def Tabuada():
    print('\n---- TABUADA ----')
    t_nu = int(input('Insira um número para ver a tabuada: '))
    for i in range(1, 11):
        print(f'{t_nu} x {i} = {t_nu * i}')
    MenuInterativo()


def Calculadora():
    print('\n---- CALCULADORA ----')
    while True:

        try:
            n1 = float(input('Insira o primeiro número: '))

            n2 = float(input('Insira o segundo número: '))

            operacoes = int(input('1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Potenciação\nEscolha a operação: '))
            match operacoes:
                case 1:
                    print('A soma dos números {} e {} é: {}'.format(n1, n2, n1 + n2))
                    MenuInterativo()
                    break

                case 2:
                    print('A subtração dos números {} e {} é: {}'.format(n1, n2, n1 - n2))
                    MenuInterativo()
                    break

                case 3:
                    print('A divisão dos números {} e {} é: {}'.format(n1, n2, n1 / n2))
                    if n2 == 0 or n1 == 0:
                        print('Não é possivel dividir zero!\n')
                    MenuInterativo()
                    break

                case 4:
                    print('A potenciação dos números {} e {} é: {}'.format(n1, n2, n1 ** n2))
                    MenuInterativo()
                    break


        except ValueError:
            print('Insira apenas números!')


def MenuInterativo():
    print('\n---- MENU ----')
    print('\nBem vindo ao menu interativo - Teste\nEscolha a opção no menu utilizando números inteiros apenas!\n')
    while True:
        try:
            opcoes = int(input(
                '1 - Calcular se é Número Primo\n2 - Calculadora Simples\n3 - Calcular se o número é par ou impar\n4 - Descobrir se um Nome é um Palindromo\n5 - Jogar Jokenpô\n6 - Tabuada\n7 - Sequencia Fibonacci\n8 - Gerador de Senha\n9 - Encerrar\nOpção escolhida: \n'))

            match opcoes:
                case 1:
                    if CalcularPrimo():
                        print("É primo!")
                        MenuInterativo()
                    else:
                        print("Não é primo!")
                        MenuInterativo()

                    break
                case 2:
                    Calculadora()

                    break
                case 3:
                    CalcularParOuImpar()

                    break
                case 4:
                    NomePalindromo()

                    break
                case 5:
                    Jokenpo()
                    break
                case 6:
                    Tabuada()
                    break
                case 7:
                    Fibonacci()
                    break
                case 8:
                    GeradorDeSenha()
                    break
                case 9:
                    print('Obrigado por usar o menu interativo em fase de teste!')
                    break
                case _:
                    print('Opção inválida, tente novamente!\n')


        except ValueError:
            print('Valor inválido, utilize apenas números inteiros!')


MenuInterativo()
