# EP03
# Nomes: Bruno da Silva Andrade
#		 Lucas Augusto de Souza
# 3° ADS/A

def enumerações(items):
    n = len(items)
    s = [0]*(n+1)
    k = 0
    while True:
        if s[k] < n:
            s[k+1] = s[k] + 1
            k += 1
        else:
            s[k-1] += 1
            k -= 1
        if k == 0:
            break
        else:
            lista = []
            for j in range(1, k+1):
                lista.append(items[s[j]-1])
            yield lista

def combinações(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in combinações(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def permutações(items):
    return combinações(items, len(items))

casamento={}
cavaleiros={}

def prencherDic(file):
    saida = {}
    for linha in file:
        linha=linha.replace("\n","")
        lista = linha.split(" ")
        saida[lista[0]]=lista[1:]
    return saida
    
f1 = open("casamento.txt")
f2 = open("cavaleiros.txt")

casamento = prencherDic(f1)
cavaleiros = prencherDic(f2)

f1.close()
f2.close()

def testaCasamento(p):
	queridos = set()
	for dama in p:
		for cara in casamento[dama]:
			queridos.add(cara)

	if len(queridos)>=len(p):
		return True
	else:
		return False

def testaAmizade(p):
	cont=0
	while cont<len(p):
		atual = p[cont]
		esquerda = p[cont-1]

		if  not ((esquerda in cavaleiros[atual]) or (atual in cavaleiros[esquerda])):
			return False

		cont+=1
	return True

saida = "Casamento possível"
for p in enumerações(['Jessica', 'Fernanda', 'Pamela', 'Renata']):
	if not testaCasamento(p):
		saida = "Preferências de "
		for a in p:
			saida += a+"-"
		saida = saida[:-1]
		saida += " insuficientes"
		break

print(saida, end="")


mesaFechada = False
for p in permutações(['Adriano','Bruno', 'Diogo', 'Eclis', 'Gabriel', 'Leandro', 'Walber']):
	if testaAmizade(p):
		print (" e mesa possivel: ", end="")
		print(p[0]+"-"+p[1]+"-"+p[2]+"-"+p[3]+"-"+p[4]+"-"+p[5]+"-"+p[6]+"-"+p[0])
		mesaFechada=True
		break

if not mesaFechada:
	print(" e não é possível arrumar a mesa")
