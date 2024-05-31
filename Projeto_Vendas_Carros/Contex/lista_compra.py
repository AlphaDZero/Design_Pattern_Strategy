from Strategy.preco import Interface_Price
from ConcreteStrategy.desconto import valor_padrao
from Contex.dataset import base_dados
import pandas as pd

class Lista_Compra:

    def __init__(self):
        self.lista_cliente = pd.DataFrame()
    
    def set_pedido(self, lista: list):
        self.lista_cliente = base_dados.loc[lista, base_dados.columns].copy()
    
    def preco(self, strategy: Interface_Price = valor_padrao):
        preco = 0
        for valor in self.lista_cliente['preco']:
            preco += valor
        strategy.valor_final(preco)