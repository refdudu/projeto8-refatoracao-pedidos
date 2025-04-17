# Projeto 8: Gerenciamento de Pedidos
pedidos = []

def novo():
    cliente = input("Cliente: ")
    valor = float(input("Valor: "))
    pedidos.append({"cliente": cliente, "valor": valor, "pago": False})

def listar():
    for p in pedidos:
        print(p["cliente"], "-", p["valor"], "-", "Pago" if p["pago"] else "Pendente")

def pagar():
    nome = input("Cliente para pagar: ")
    for p in pedidos:
        if p["cliente"] == nome and not p["pago"]:
            p["pago"] = True
            print("Pagamento feito")
            return

while True:
    print("1-Novo 2-Listar 3-Pagar 4-Sair")
    op = input("Opção: ")
    if op == "1":
        novo()
    elif op == "2":
        listar()
    elif op == "3":
        pagar()
    elif op == "4":
        break
