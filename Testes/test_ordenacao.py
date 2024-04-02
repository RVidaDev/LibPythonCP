class TestOrdenacao:
    @staticmethod
    def vetor_ordenado_crescente(vetor):
        print("Verificando se o vetor está ordenado de forma crescente:", vetor)
        for i in range(len(vetor) - 1):
            if vetor[i] > vetor[i + 1]:
                return False
        return True

    @staticmethod
    def nao_ordenado(vetor):
        print("Verificando se o vetor está ordenado:", vetor)
        for i in range(len(vetor) - 1):
            if vetor[i] > vetor[i + 1]:
                return False
        return True

    @staticmethod
    def ordenado_decrescente(vetor):
        print("Verificando se o vetor está ordenado de forma decrescente:", vetor)
        for i in range(len(vetor) - 1):
            if vetor[i] < vetor[i + 1]:
                return False
        return True

    @staticmethod
    def vazio_vetor(vetor):
        print("Verificando se o vetor está vazio:", vetor)
        if len(vetor) == 0:
            return True
        return False

    @staticmethod
    def unico_elemento(vetor):
        print("Verificando se o vetor possui apenas um elemento:", vetor)
        if len(vetor) == 1:
            return True
        return False

    @staticmethod
    def elementos_repetidos(vetor):
        print("Verificando se há elementos repetidos no vetor:", vetor)
        for i in range(len(vetor) - 1):
            if vetor[i] == vetor[i + 1]:
                return True
        return False

    @staticmethod
    def elementos_negativos(vetor):
        print("Verificando se há elementos negativos no vetor:", vetor)
        for num in vetor:
            if num < 0:
                return True
        return False


# Testando o código
vetor_ordenado = [3, 7, 33, 59, 71]
print("Vetor ordenado crescente:", TestOrdenacao.vetor_ordenado_crescente(vetor_ordenado))  

vetor_nao_ordenado = [71, 7, 3, 9, 7]
print("Vetor não ordenado:", TestOrdenacao.nao_ordenado(vetor_nao_ordenado))  

vetor_ordenado_decrescente = [71, 59, 33, 7, 3]
print("Vetor ordenado decrescente:", TestOrdenacao.ordenado_decrescente(vetor_ordenado_decrescente)) 

vetor_vazio = []
print("Vetor vazio:", TestOrdenacao.vazio_vetor(vetor_vazio))  

vetor_unico_elemento = [42]
print("Vetor com único elemento:", TestOrdenacao.unico_elemento(vetor_unico_elemento))  

vetor_elementos_repetidos = [3, 7, 3, 9, 7]
print("Vetor com elementos repetidos:", TestOrdenacao.elementos_repetidos(vetor_elementos_repetidos))  

vetor_elementos_negativos = [-5, -3, -9, -1]
print("Vetor com elementos negativos:", TestOrdenacao.elementos_negativos(vetor_elementos_negativos))  