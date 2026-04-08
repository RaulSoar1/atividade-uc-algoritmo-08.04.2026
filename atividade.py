def calcular_pontos(p, d, b):
    return p * 1 + d * 2 + b * 3

def determinar_premio(pontos):
    if pontos >= 150:
        return 'B'
    elif pontos >= 120:
        return 'D'
    elif pontos >= 100:
        return 'P'
    else:
        return 'N'

def nome_premio(letra):
    if letra == 'B':
        return "Bolo"
    elif letra == 'D':
        return "Doce"
    elif letra == 'P':
        return "Pão"
    else:
        return "Nenhum"

def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("Digite um número não negativo!")
            else:
                return valor
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

def main():
    print("=== Sistema de Pontuação da ONG ===")

    P = ler_inteiro("Quantidade de pães: ")
    D = ler_inteiro("Quantidade de doces: ")
    B = ler_inteiro("Quantidade de bolos: ")

    pontos = calcular_pontos(P, D, B)
    premio = determinar_premio(pontos)

    print("\nPontuação total:", pontos)
    print("Prêmio:", nome_premio(premio))

if __name__ == "__main__":
    main()
