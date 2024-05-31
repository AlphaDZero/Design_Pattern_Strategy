from Contex.lista_compra import Lista_Compra
from ConcreteStrategy.desconto import black_friday, casos_especificos, valor_padrao

cliente = Lista_Compra()
cliente.set_pedido([0,4,6,6])

cliente.preco()
cliente.preco(casos_especificos)
cliente.preco(black_friday)
cliente.preco(valor_padrao)