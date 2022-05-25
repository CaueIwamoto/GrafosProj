import os

print("--------------- Grafos ---------------")
#Primeira parte onde o programa abre o arquivo "A.txt" (entrada a matriz "A" de adjacência) e lê:
def main():
    archive = open("A.txt", "r")
    dados = archive.readlines()
    archive.close()
    for n in range(len(dados)):
        dados[n] = dados[n].split()
    #Utiliza o filtro "None" da lista para remover algum conteúdo vazio:
    dados = list(filter(None, dados))

    Grafoex, graus, somatoria = SequenciaGraus(dados)
    if not Grafoex:
        exit()

    #Variáveis (grafos):  
    Narestas(somatoria)
    simples = grafoSimples(dados)  
    grafoCompleto(dados, simples)
    grafoRegular(graus)
    bipartido, x, y = grafoBipartido(dados)
    grafoBiparCompleto(simples, bipartido, x, y)

#Sequencia dos graus:    
def SequenciaGraus(matriz):
    graus = []
    for linha in range(len(matriz)):
        graus.append(0)
        for coluna in range(len(matriz)):
            if linha == coluna:
                graus[linha] += (int(matriz[linha][coluna])*2)
            else:
                graus[linha] += int(matriz[linha][coluna])

    somatoria = 0
    for item in range(len(graus)):
        somatoria += graus[item]

    if somatoria % 2 == 1:
        print("O grafo nao existe.")
        return False, graus, somatoria
    else:
        graus = ordemDecrescente(graus)
        print("Sequencia dos graus do grafo: ", end=" ")
        print(*graus, sep=", ")
        return True, graus, somatoria

#Organizar os dados em ordem crescente e tambehm inverter a lista:
def ordemDecrescente(graus):
    graus = sorted(graus)
    graus = graus[::-1]
    return graus


#Função que faz a verificação dos números de arestas do grafo:
def Narestas(somaDosGraus):
    arestas = somaDosGraus/2
    print("Numero de arestas do grafo: ", int(arestas))

#Função que averigua a existência de laços/arestas múltiplas:
def verificarLacos(matriz):
    lacos = []
    arestasMultiplas = []

    #Valores que se forem maior que 0, ele será um laço; Valores maior que 1, será aresta múltipla.:
    for linha in range(len(matriz)):
        for coluna in range(linha, len(matriz)):
            if linha == coluna and int(matriz[linha][coluna]) > 0: 
                lacos.append("v{0}".format (linha+1))
            elif int(matriz[linha][coluna]) > 1:
                arestasMultiplas.append("v{0} e v{1}".format (linha+1, coluna+1))

    return lacos, arestasMultiplas

#Grafo simples:
def grafoSimples(matriz):
    lacos, arestasMultiplas = verificarLacos(matriz)
    
    #Prints grafo simples:
    if lacos and arestasMultiplas:
        print("O grafo eh simples? R- Nao.")
        print("O grafo nao eh simples pois apresenta ele lacos e arestas multiplas.")
        screenshotLacos(lacos, arestasMultiplas)
        return False

    #Averiguar se o grafo tem laços ou arestas múltiplas:
    elif lacos or arestasMultiplas:
        if lacos:
            print("O grafo eh simples? R- Nao.")
            print("O grafo nao eh simples pois apresenta lacos.")

        if arestasMultiplas:
            print("O grafo eh simples? R - Nao.")
            print("O grafo nao eh simples pois apresenta arestas multiplas.")

        screenshotLacos(lacos, arestasMultiplas)
        return False
    else:
        print("O grafo eh simples? R- Sim.")
        print("O grafo eh simples pois ele nao apresenta lacos e arestas multiplas.")
        return True

#Prints para ver se o grafo possui vértices com arestas múltiplas e/ou com laços:
def screenshotLacos (lacos, arestasMultiplas):
    if arestasMultiplas:
        print("Vertices com arestas multiplas: ", end=" ")
        print(*arestasMultiplas, sep=", ")
    else:
        print("O grafo nao tem arestas multiplas.")

    if lacos:
        print("Vertices com lacos: ", end=" ")
        print(*lacos, sep=", ")
    else:
        print("O grafo nao tem lacos.")

