from typing import List, Tuple


def depositar(saldo: float, valor: float, extrato: List[str]) -> Tuple[float, List[str], str]:
    """Deposita um valor positivo em `saldo` e registra no `extrato`.
d
    Retorna (saldo_atualizado, extrato_atualizado, mensagem).
    """
    if valor <= 0:
        return saldo, extrato, "Operação falhou! O valor informado é inválido."

    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")
    return saldo, extrato, "Depósito realizado com sucesso!"


def sacar(
    saldo: float,
    valor: float,
    extrato: List[str],
    limite: float,
    numero_saques: int,
    limite_saques: int,
) -> Tuple[float, List[str], int, str]:
    """Tenta sacar um valor, respeitando `saldo`, `limite` e `limite_saques`.

    Retorna (saldo_atualizado, extrato_atualizado, numero_saques_atual, mensagem).
    """
    if valor <= 0:
        return saldo, extrato, numero_saques, "Operação falhou! O valor informado é inválido."

    if valor > saldo:
        return saldo, extrato, numero_saques, "Operação falhou! Você não tem saldo suficiente."

    if valor > limite:
        return saldo, extrato, numero_saques, "Operação falhou! O valor do saque excede o limite."

    if numero_saques >= limite_saques:
        return saldo, extrato, numero_saques, "Operação falhou! Número máximo de saques excedido."

    saldo -= valor
    extrato.append(f"Saque: R$ {valor:.2f}")
    numero_saques += 1

    return saldo, extrato, numero_saques, "Saque realizado com sucesso!"


def exibir_extrato(saldo: float, extrato: List[str]) -> str:
    """Retorna uma string formatada do extrato e saldo para exibição no CLI."""
    linhas = ["================ EXTRATO ================"]
    if not extrato:
        linhas.append("Não foram realizadas movimentações.")
    else:
        linhas.extend(extrato)

    linhas.append(f"\nSaldo: R$ {saldo:.2f}")
    linhas.append("==========================================")

    return "\n" + "\n".join(linhas) + "\n"


LIMITE_SAQUE = 500.0
LIMITE_SAQUES = 3


def main() -> None:
    saldo = 0.0
    limite = LIMITE_SAQUE
    extrato: List[str] = []
    numero_saques = 0

    menu = """[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
            except ValueError:
                print("Valor inválido. Tente novamente.")
                continue

            saldo, extrato, mensagem = depositar(saldo, valor, extrato)
            print(mensagem)

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
            except ValueError:
                print("Valor inválido. Tente novamente.")
                continue

            saldo, extrato, numero_saques, mensagem = sacar(
                saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES
            )
            print(mensagem)

        elif opcao == "e":
            print(exibir_extrato(saldo, extrato))

        elif opcao == "q":
            print("Encerrando sistema. Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
