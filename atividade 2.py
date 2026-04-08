def dias_para_atingir(N, R, P):
    """
    Calcula o número de dias necessários para atingir pelo menos P infectados.
    
    Parâmetros:
    N (int): infectados no dia 0
    R (int): fator reprodutivo
    P (int): número alvo de infectados
    
    Retorna:
    int: número de dias necessários
    """
    total = N
    infectados_no_dia = N
    dias = 0

    while total < P:
        infectados_no_dia *= R
        total += infectados_no_dia
        dias += 1

    return dias


def resolver_entrada():
    """
    Lê entrada padrão (estilo OBI) e imprime o resultado.
    """
    N = int(input().strip())
    R = int(input().strip())
    P = int(input().strip())

    print(dias_para_atingir(N, R, P))


def rodar_testes():
    """
    Executa testes básicos para validar o código.
    """
    testes = [
        # (N, R, P, resposta_esperada)
        (1, 5, 156, 3),
        (2, 1, 11, 5),
        (10, 2, 10, 0),   # já atingiu no dia 0
        (3, 2, 21, 2),
        (1, 1, 100, 99),  # crescimento linear
    ]

    print("Rodando testes...\n")
    for i, (N, R, P, esperado) in enumerate(testes, 1):
        resultado = dias_para_atingir(N, R, P)
        status = "✅ PASSOU" if resultado == esperado else "❌ FALHOU"
        
        print(f"Teste {i}: N={N}, R={R}, P={P}")
        print(f"Esperado: {esperado} | Obtido: {resultado} -> {status}\n")


if __name__ == "__main__":
    # Escolha o modo:
    
    # 1. Para rodar com entrada padrão (OBI):
    resolver_entrada()
    
    # 2. Para rodar testes (descomente abaixo):
    # rodar_testes()
