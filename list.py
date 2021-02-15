#lista
produtos = []
precos = []
quantidades = []

total = 0
while True:
    print('Digite um produto:')
    produto = input()
    print('Digite um preco:')
    preco = float(input())
    print('Digite um preco:')
    quantidade = int(input())  
    if produto == '':
        break

    produtos.append(produto)
    precos.append(preco)
    quantidades.append(quantidade)

    total += quantidade * preco
