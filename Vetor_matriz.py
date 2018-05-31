import math # Para usar sqrt no modulo do vetor

# Indice para consulta dos principais conceitos.

#Funcoes essenciais para se trabalhar com vetores lista - l.124
# Map Filter and reduce - l.54
# Zip - l.16
# Matrizes - l.146

#Vetores como lista
def vector_add(v,w):
	return [v_i + w_i for v_i,w_i in zip(v,w)] 	# Serve para atribuir o resultado da soma
	#de v com w.

def vector_mult(v,a):
	return [v_i*a for v_i in v] # Serve para atribuir o resultado da multiplicao de v 
#por um real a

# zip junta elementos correspondentes de listas em tuplas, exemplo:
# Se tivermos l1 = ["Victor","Eduardo"] e l2 = ["Carol","Camila"]
# zip(l1,l2) = [("Victor","Carol"),("Eduardo","Camila")]
# Portanto zip(l1,l2,l3..) cria uma lista de tuplas dessa forma.

#Note que se quisermos subtrair um vetor, digamos v - w, basta :
v = [3,3,3]
w = [2,2,2]

u = vector_add(v,vector_mult(w,-1)) # u = [1,1,1]
# Tambem podemos fazer uma funcao vector_subtract para dar mais clareza ao codigo.

def vector_subtract(v,w):
	return vector_add(v,vector_mult(w,-1))

u = vector_subtract(v,w) # u = [1,1,1]

# Com frequencia queremos obter uma lista de vetores e soma-los todos:

def vector_sum(vectors):# Passamos uma lista de listas(vetores)
	s = vector_add(vectors[0],vectors[1]) # Inicializamos s como sendo a soma do primeiro
# 	com o segundo vetor
	for i in range(len(vectors)-2): # O loop ira rodar menos 2 vezes pois ja somamos 2 vetores
		s = vector_add(s,vectors[i+2]) # aqui somamos s que ja somou [0] e [1] com [2]
	return s

d = vector_sum([[1,2,1],[2,3,1],[4,5,1]]) # [7,10,3] como deveria ser.

# Porem ha formas mais Pythonic de fazer isso

def vector_sum_1(vectors):
	result = vector[0]  # inicializamos a soma como o primeiro vetor
	for vector in vectors[1:]: # para todos os vetores restantes.
		result = vector_add(result,vector) # somamos um por vez.
	return result

def vector_sum_2(vectors):
	return reduce(vector_add,vectors) # O que eh reduce? 

# Map, Filter E Reduce !
# Map cria uma lista a partir de outra com os elementos afetados por uma funcao
#Ex:
def dobra(a):
 	return a*2 #Uma funcao que retorna o dobro do input

lista = [1,2,3,4] # Uma lista inocente

lista_2 = map(dobra,lista)  # lista_2 = [2,4,6,8]
# Ou seja, map eh uma funcao que recebe uma funcao e uma lista e retorna uma lista
# com os elementos modificados pela funcao !

# Tambem podemos combar o uso de map com as funcoes lambda

lista_3 = map(lambda x: 2*x,lista) # Uma forma muito mais interessante ! de dobrar os 
# elementos de uma lista.

#Filter cria uma lista com elementos de uma dada lista para os quais uma certa condicao eh verdadeira

lista = [1,2,3,4,5,6,7,8,9,10]

# E se quisessemos criar uma lista contendo apenas os elementos que sao divisiveis por 2?

lista_2 = filter(lambda x: x%2 ==0,lista) # Vai calcular x%2 para todos os elementos de lista
# aqueles cujo o resulto for 0 sao dignos de pertencer a lista_2
# portanto lista_2 = [2,4,6,8,10]

# Outro exemplo:

lista = ["Victor","Eduardo","Lula","Bolsonaro"]
lista_2 = filter(lambda palavra:palavra[0]=="V",lista) # vai verificar palavra[0] para
# todas as palavras na lista, aquelas que comecarem com V sao dignas de compor a lista_2
# Seria uma forma interessante de obter todas as palavras que comecam com determinada letra
# em um livro

#Reduce - Realiza uma computacao sequencial par a par sobre elementos de uma lista
#Exemplo 1:

lista = [1,2,3,4]
# Imagine que queremos multiplicar um elemento pelo outro e apresentar essa multiplicacao
# Como fariamos isso? Multiplicando o 1 pelo 2, guardando o resultado, multiplicando o resultado por 3
# guardando o resultado e entao multiplicando o mesmo por 4, eh isso que quis dizer por
# computacao sequencial par a par, sempre teremos um par que contem a informacao anterior e faremos
# ele interagir com o elemento seguinte da lista.

lista_2 = reduce(lambda acumulado,proximo: acumulado*proximo , lista) #Reduziu a lista par 24

# Exemplo 2:
lista = [1,2,3,4]

lista_2 = reduce(lambda acumulado,proximo: acumulado + proximo, lista) #Reduziu a lista para 10

# Pelo que entendo reduce pode ter como argumento qualquer funcao que pegue duas coisas e as torne uma
# por isso fizemos reduce(vector_add, vectors)
# portanto a melhor forma de pensar na reduce eh reduce(funcaoquepegaduascoisasetornauma,listaaserreduzidasequencialmente)

# Vamos agora fazer o Produto escalar de dois vetores:

def dotprod(v,w):
	u = [v1*v2 for v1,v2 in v,w] # Cria uma lista obtida pela multiplicacao componente a componente
	return reduce(lambda a,b:a+b,u) # reduz a lista somando os elementos

# e agora vamos fazer uma funcao que calcula o modulo de um vetor

def sum_quad(v):
	return reduce(lambda a,b:(a**2)+(b**2),v)

def modulo(v):
	return math.sqrt(sum_quad(v))


#Portanto as funcoes essenciais para se trabalhar com vetores lista sao:

def vector_add(v,w):
	return [v_i + w_i for v_i,w_i in zip(v,w)] 

def vector_mult(v,a):
	return [v_i*a for v_i in v]

def vector_subtract(v,w):                         
	return vector_add(v,vector_mult(w,-1))

def dotprod(v,w):
	u = [v1*v2 for v1,v2 in v,w] 
	return reduce(lambda a,b:a+b,u)

def mod(v):
	return math.sqrt(dotprod(v,v))        

# Representacao de matrizes no Python, nada alem de Lista de listas.
# Ex 1. Matriz 2x3

A = [[1,2,3],
	[4,5,6]]
#Ex 2. Matriz 2x2
B = [[1,2],
	 [3,4]]
# Note que o comprimento das listas individuais define o numero de colunas e o numero
# de listas individuais define o numero de linhas da matriz

# Para A

num_linhas = len(A)
num_colunas = len(A[0])

# Podemos assim fazer uma funcao que retorna a ordem da matriz, retornando uma tupla(#linhas,#colunas)

def shape(A):
	num_linhas = len(A)
	num_colunas = len(A[0])
	return (num_linhas,num_colunas)

# Podemos fazer uma funcao que retorna a i-esima linha

def getrow(A,i):
	return A[i]

# E uma que retorna a j-esima coluna

def getcol(A,j):
	return [A[i][j] for i in range(len(A))]

