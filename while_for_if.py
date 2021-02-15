#calculo de juros topster com while
print ("entre com o valor inicial")
inicial = int(input())
print ("entre com o juros")
juros = float(input())
deposito = 50
anos = 10
inflacao = 0.2
meses=12
periodo=meses*anos
objetivo=10000
fator=1+(juros/100)
infla=1+(inflacao/100)
res=inicial
for i in range (periodo):
    res*=fator
    res/=infla
    res+=deposito
if res < objetivo:
    print ("Objetivo atingido")
if res>= objetivo:
    print ("Objetivo não atingido")


