import pandas as pd
tabela = {
    'marca' :['BMW','Dodge','Mercedes-Benz','BMW','Porshe','Ford','Chevrolet','Chevrolet'],
    'modelo':['M3 E46 GTR','Challenger SRT','Gla 200','X1','911','Mustang','Ônix Lt 1.0 Mt','Ônix 1.0 Turbo'],
    'preco' :[5000000,1125000,119950,299900,875000,529000,93765,100730]
}

base_dados = pd.DataFrame(tabela)