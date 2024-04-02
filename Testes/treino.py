def vetor_ordenado_crescente(vetor):
    return all(vetor[x] <= vetor[x + 1] for x in range(len(vetor) - 1))

def nao_ordenado(vetor):
    return not any(vetor[x] > vetor[x + 1] for x in range(len(vetor) - 1))

def ordenado_decrescente(vetor):
    return all(vetor[x] >= vetor[x + 1] for x in range(len(vetor) - 1))

def vazio_vetor(vetor):
    return not vetor

def unico_elemento(vetor):
    return len(vetor) == 1

def elementos_repetidos(vetor):
    return len(vetor) == len(set(vetor))

def elementos_negativos(vetor):
    return all(vetor[x] >= vetor[x + 1] for x in range(len(vetor) - 1))

def main():
    vetor_ordenado = [3, 7, 33, 59, 71]
    vetor_nao_ordenado = [71, 7, 3, 9, 7]
    vetor_ordenado_decrescente = [71, 59, 33, 7, 3]
    vetor_vazio = []
    vetor_unico_elemento = [42]
    vetor_elementos_repetidos = [3, 7, 3, 9, 7]
    vetor_elementos_negativos = [-5, -3, -9, -1]

    print("Vetor ordenado crescente:", vetor_ordenado_crescente(vetor_ordenado))
    print("Não ordenado:", nao_ordenado(vetor_nao_ordenado))
    print("Ordenado decrescente:", ordenado_decrescente(vetor_ordenado_decrescente))
    print("Vazio:", vazio_vetor(vetor_vazio))
    print("Único elemento:", unico_elemento(vetor_unico_elemento))
    print("Elementos repetidos:", elementos_repetidos(vetor_elementos_repetidos))
    print("Elementos negativos:", elementos_negativos(vetor_elementos_negativos))

if __name__ == "__main__":
    main()
