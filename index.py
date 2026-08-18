def calcular_media(np1, np2, pim):
    return ((np1 * 4) + (np2 * 4) + (pim * 2)) / 10


def cadastro_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")

    np1 = float(input("Digite a nota da NP1: "))
    np2 = float(input("Digite a nota da NP2: "))
    pim = float(input("Digite a nota do PIM: "))

    if not (0 <= np1 <= 10 and 0 <= np2 <= 10 and 0 <= pim <= 10):
        print("As notas devem estar entre 0 e 10.")
        return

    media = calcular_media(np1, np2, pim)
    situacao = "Aprovado" if media >= 7 else "Reprovado"

    print("\n--- Dados do aluno ---")
    print(f"Nome: {nome}")
    print(f"Matrícula: {matricula}")
    print(f"NP1: {np1}")
    print(f"NP2: {np2}")
    print(f"PIM: {pim}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


cadastro_aluno()
