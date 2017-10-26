#EP02
#Nomes:	Bruno da Silva Andrade
#		Lucas Augusto de Souza
#

matriz1='''010
111
000
101'''.split()

matriz2 = '''10101
10101
11111'''.split()

matriz3 = '''0011001010
0110001010
0011001110
0000000000
0010001010
0010011111
1111100000
0010001110
0010001110'''.split()

pixels = []
grupos = {}

def listar(matriz):
	global grupos, pixels
	pixels = []
	grupos = {}

	linha = 0
	for line in matriz:
		coluna = 0
		for p in line:
			if p == "1":
				pixels.append([linha,coluna])
			coluna += 1                
		linha += 1

def rotular():
	global grupos, pixels
	for px in pixels:
		if grupos == {}:
			grupos[1] = [px]
		else:
			possibilidades = []

			esquerda =  getRotulo([px[0],px[1]-1])
			cima = getRotulo([px[0]-1,px[1]])

			if esquerda!=-1:
				possibilidades.append(esquerda)
			if cima!=-1:
				possibilidades.append(cima)

			if possibilidades !=[]:
				rotulo = min(possibilidades)
				grupos[rotulo].append(px)
			else:
				rotulo = novoRotulo()
				grupos[rotulo]=[px]
			coEsquerda([px[0],px[1]])
			coCima([px[0],px[1]])

def getRotulo(pixFind):
	global grupos
	for rotulo in grupos:
		c=0
		while c<len(grupos[rotulo]):
			if grupos[rotulo][c]==pixFind:
				return rotulo
			c+=1
	return -1

def novoRotulo():
	global grupos
	
	grupoAux={}
	indice=1
	for rotulo in grupos:
		if grupos[rotulo]!=[]:
			grupoAux[indice]=grupos[rotulo]
			indice+=1

	grupos = grupoAux #Apaga rotulos vazios

	ult = 0
	for rotulo in grupos:
		ult = rotulo#Pega o ultimo rótulo
	return rotulo+1 

def printMatriz(matriz):
	global grupos
	nColunas = len(matriz[0])
	nLinhas = len(matriz)
	for l in range(nLinhas):
		for c in range(nColunas):
			rot = getRotulo([l,c])
			if rot == -1:
				print("0", end="")
			else:
				print(rot, end="")
		print("\n",end="")

def coEsquerda(pixel):
	global grupos

	linha=pixel[0]
	coluna=pixel[1]

	my = getRotulo([linha,coluna])

	rotuloEsq=getRotulo([linha,coluna-1])

	if rotuloEsq!=-1:
		if rotuloEsq != my:
			grupos[rotuloEsq].remove([linha,coluna-1])
			grupos[my].append([linha,coluna-1])
			coEsquerda([linha,coluna-1]) 

def coCima(pixel):
	global grupos

	linha=pixel[0]
	coluna=pixel[1]

	my = getRotulo([linha,coluna])

	rotuloCima=getRotulo([linha-1,coluna])

	if rotuloCima!=-1:
		if rotuloCima != my:
			grupos[rotuloCima].remove([linha-1,coluna])
			grupos[my].append([linha-1,coluna])
			coCima([linha-1,coluna])



listar(matriz1)
rotular()
printMatriz(matriz1)

print()
listar(matriz2)
rotular()
printMatriz(matriz2)

print()
listar(matriz3)
rotular()
printMatriz(matriz3)
