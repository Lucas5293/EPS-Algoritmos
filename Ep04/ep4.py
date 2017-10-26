#3º ADS A - Estrutura de Dados
#Lucas Augusto de Souza
#Bruno da Silva Andrade 


#Entrada do Grafo
G = {
1:[6,7],
2:[3,7],
3:[4,7],
4:[3,7],
5:[7],
6:[3,1],
7:[1,2,3,4,5]}



#Vertice com menor numero de ligações 
def getMenor():
	tam = {}
	
	for key in G:
		t = len(G[key])
		if t not in tam:
			tam[t] = key

	
	return tam[min(tam)]


#Destroi a vertice e suas ligações
def destroy(vertice):
	global G
	aux = {}
	
	remover = G[vertice] 

	for key in G:
		if key!=vertice and vertice not in G[key]:
			aux[key] = G[key]
			for remove in remover:
				if remove in aux[key]:
					posApagar = aux[key].index(remove)
					del aux[key][posApagar]

	G = aux


#Vertices destruidas
S=[]
print(G)
#Loop para esvaziar o grafo
while G!={}:
	a=getMenor()

	print(a, end=": ")


	S.append(a)
	destroy(a)
	
	print(G)

S.sort()
print(S)