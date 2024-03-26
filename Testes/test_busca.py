class test_busca:
    def busca_elemento(vetor, elemento):
        for item in vetor:
            if item == elemento:
                return True
            return False
        
        vetor = [3, 7, 33, 59, 71]
        
        elemento_de_busca = 33
        
        resultado = busca_elemento(vetor, elemento_de_busca)
        
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def busca_elemento_nulo(vetor, elemento):
        for item in vetor:
            if item == elemento:
                return True
            return False
        
        vetor = [3, 7, 33, 59, 71]
        
        elemento_de_busca = [10]
        
        resultado = busca_elemento_nulo(vetor, elemento_de_busca)
        
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def busca_elemento_vazio(vetor, elemento):
        for item in vetor:
            if item == elemento:
                return True
            return False
        
        vetor_vazio = []
        
        elemento_busca = 10
        
        resultado = busca_elemento_vazio(vetor_vazio, elemento_busca)
        
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def busca_elemento_unico(vetor, elemento):
        for item in vetor:
            if item == elemento:
                return True
            return False
        
        vetor_unico = [3, 9, 200, 42, 29, 44 ]
        
        elemento_busca = [42]
        
        resultado = busca_elemento_unico(vetor, elemento_busca)
        