#Grafo completo:
def grafoCompleto(matriz, simples):
    #Se nao for simples, nao será completo:
    if not simples:
        completo = False
    else:
        completo = True
        #Valores que forem maior que 0, ele será um laço; Valores maior que 1, será aresta múltipla.:
        for linha in range(len(matriz)):
            for coluna in range(len(matriz)):
                if linha == coluna and int(matriz[linha][coluna]) != 0:
                    completo = False
                    break
                elif linha != coluna and int(matriz[linha][coluna]) != 1:
                    completo = False
                    break
    #Prints grafo completo:
    if completo:
        print("O grafo eh completo? R- Sim.")
        print("O grafo eh completo por conta dele ser simples. E cada um de seus vertices sao adjacentes aos outros vertices.")
    else:
        print("O grafo eh completo? R- Nao.")
        if not simples:
            print("O grafo nao eh completo pois nao eh simples.")
        else:
            print("O grafo nao eh completo. Apesar do grafo ser simples, nao sao todos os vertices que serao adjacentes aos outros vertices.")

#Grafo regular:
def grafoRegular(graus):
    regular = True
    for item in graus:
        if graus[0] == item:
            pass
        else:
            regular = False
            break
    
    #Prints grafo regular:
    if regular:
        print("O grafo eh regular? R- Sim.")
        print("O grafo eh regular porque todos os vertices possuem o mesmo grau.")
    else:
        print("O grafo eh regular? R- Nao.")
        print("O grafo nao eh regular porque nem todos os vertices possuem o mesmo grau.")

#Grafo bipartido:
def grafoBipartido (matriz):
    x = [0]
    y = []
    bipartido2 = True
    
    #Averiguar quando o grafo possuir laços:
    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if linha in x and int(matriz[linha][coluna]) != 0 and coluna not in y:
                if coluna in x:
                    bipartido2 = False
                else:
                    y.append(coluna)
            elif linha in y and int(matriz[linha][coluna]) != 0 and coluna not in x:
                if coluna in y:
                    bipartido2 = False
                else:
                    x.append(coluna)
    
    #Prints grafo bipartido:
    if bipartido2:
        print("O grafo eh bipartido? R- Sim.")
        print("O grafo eh bipartido porque os vertices podem ser divididos em dois conjuntos disjuntos.")
        screenshotParteBiparticao(x, y)
        return True, x, y
    else:
        print("O grafo eh bipartido? R- Nao.")
        print("O grafo nao eh bipartido porque os vertices nao podem ser divididos em dois conjuntos disjuntos.")
        return False, False, False

#Grafo bipartido completo:
def grafoBiparCompleto (simples, bipartido, x, y):
    #Prints grafo bipartido completo:
    if simples and bipartido:
        print("O grafo eh bipartido completo? R- Sim.")
        print("O grafo eh bipartido completo pois ele eh simples e bipartido.")
        screenshotParteBiparticao(x, y)
    else:
        print("O grafo eh bipartido completo? R- Nao.")
        if not bipartido:
            print("O grafo nao eh bipartido completo pois ele nao eh bipartido.")
        elif not simples:
            print("O grafo nao eh bipartido completo pois ele nao eh simples.")

#Em caso afirmativo de grafo bipartido completo, bipartição do grafo:
def screenshotParteBiparticao (x, y):
    print("Bipartição: ")
    print("X = {", end="")
    for v in x:
        if v == x[-1]:
            print("v{0}".format (v+1), end="}\n")
        else:
            print("v{0}".format (v+1), end=", ")

    print("Y = {", end="")
    for v in y:
        if v == y[-1]:
            print("v{0}".format (v+1), end="}\n")
        else:
            print("v{0}".format (v+1), end=", ")

main()
