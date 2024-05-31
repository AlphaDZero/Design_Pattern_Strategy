from Strategy.preco import Interface_Price

class valor_padrao(Interface_Price):

    def __init__(self):
        pass
    
    def valor_final(preco):
        print(f'Preço final valor padrão: R$ {preco}')


class black_friday(Interface_Price):

    def __init__(self):
        pass
    
    def valor_final(preco):
        preco = preco*0.85
        print(f'Preço final BlackFriday: R$ {preco}')


class casos_especificos(Interface_Price):

    def __init__(self):
        pass
    
    def valor_final(preco):
        preco = preco*0.8
        print(f'Preço final de casos especificos: R$ {preco}')