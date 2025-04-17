# Projeto 8: Gerenciamento de Pedidos

class GerenciadorPedidos:
    def __init__(self):
        self.pedidos = []
    
    def cadastrar_pedido(self):
        nome_cliente = self.obter_nome_cliente()
        valor_pedido = self.obter_valor_pedido()
        self.adicionar_pedido(nome_cliente, valor_pedido)
    
    def obter_nome_cliente(self):
        return input("Cliente: ")
    
    def obter_valor_pedido(self):
        return float(input("Valor: "))
    
    def adicionar_pedido(self, nome_cliente, valor_pedido):
        self.pedidos.append({"cliente": nome_cliente, "valor": valor_pedido, "pago": False})
    
    def listar_pedidos(self):
        for pedido in self.pedidos:
            self.exibir_informacoes_pedido(pedido)
    
    def exibir_informacoes_pedido(self, pedido):
        status_pagamento = self.obter_status_pagamento(pedido)
        print(pedido["cliente"], "-", pedido["valor"], "-", status_pagamento)
    
    def obter_status_pagamento(self, pedido):
        return "Pago" if pedido["pago"] else "Pendente"
    
    def registrar_pagamento(self):
        nome_cliente = self.obter_nome_cliente_para_pagamento()
        self.processar_pagamento(nome_cliente)
    
    def obter_nome_cliente_para_pagamento(self):
        return input("Cliente para pagar: ")
    
    def processar_pagamento(self, nome_cliente):
        for pedido in self.pedidos:
            if self.eh_pedido_pendente(pedido, nome_cliente):
                self.marcar_como_pago(pedido)
                self.notificar_pagamento_realizado()
                return
    
    def eh_pedido_pendente(self, pedido, nome_cliente):
        return pedido["cliente"] == nome_cliente and not pedido["pago"]
    
    def marcar_como_pago(self, pedido):
        pedido["pago"] = True
    
    def notificar_pagamento_realizado(self):
        print("Pagamento feito")


class InterfaceUsuario:
    def __init__(self):
        self.gerenciador = GerenciadorPedidos()
    
    def exibir_menu(self):
        print("1-Novo 2-Listar 3-Pagar 4-Sair")
    
    def executar_programa(self):
        while True:
            self.exibir_menu()
            opcao = self.obter_opcao_usuario()
            if self.processar_opcao(opcao):
                break
    
    def obter_opcao_usuario(self):
        return input("Opção: ")
    
    def processar_opcao(self, opcao):
        if opcao == "1":
            self.gerenciador.cadastrar_pedido()
        elif opcao == "2":
            self.gerenciador.listar_pedidos()
        elif opcao == "3":
            self.gerenciador.registrar_pagamento()
        elif opcao == "4":
            return True
        return False


# Iniciar o programa
if __name__ == "__main__":
    interface = InterfaceUsuario()
    interface.executar_programa()