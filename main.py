import time
import random
import matplotlib.pyplot as plt

class Busca:
    @staticmethod
    def busca_sequencial(lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    
    @staticmethod
    def busca_binaria(lista, alvo):
        inicio = 0
        fim = len(lista) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2
            if lista[meio] == alvo:
                return meio
            elif lista[meio] < alvo:
                inicio = meio + 1
            else:
                fim = meio - 1
        return -1

def medir_tempo_execucao(algoritmo, lista, elemento=None):
    inicio = time.time()
    if elemento is None:
        algoritmo(lista)
    else:
        algoritmo(lista, elemento)
    fim = time.time()
    return fim - inicio

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    
    return merge(esquerda, direita)

tamanhos_lista = [100, 1000, 10000]

resultados_busca_sequencial = []
resultados_busca_binaria = []

resultados_ordenacao = {
    "Ordenação Bubble Sort": [],
    "Ordenação Insertion": [],
    "Ordenação Merge": [],
}

for tamanho in tamanhos_lista:
    lista = sorted([random.randint(1, 1000) for _ in range(tamanho)])
    elemento = random.randint(1, 1000)
    
    tempo_execucao = medir_tempo_execucao(Busca.busca_sequencial, lista, elemento)
    resultados_busca_sequencial.append(tempo_execucao * 10)  # Multiplicando por 10 para tornar mais visível
    
    tempo_execucao = medir_tempo_execucao(Busca.busca_binaria, lista, elemento)
    resultados_busca_binaria.append(tempo_execucao)

plt.plot(tamanhos_lista, resultados_busca_sequencial, label="Busca Sequencial")
plt.plot(tamanhos_lista, resultados_busca_binaria, label="Busca Binária")
plt.xlabel("Tamanho da Lista de Teste")
plt.ylabel("Tempo de Execução (segundos)")
plt.title("Desempenho dos Algoritmos de Busca em Função do Tamanho da Lista de Teste")
plt.legend()
plt.savefig("relatorio_grafico_busca.png")
plt.show()

for tamanho in tamanhos_lista:
    lista = [random.randint(1, 1000) for _ in range(tamanho)]
    
    tempo_execucao = medir_tempo_execucao(bubble_sort, lista.copy())
    resultados_ordenacao["Ordenação Bubble Sort"].append(tempo_execucao)
    
    tempo_execucao = medir_tempo_execucao(insertion_sort, lista.copy())
    resultados_ordenacao["Ordenação Insertion"].append(tempo_execucao)
    
    tempo_execucao = medir_tempo_execucao(merge_sort, lista.copy())
    resultados_ordenacao["Ordenação Merge"].append(tempo_execucao)

plt.plot(tamanhos_lista, resultados_ordenacao["Ordenação Bubble Sort"], label="Bubble Sort")
plt.plot(tamanhos_lista, resultados_ordenacao["Ordenação Insertion"], label="Insertion Sort")
plt.plot(tamanhos_lista, resultados_ordenacao["Ordenação Merge"], label="Merge Sort")
plt.xlabel("Tamanho da Lista de Teste")
plt.ylabel("Tempo de Execução (segundos)")
plt.title("Desempenho dos Algoritmos de Ordenação em Função do Tamanho da Lista de Teste")
plt.legend()
plt.savefig("relatorio_grafico_ordenacao.png")
plt.show()
