    #calculo de juros topster com inflacao
    inicial = 1000
    juros = 0.5
    deposito = 50
    anos = 10
    inflacao = 0.2
    meses=12
    periodo=meses*anos
    fator=1+(juros/100)
    infla=1+(inflacao/100)
    res=inicial
    for i in range (periodo):
        res*=fator
        res/=infla
        res+=deposito
    print(res)
