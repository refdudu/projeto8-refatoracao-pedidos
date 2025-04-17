# Projeto 8: Gerenciamento de Pedidos
lista_pedidos = []

def cadastrar_pedido():
    nome_cliente = input("Cliente: ")
    valor_pedido = float(input("Valor: "))
    lista_pedidos.append({"cliente": nome_cliente, "valor": valor_pedido, "pago": False})

def listar_pedidos():
    for pedido in lista_pedidos:
        print(pedido["cliente"], "-", pedido["valor"], "-", "Pago" if pedido["pago"] else "Pendente")

def registrar_pagamento():
    nome_cliente = input("Cliente para pagar: ")
    for pedido in lista_pedidos:
        if pedido["cliente"] == nome_cliente and not pedido["pago"]:
            pedido["pago"] = True
            print("Pagamento feito")
            return

while True:
    print("1-Novo 2-Listar 3-Pagar 4-Sair")
    opcao = input("Opção: ")
    if opcao == "1":
        cadastrar_pedido()
    elif opcao == "2":
        listar_pedidos()
    elif opcao == "3":
        registrar_pagamento()
    elif opcao == "4":
        break
