import textwrap

# Constantes de Configuração
BARRA = "=" * 45
ALERTA = "@@@"
SUCESSO = "==="

def depositar(saldo, valor, extrato, /):
    """Realiza o depósito de forma posicional."""
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t\tR$ {valor:>8.2f}\n"
        print(f"\n{SUCESSO} Depósito de R$ {valor:.2f} realizado! {SUCESSO}")
    else:
        print(f"\n{ALERTA} Erro: O valor informado é inválido. {ALERTA}")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Realiza o saque validando regras de negócio via keywords."""
    falhou_saldo = valor > saldo
    falhou_limite = valor > limite
    falhou_saques = numero_saques >= limite_saques

    if falhou_saldo:
        print(f"\n{ALERTA} Erro: Saldo insuficiente. {ALERTA}")
    elif falhou_limite:
        print(f"\n{ALERTA} Erro: O valor excede o limite de R$ {limite:.2f}. {ALERTA}")
    elif falhou_saques:
        print(f"\n{ALERTA} Erro: Limite de {limite_saques} saques diários atingido. {ALERTA}")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t\tR$ {valor:>8.2f}\n"
        numero_saques += 1
        print(f"\n{SUCESSO} Saque realizado com sucesso! {SUCESSO}")
    else:
        print(f"\n{ALERTA} Erro: Valor informado é inválido. {ALERTA}")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    """Exibe o extrato formatado."""
    print(f"\n{BARRA}")
    print(f"{'EXTRATO BANCÁRIO':^45}")
    print(f"{BARRA}")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"{'-' * 45}")
    print(f"Saldo Atual:\t\tR$ {saldo:>8.2f}")
    print(f"{BARRA}\n")

def filtrar_usuario(cpf, usuarios):
    """Busca usuário por CPF usando Generator para eficiência."""
    return next((u for u in usuarios if u["cpf"] == cpf), None)

def criar_usuario(usuarios):
    """Cadastra um novo cliente com sanitização de entrada."""
    cpf = input("Informe o CPF (somente números): ").strip().replace(".", "").replace("-", "")
    
    if filtrar_usuario(cpf, usuarios):
        print(f"\n{ALERTA} Erro: Já existe um usuário com o CPF {cpf}! {ALERTA}")
        return

    nome = input("Nome completo: ").title()
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (Logradouro, Nro - Bairro - Cidade/UF): ")

    usuarios.append({
        "nome": nome, 
        "data_nascimento": data_nascimento, 
        "cpf": cpf, 
        "endereco": endereco
    })
    print(f"\n{SUCESSO} Usuário {nome} cadastrado com sucesso! {SUCESSO}")

def criar_conta(agencia, numero_conta, usuarios):
    """Vincula uma nova conta corrente a um usuário existente."""
    cpf = input("Informe o CPF do titular: ").strip().replace(".", "").replace("-", "")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f"\n{SUCESSO} Conta {numero_conta} aberta com sucesso! {SUCESSO}")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print(f"\n{ALERTA} Erro: Usuário não encontrado. Operação abortada! {ALERTA}")

def listar_contas(contas):
    """Exibe as contas cadastradas de forma tabular."""
    if not contas:
        print(f"\n{ALERTA} Nenhuma conta cadastrada no sistema. {ALERTA}")
        return
    
    print(f"\n{BARRA}")
    print(f"{'LISTAGEM DE CONTAS':^45}")
    print(f"{BARRA}")
    for conta in contas:
        print(f"AG: {conta['agencia']} | C/C: {conta['numero_conta']:04d} | Titular: {conta['usuario']['nome']}")
    print(f"{BARRA}\n")

def menu():
    menu_str = f"""
    {BARRA}
    { 'SISTEMA BANCÁRIO MAGALU' : ^45}
    {BARRA}
    [d]  Depositar      [nc] Nova Conta
    [s]  Sacar          [lc] Listar Contas
    [e]  Extrato        [nu] Novo Usuário
    [q]  Sair
    => """
    return input(textwrap.dedent(menu_str)).lower().strip()

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0.0
    limite = 500.0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        try:
            if opcao == "d":
                valor = float(input("Valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)

            elif opcao == "s":
                valor = float(input("Valor do saque: "))
                saldo, extrato, numero_saques = sacar(
                    saldo=saldo, valor=valor, extrato=extrato,
                    limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
                )

            elif opcao == "e":
                exibir_extrato(saldo, extrato=extrato)

            elif opcao == "nu":
                criar_usuario(usuarios)

            elif opcao == "nc":
                numero_conta = len(contas) + 1
                nova_conta = criar_conta(AGENCIA, numero_conta, usuarios)
                if nova_conta:
                    contas.append(nova_conta)

            elif opcao == "lc":
                listar_contas(contas)

            elif opcao == "q":
                print("\nEncerrando sistema... Até logo!")
                break
            
            else:
                print(f"\n{ALERTA} Opção inválida! {ALERTA}")
        
        except ValueError:
            print(f"\n{ALERTA} Erro crítico: Digite apenas números para valores. {ALERTA}")

if __name__ == "__main__":
    main()