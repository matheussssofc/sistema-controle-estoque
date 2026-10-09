produtos = []


def cadastrar_produto():
    codigo = input("Digite o codigo do produto: ")

    for produto in produtos:
        if produto["codigo"] == codigo:
            print("Esse codigo ja esta cadastrado.")
            return

    nome = input("Digite o nome do produto: ")

    preco = float(input("Digite o preco do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))

    if preco < 0 or quantidade < 0:
        print("O preco e a quantidade nao podem ser negativos.")
        return

    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

    print("Produto cadastrado com sucesso!")


def listar_produtos():
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    print("\n--- PRODUTOS CADASTRADOS ---")

    for produto in produtos:
        print(f"""
Codigo: {produto["codigo"]}
Nome: {produto["nome"]}
Preco: R$ {produto["preco"]:.2f}
Quantidade: {produto["quantidade"]}
-----------------------------
""")


def calcular_total():
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    total = 0

    for produto in produtos:
        valor = produto["preco"] * produto["quantidade"]
        total += valor

    print(f"Valor total do estoque: R$ {total:.2f}")


def menu():
    while True:
        print("""
===== CONTROLE DE ESTOQUE =====

1 - Cadastrar produto
2 - Listar produtos
3 - Calcular valor total do estoque
4 - Sair
""")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            calcular_total()

        elif opcao == "4":
            print("Sistema encerrado.")
            break

        else:
            print("Opcao invalida.")


menu()