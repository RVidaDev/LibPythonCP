class test_ordenacao:
    def vetor_ordenado_crescente(vetor):
        for i in range(len(vetor) - 1):
            if vetor[i] > vetor[i + 1]:
                return False
            return True
        
        vetor_ordenado = [3, 7, 33, 59, 71]
        
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def nao_ordenado(vetor):
        for i in range(len(vetor) -1):
            if vetor[i] > vetor[i + 1]:
                return False
            return True
        
        vetor_nao_ordenado = [71, 7, 3, 9, 7]
        
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def ordenado_decrescente(vetor):
        for i in range(len(vetor) -1):
            if vetor[i] > vetor[i + 1]:
                return False
            return True
        
        vetor_ordenado_decrescente = [71, 59, 33, 7, 3]
        
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def vazio_vetor(vetor):
        for i in range(len(vetor) -1):
            if vetor[i] > vetor[i + 1]:
                return False
            return True
        vetor_vazio = []
        
    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def unico_elemento(vetor):
        for i in range(len(vetor) - 1):
            if vetor[i] > vetor[i + 1]:
                return False
            return True
        vetor_unico_elemento = [42]
        
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def elementos_repetidos(vetor):
        for i in range(len(vetor) - 1):
            if vetor[i] > vetor[i+ 1]:
                return False
            return True
        vetor_elementos_repetidos = [3, 7, 3, 9, 7]

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def elementos_negativos(vetor):
        for i in range(len(vetor - 1)):
            if vetor[i] > vetor[i  + 1]:
                return False
            return True
        vetor_elementos_negativos = [-5, -3, -9, -1]
        
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

            