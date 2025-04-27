def validar_nota(nota):
    # define se a nota é válida
    if 0 <= nota <= 10:
        return True
    else:
        return False


def calcular_media(n1, n2, pim):
    # calcula a média das notas
    return (n1 * 0.4 + n2 * 0.4 + pim * 0.2)


def verificar_aprovacao(media):
    # verifica se o aluno foi aprovado
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


def main():
    print("Bem-vindo ao medidor de notas ;D")
    # Solicitação de notas
    while True:
        try:
            n1 = float(input("Digite a nota da N1 (0 a 10): "))
            if not validar_nota(n1):
                print("Nota inválida, digite novamente.")
                continue

            n2 = float(input("Digite a nota da N2 (0 a 10): "))
            if not validar_nota(n2):
                print("Nota inválida, digite novamente.")
                continue

            pim = float(input("Digite a nota do PIM (0 a 10): "))
            if not validar_nota(pim):
                print("Nota inválida, digite novamente.")
                continue

            break  # Sai do loop se as notas forem válidas
        except ValueError:
            print("Valor inválido, digite novamente.")
            continue

    # Calcula a média e verifica aprovação
    media = calcular_media(n1, n2, pim)
    print(f"Sua média é: {media:.2f}")
    print(verificar_aprovacao(media))



if __name__ == "__main__":

    main()

