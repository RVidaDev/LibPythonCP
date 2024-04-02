# Imports realizados 
import time
import random
import matplotlib.pyplot as plt

# Realização das listas

# Lista com 100 elementos
lista_100 = random.sample(range(10000), 100)

# Lista com 1000 elementos
lista_1000 = random.sample(range(10000), 1000)

# Lista com 10000 elementos
lista_10000 = random.sample(range(10000), 10000)

# Medindo o tempo executável:
def medir_tempo_execucao(algoritmo, lista):
    inicio = time.time()
    algoritmo(lista)      
    fim = time.time()     
    return fim - inicio  

# Resultados:

resultados = {
    "Busca Sequencial": [],
    "Busca Binária": [],
    "Ordenação Bubble Sort": [],
    "Ordenação Insertion": [],
    "Ordenação Merge": [],
}

# ///////////////////////////
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Definindo tamanhos das listas de teste
tamanhos_lista = [100, 1000, 10000]

# Executar testes para cada tamanho de lista
resultados = {"Ordenação Bubble Sort": []}
for tamanho in tamanhos_lista:
    lista = [random.randint(1, 1000) for _ in range(tamanho)]
    tempo_execucao = medir_tempo_execucao(bubble_sort, lista)
    resultados["Ordenação Bubble Sort"].append(tempo_execucao)

# Plotando gráficos
plt.plot(tamanhos_lista, resultados["Ordenação Bubble Sort"], label="Ordenação Bubble Sort")
plt.xlabel("Tamanho da Lista de Teste")
plt.ylabel("Tempo de Execução (segundos)")
plt.title("Desempenho da Ordenação Bolha em Função do Tamanho da Lista de Teste")
plt.legend()
plt.savefig("relatorio_grafico.png")  # Salvar o gráfico como uma imagem
plt.show()


