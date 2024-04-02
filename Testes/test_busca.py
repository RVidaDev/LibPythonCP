class TestBusca:
    @staticmethod
    def busca_elemento(vetor, elemento):
        print("Buscando elemento {} no vetor {}".format(elemento, vetor))
        for item in vetor:
            if item == elemento:
                print("Elemento encontrado!")
                return True
        print("Elemento não encontrado.")
        return False

    @staticmethod
    def busca_elemento_nulo(vetor, elemento):
        print("Buscando elemento {} no vetor {}".format(elemento, vetor))
        for item in vetor:
            if item == elemento:
                print("Elemento encontrado!")
                return True
        print("Elemento não encontrado.")
        return False

    @staticmethod
    def busca_elemento_vazio(vetor, elemento):
        print("Buscando elemento {} no vetor {}".format(elemento, vetor))
        for item in vetor:
            if item == elemento:
                print("Elemento encontrado!")
                return True
        print("Elemento não encontrado.")
        return False

    @staticmethod
    def busca_elemento_unico(vetor, elemento):
        print("Buscando elemento {} no vetor {}".format(elemento, vetor))
        for item in vetor:
            if item == elemento:
                print("Elemento encontrado!")
                return True
        print("Elemento não encontrado.")
        return False


# Testando o código
vetor = [3, 7, 33, 59, 71]
elemento_de_busca = 33
print("Resultado da busca:", TestBusca.busca_elemento(vetor, elemento_de_busca))  

elemento_de_busca = [10]
print("Resultado da busca:", TestBusca.busca_elemento_nulo(vetor, elemento_de_busca))  

vetor_vazio = []
elemento_busca = 10
print("Resultado da busca:", TestBusca.busca_elemento_vazio(vetor_vazio, elemento_busca)) 

vetor_unico = [3, 9, 200, 42, 29, 44]
elemento_busca = 42
print("Resultado da busca:", TestBusca.busca_elemento_unico(vetor_unico, elemento_busca))  
