# Projeto 8: Gerenciamento de Pedidos
lista_pedidos = []

def cadastrar_pedido():
    nome_cliente = obter_nome_cliente()
    valor_pedido = obter_valor_pedido()
    adicionar_pedido(nome_cliente, valor_pedido)

def obter_nome_cliente():
    return input("Cliente: ")

def obter_valor_pedido():
    return float(input("Valor: "))

def adicionar_pedido(nome_cliente, valor_pedido):
    lista_pedidos.append({"cliente": nome_cliente, "valor": valor_pedido, "pago": False})

def listar_pedidos():
    for pedido in lista_pedidos:
        exibir_informacoes_pedido(pedido)

def exibir_informacoes_pedido(pedido):
    status_pagamento = obter_status_pagamento(pedido)
    print(pedido["cliente"], "-", pedido["valor"], "-", status_pagamento)

def obter_status_pagamento(pedido):
    return "Pago" if pedido["pago"] else "Pendente"

def registrar_pagamento():
    nome_cliente = obter_nome_cliente_para_pagamento()
    processar_pagamento(nome_cliente)

def obter_nome_cliente_para_pagamento():
    return input("Cliente para pagar: ")

def processar_pagamento(nome_cliente):
    for pedido in lista_pedidos:
        if eh_pedido_pendente(pedido, nome_cliente):
            marcar_como_pago(pedido)
            notificar_pagamento_realizado()
            return

def eh_pedido_pendente(pedido, nome_cliente):
    return pedido["cliente"] == nome_cliente and not pedido["pago"]

def marcar_como_pago(pedido):
    pedido["pago"] = True

def notificar_pagamento_realizado():
    print("Pagamento feito")

def exibir_menu():
    print("1-Novo 2-Listar 3-Pagar 4-Sair")

def executar_programa():
    while True:
        exibir_menu()
        opcao = obter_opcao_usuario()
        if processar_opcao(opcao):
            break

def obter_opcao_usuario():
    return input("Opção: ")

def processar_opcao(opcao):
    if opcao == "1":
        cadastrar_pedido()
    elif opcao == "2":
        listar_pedidos()
    elif opcao == "3":
        registrar_pagamento()
    elif opcao == "4":
        return True
    return False

executar_programa()
