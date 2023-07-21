def menu():
    return """
    Bem Vindo ao Banco
    Escolha uma opção
    [1] Deposito
    [2] Saque
    [3] Extrato
    [4] Criar Usuário
    [5] Criar Conta
    [6] Listar Contas
    [0] Sair
    """

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo Insuficiente")
    elif valor > 500:
        print("Valor excede o limite")
    elif numero_saques[0] >= limite_saques:
        print("Limite de Saques diarios atingido")
    elif valor < 0:
        print("Valor invalido")
    else:
        saldo -= valor
        extrato += f"Saque no valor de R$ {valor:.2f}\n"
        numero_saques[0] += 1
        print("Saque realizado!")
    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito no valor de R$ {valor:.2f}\n"
        print("Deposito realizado!")
    else:
        print("Valor Invalido")
    return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")

def busca_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

def criar_usuario(usuarios):
    cpf = input("Digite seu cpf: ")
    usuario = busca_usuario(cpf, usuarios)

    if usuario:
        print("Usuario ja existente")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = busca_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado!\n")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = [0]
    usuarios = []
    contas = []

    opcoes = {
        "1": lambda: depositar(
            saldo,
            float(input("Informe o valor do depósito: ")),
            extrato,
        ),
        "2": lambda: sacar(
            saldo=saldo,
            valor=float(input("Informe o valor do saque: ")),
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        ),
        "3": lambda: exibir_extrato(saldo, extrato),
        "4": lambda: criar_usuario(usuarios),
        "5": lambda: criar_conta(
            AGENCIA,
            len(contas) + 1,
            usuarios,
        ),
        "6": lambda: listar_contas(contas),
        "0": lambda: exit(),
    }

    while True:
        print(menu())
        opcao = input("Escolha uma opção: ")

        if opcao in opcoes:
            opcoes[opcao]()
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
