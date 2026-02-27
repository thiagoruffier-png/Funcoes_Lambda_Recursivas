# Função para calcular o reajuste de um produto em 30%
#Função convencional
def calcular_reajuste(valor):
    return valor * 1.3

print(f'Preço: {calcular_reajuste(1000)}')
#Função lambda
reajuste = lambda x: x * 1.3
print(reajuste(1000))


produtos = [1000, 200, 350, 520, 110]
print(list(map(calcular_reajuste, produtos)))
print(list(map(lambda x : x * 1.3, produtos)))
print(list(map(reajuste, produtos)))

#Converte uma string em maiuscula
nome_lambda = lambda nome : nome.upper()
print(nome_lambda('juca'))

lista = ['ana', 'maria', 'carlos', 'pedro']

print(list(map(lambda nome : nome.upper(), lista)))


#retornar gerar uma lista apenas com valores pares
numeros = [1,2,3,4,5,6,7,8,10]

print(list(filter(lambda x : x % 2 == 0, numeros)))