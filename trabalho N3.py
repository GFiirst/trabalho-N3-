#criar as listas
A = ["a1","a2","a3","a4","a5","a6","a7"]
B = ["b1","b2","b3","b4","b5","b6","b7"]
C = ["c1","c2","c3","c4","c5","c6","c7"]
lista = []

#printar as listas para o usuário e pedir a escolha
for i in range(7):
    print(A[i]+' '+B[i]+' '+ C[i])

comando = input('Escolha um elemento e digite qual a coluna que ele esta: A, B ou C?')

#colocar a tabela escolhida entre as outras tabelas e juntar
if (comando == 'A'):
    lista = B + A + C

if (comando == 'B'):
    lista = A + B + C

if (comando == 'C'):
    lista = A + C + B

#separar a lista juntada em outras 3 listas novamente
A = [lista[0], lista[3], lista[6], lista[9], lista[12], lista[15], lista[18]]
B = [lista[1], lista[4], lista[7], lista[10], lista[13], lista[16], lista[19]]
C = [lista[2], lista[5], lista[8], lista[11], lista[14], lista[17], lista[20]]

#printar as listas
for i in range(7):
    print(A[i]+' '+B[i]+' '+ C[i])

comando = input('esta em qual coluna?')

if (comando == 'A'):
    lista = B + A + C

if (comando == 'B'):
    lista = A + B + C

if (comando == 'C'):
    lista = A + C + B


A = [lista[0], lista[3], lista[6], lista[9], lista[12], lista[15], lista[18]]
B = [lista[1], lista[4], lista[7], lista[10], lista[13], lista[16], lista[19]]
C = [lista[2], lista[5], lista[8], lista[11], lista[14], lista[17], lista[20]]

for i in range(7):
    print(A[i]+' '+B[i]+' '+ C[i])

comando = input('Digite a coluna:')

if (comando == 'A'):
    lista = B + A + C

if (comando == 'B'):
    lista = A + B + C

if (comando == 'C'):
    lista = A + C + B

#escolher o decimo primeiro elemento da lista
print(lista[10])