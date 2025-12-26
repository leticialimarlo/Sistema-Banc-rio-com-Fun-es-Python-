import textwrap

# Constantes de Interface
BARRA = "=" * 45
ALERTA = "@@@"
SUCESSO = "==="

def depositar(saldo, valor, extrato, /):
    """Realiza o depósito (Positional-only)."""
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"\n{SUCESSO} Depósito realizado com sucesso! {SUCESSO}")
    else:
        print(f"\n{ALERTA} Operação falhou! O valor informado é inválido. {ALERTA}")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Realiza o saque (Keyword-only)."""
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(f"\n{ALERTA} Operação falhou! Você não tem saldo suficiente. {ALERTA}")
    elif excedeu_limite:
        print(f"\n{ALERTA} Operação falhou! O valor excede o limite. {ALERTA}")
    elif excedeu_saques:
        print(f"\n{ALERTA} Operação falhou! Número máximo de saques excedido. {ALERTA}")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\n{SUCESSO} Saque realizado com sucesso! {SUCESSO}")
    else:
        print(f"\n{ALERTA} Operação falhou! O valor informado é inválido. {ALERTA}")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    """Exibe o extrato formatado."""
    print(f"\n{BARRA} EXTRATO {BARRA}")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print(f"{BARRA}")

def filtrar_usuario(cpf, usuarios):
    """Localiza usuário pelo CPF."""
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    """Cadastra um novo usuário."""
    # Sanitização: remove caracteres não numéricos para evitar duplicidade por formatação
    cpf = input("Informe o CPF (somente número): ").strip().replace(".", "").replace("-", "")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f"\n{ALERTA} Já existe usuário com esse CPF! {ALERTA}")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome, 
        "data_nascimento": data_nascimento, 
        "cpf": cpf, 
        "endereco": endereco
    })
    print(f"\n{SUCESSO} Usuário criado com sucesso! {SUCESSO}")

def criar_conta(agencia, numero_conta, usuarios):
    """Cria uma conta corrente vinculada a um usuário."""
    cpf = input("Informe o CPF do usuário: ").strip().replace(".", "").replace("-", "")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f"\n{SUCESSO} Conta criada com sucesso! {SUCESSO}")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print(f"\n{ALERTA} Usuário não encontrado, fluxo de criação de conta encerrado! {ALERTA}")

def listar_contas(contas):
    """Lista todas as contas formatadas."""
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 45)
        print(textwrap.dedent(linha))

def menu():
    menu_str = f"""
    {BARRA} MENU {BARRA}
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_str)).lower()

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        try:
            if opcao == "d":
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)

            elif opcao == "s":
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato, numero_saques = sacar(
                    saldo=saldo, valor=valor, extrato=extrato,
                    limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES,
                )

            elif opcao == "e":
                exibir_extrato(saldo, extrato=extrato)

            elif opcao == "nu":
                criar_usuario(usuarios)

            elif opcao == "nc":
                # Lógica idêntica à imagem b1a961.png
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)
                if conta:
                    contas.append(conta)

            elif opcao == "lc":
                listar_contas(contas)

            elif opcao == "q":
                print("Obrigado por utilizar nosso sistema!")
                break
            
            else:
                print(f"\n{ALERTA} Operação inválida. {ALERTA}")

        except ValueError:
            print(f"\n{ALERTA} Erro: Informe apenas números para valores monetários. {ALERTA}")

if __name__ == "__main__":
    main()