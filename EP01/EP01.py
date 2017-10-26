#       EP01
#       Nomes: Bruno Andrade
#              Lucas Augusto de Souza
#       3° ADS/1


from random import *
from time import *

def merge(e,d):
	r=[]
	i, j = 0, 0
	while i < len(e) and j < len(d):
		if e[i] <= d[j]:
			r.append(e[i])
			i+=1
		else:
			r.append(d[j])
			j+=1
	r+= e[i:]
	r+= d[j:]
	return r

def mergesort(v):
	if len(v) <=1:
		return v
	else:
		m = len(v) // 2
		e = mergesort(v[:m])
		d = mergesort(v[m:])
		return merge(e,d)

def quicksort(lista):
    if len(lista) <=1:
        return lista
    else:
        pivô = lista[0]
        iguais = [x for x in lista if x == pivô]
        menores = [x for x in lista if x < pivô]
        maiores = [x for x in lista if x > pivô]
        return quicksort(menores)+ iguais + quicksort(maiores)

def selection(v):
    resp=[]
    while(len(v)>0):
        m= min(v)
        resp.append(m)
        v.remove(m)
    return resp

#cabeçalho
print("\t\tTempo em (s)")
print("-"*70)
print("\tNative   Mergesort   Quicksort   Selection")

nI = 2000
tempoInit = time()

while ((time() - tempoInit) < 30):
        lista = sample(range(0, nI), nI)

        #quicksort
        ini3 = time()
        quicksort(lista)
        fim3 = time()
        
        #native
        ini1 = time()
        lista.sort()
        fim1 = time()

        #mergesort
        ini2 = time()
        lista=mergesort(lista)
        fim2 = time()

        #selection
        ini4 = time()
        lista=selection(lista)
        fim4 = time()

        print(nI,"\t   %.2f\t   %.2f\t      %.2f\t     %.2f"%((fim1-ini1),(fim2-ini2),(fim3-ini3),(fim4-ini4)))
        nI+=2000

print("-"*70)
print("Processo finalizado, 30 segundos decorridos")
