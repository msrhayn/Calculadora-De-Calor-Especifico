def calcular_calor_especifico(Q, m, delta_T):
    if m == 0 or delta_T == 0:
        raise ValueError("A massa e a variação de temperatura devem ser diferentes de 0")
    c = Q / (m * delta_T)
    return c

def main():
    print("Calculadora de calor específico")
    try:
        Q = float(input("Digite a quantidade de calor (Q) em Joules: "))
        m = float(input("Digite a massa (m) em kg: "))
        delta_T = float(input("Digite a variação de temperatura (ΔT) em °C: "))
        c = calcular_calor_especifico(Q, m, delta_T)
        print(f"O calor específico (c) é: {c:.2f}J/(kg °C)")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
