
variavel_a = 'olá mundo'

print(variavel_a)

variavel_b = input('digite algo ')

print(variavel_b)

a = type(variavel_a)
b = type(variavel_b)

print(a, b)

number1 = 5
number2 = 5.
number3 = number1+number2

print(number3)

number1 = number1 + number1 + 10

print(number1)

number1 += 3

print(number1)

number1 = 10**3

print(number1)

n_c = 5 + 1j

n_c2 = n_c+n_c

print(n_c2)

strNumber = '123'

numberfloat = float(strNumber)

print(numberfloat)

a = 'ola \n mundo \n'

print(a)

print(a + a)

print(a*5)

lista = [1,2,3,4]

print(lista)

lista += ['lapis'] # add palavras

print(lista)

lista += 'lapis' # add letra por letra

print(lista)

print(lista[0])

print(len(lista)) # retorna o tamanho da lista


lista_1 = ['p','y','t','h','o','n']
string_1 = 'python ' #string pode ter index igual a lista 

print(string_1[2:]) #do segundo elemento para frente 
print(lista_1[:2]) #até o segundo elemento

print(string_1*2) #aqui é concatenação da mesma sting, soma também funciona da mesma forma

a = True

print(type(a))

print(a)

a = 5 == 5

print(a)

a = 5 == 6

print(a)

#bool é usado como condição



#numeros podem ser comparados

y = int(input('escolha um número \n'))
if y > 0:
    print('positivo')
elif y < 0:
    print('negativo')
else:
    print('é 0')

#string pode ser comparadas
x = input('escolha uma palavra \n')

if x == 'string':
    print('são a mesma palavra')
else:
    print('não é a mesma palavra')


#pode comparara tipo 
#is pergunta se é algo

if x is not str:
    print('é número')

#operador and

if y > 4 and y < 10:
    print('o número foi aceito', y)

#operador or

if y < 4 or y > 10:
    print('o número foi aceito', y)



lista_1 = ['p','y','t','h','o','n']

lista_2 = [1,2,3,4,5]

#printa os elementos da lista

for i in lista_1:
    print(i)


for i in range(len(lista_1)):
    print(i)

#devolve o valor e o index correspondente

for i in enumerate(lista_1):
    print(i)
    print(i[0])
    print(i[1])



#while é enquanto

x = 10

while x >= 10:
    print(x)
    x += 1
    if x > 20:
        print('muito tempo de loop')
        break


lista_ex1 = [1,2,3,4,5,6,7,8,'a','b','c',0,-1,-2,-3,-4]

for i in lista_ex1:
    if type(i) == int:
        if i > 0:
            print('positivo \n')
        elif i < 0:
            print('negativo \n')
        elif i == 0:
            print('é zero \n')
    else:
        print('não é um número\n')



lista_1 = [1,2,3,4]
lista_2 = ['a','b','c','d']
lista_3 = []

for i in range(len(lista_1)):
    lista_3 += [lista_1[i]]
    lista_3 += [lista_2[i]]

for i in lista_3:
    print(i)



number = 4
result = 1

while number > 0:
    result *= number
    number -= 1

print(result)



lista_primos = []
number = 2

while len(lista_primos) < 50:
    i = 0
    j = 1
    while j <= number:
        if number % j == 0:
            i += 1
        j += 1
    if i == 2:
            lista_primos += [number]
    number += 1

for i in lista_primos:
    print(i)



lista = ['a','r','a','r','a']

lista_palavra = []

iteracao = 0

for i5 in range(len(lista)):
    L5 = lista[i5]
    lista_L5 = lista.copy() 
    lista_L4 = lista_L5.copy()
    lista_L4.pop(i5)
    for i4 in range(len(lista_L4)):
        L4 = lista_L4[i4]
        lista_L3 = lista_L4.copy()
        lista_L3.pop(i4)
        for i3 in range(len(lista_L3)):
            L3 = lista_L3[i3]
            lista_L2 = lista_L3.copy()
            lista_L2.pop(i3)
            for i2 in range(len(lista_L2)):
                L2 = lista_L2[i2]
                lista_L1 = lista_L2.copy()
                lista_L1.pop(i2)
                for i in range(len(lista_L1)):
                    L1 = lista_L1[i]
                    palavra = L5 + L4 + L3 + L2 + L1
                    
                    if palavra not in lista_palavra:
                        lista_palavra.append(palavra)

print(lista_palavra)
                    


lista1 = [1,2,3,4]
lista2 = [5,6,7,8]

lista1.extend(lista2) #junta as listas

print(lista1)

lista3 = lista2

lista3.append(lista2) #adiciona a lista no array como se fosse um elemento e não os elementos da lista

print(lista3) 

listaL = ['a','b','c','a']
print(listaL.count('a')) #função que conta o número de vezes q um elemento aparece

listaO = [1,3,2,6,4,5]
print(listaO)
listaO.sort() #ordena a lista, atenção pois ela modifica a lista e não retorna uma variavel com a lista ordenada
print(listaO)

listaL = ['t','f','z','b']
print(listaL)
listaL.sort()
print(listaL)




listaQ = []

for i in range(5):
    listaQ.append(i**2)

print(listaQ)

numeros = [1,2,3,4,5]
letras = ['a', 'b', 'c']
f = lambda x: x**2 if isinstance(x,(int, float)) else x * 2 #criamos uma função funciona com números e letras
for i in numeros:
    print(f(i))

for i in letras:
    print(f(i))

listaM = list(map(f, numeros))

print(listaM)

Q = [x**2 for x in range(6)]

print(Q)


vogais = ('a','e','i','o','u') #tupla é exatamente igual a lista só q n pode ser mudado, 1 vez definido não poder ser mudado

print(vogais)

numeros = [1,2,3,4,5]

for i in enumerate(numeros): #cria uma tupla
    print(i) 

setVar = {'a','e','i','o','u','a'}  #conjunto, não importa ordem e só se mostra uma vez mesmo q tenha n repetições dele no conjunto
print(setVar)

disc = {'data':10, 'data2':20} #informação com chave, ou seja, algo significa outra coisa 
print(disc['data'])
print(disc['data2'])


algRomano = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5}

print(algRomano)

algRomano.pop('V') #é capaz de modificar a tupla

print(algRomano)

list(algRomano.items())
print(list(algRomano.items())[3][0])

algRomano.keys()
list(algRomano.keys())
print(list(algRomano.keys()))

list(algRomano.values())
print(list(algRomano.values()))

print(algRomano.get('I'))


listaEX = ['P','A','Y','A','T','A','H','O','N']

i = 0
print(listaEX.count('A'))
while i < len(listaEX):
    if(listaEX[i] == 'A'):
        listaEX.pop(i)
    i += 1
    


print(listaEX)



listaImpares = [(i*2+1) for i in range(26)]

print(listaImpares)


valores = [1,2,3,4,5]
keys = ['a','b','c','d','e']

listaContida = {}

for i in range(5):
    listaContida[keys[i]] = valores[i]

print(listaContida)

listavalor = list(listaContida.values())

listaKeys = list(listaContida.keys())

print(listavalor)
print(listaKeys)

import matplotlib.pyplot as plt

x = [x for x in range((101))]
y = [y**2 for y in x]

plt.plot(x,y)




