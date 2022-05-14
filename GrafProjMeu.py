import os

#Primeira parte onde ele abre o archive "A.txt" (entrada a matriz "A" de adjacência) e lê:
def main():
    archive = open("A.txt", "r")
    dados = archive.readlines()
    archive.close()
    for n in range(len(dados)):
        dados[n] = dados[n].split()
    #Utiliza o filtro "None" da lista para remover conteúdo vazio:
    dados = list(filter(None, dados))

    graus, existe, somatoria = SeqGraus(dados)
    if not existe:
        exit()

    #Variáveis (grafos):    
    simples = GrafoSimples(dados)
    grafoRegular(graus)
    grafoCompleto(dados, simples)
    Narestas(somatoria)
    bipartido, x, y = GrafoBipartido(dados)
    BipartidoCompleto(simples, bipartido, x, y)
    
#Verificação dos graus:     
def SeqGraus(Matriz):
    graus = []
    for linha in range(len(Matriz)):
        graus.append(0)
        for coluna in range(len(Matriz)):
            if linha == coluna:
                graus[linha] += (int(Matriz[linha][coluna])*2)
            else:
                graus[linha] += int(Matriz[linha][coluna])

    somatoria = 0
    for item in range(len(graus)):
        somatoria += graus[item]

    if somatoria % 2 == 1:
        print("O grafo nao existe!")
        return False, graus, somatoria
    else:
        graus = decrescente(graus)
        print("Sequencia dos graus do grafo: ", end=" ")
        print(*graus, sep=", ")
        return True, graus, somatoria

#Organizar os dados em ordem crescente e também inverter a lista:
def decrescente(graus):
    graus = sorted(graus)
    graus = graus[::-1] 
    return graus


#Def que faz a verificação dos números de arestas do grafo:
def Narestas(somatoriaDeGraus):
    arestas = somatoriaDeGraus/2
    print("Numero de arestas do grafo: ", int(arestas))

#Função que averigua a existência de arestas/laços múltiplos:
def VerificarLacos(Matriz):
    lacos = []
    ArestasMulti = []

    #Valores que se forem maior que 0, ele será um laço; Valores maior que 1, será aresta múltipla.
    for linha in range(len(Matriz)):
        for coluna in range(linha, len(Matriz)): 
            if linha == coluna and int(Matriz[linha][coluna]) > 0: 
                lacos.append("v{0}".format (linha+1))
            elif int(Matriz[linha][coluna]) > 1:
                ArestasMulti.append("v{0} e v{1}".format (linha+1, coluna+1))

    return lacos, ArestasMulti

#Grafo simples:
def GrafoSimples(Matriz):
    lacos, ArestasMulti = VerificarLacos(Matriz)

    if lacos and ArestasMulti:
        print("O grafo eh simples? Nao.")
        print("O grafo nao eh simples pois ele apresenta lacos e arestas multiplas.")
        printLacos(lacos, ArestasMulti)
        return False

    #Verificar se o grafo tem laços ou arestas múltiplas: 
    elif ArestasMulti or lacos:
        if ArestasMulti: 
            print("O grafo eh simples? Nao.")
            print("O grafo nao eh simples pois ele apresenta arestas multiplas.")

        if lacos: 
            print("O grafo eh simples? Nao.")
            print("O grafo nao eh simples pois ele apresenta lacos.")

        printLacos(ArestasMulti, lacos)
        return False
    else:
        print("O grafo eh simples? Sim.")
        print("O grafo eh simples pois ele nao apresenta laços nem arestas multiplas.")
        return True
#Prints para ver se o grafo possui vértices com arestas múltiplas e/ou com laços:
def printLacos (lacos, ArestasMulti):
    if ArestasMulti:
        print("Vertices com arestas multiplas: ", end=" ")
        print(*ArestasMulti, sep=", ")
    else:
        print("O grafo nao tem arestas multiplas.")

    if lacos:
        print("Vertices com lacos: ", end=" ")
        print(*lacos, sep=", ")
    else:
        print("O grafo nao tem lacos.")

#Grafo completo:
def grafoCompleto(Matriz, simples):
    if not simples:
        completo = False
    else:
        completo = True
        #Valores que se forem maior que 0, ele será um laço; Valores maior que 1, será aresta múltipla.
        for linha in range(len(Matriz)):
            for coluna in range(len(Matriz)):
                if linha == coluna and int(Matriz[linha][coluna]) != 0: # Se o valor da célula for maior que 0 ela é um laço
                    completo = False
                    break
                elif linha != coluna and int(Matriz[linha][coluna]) != 1: # Se o valor da célula for maior que 1 ela é aresta multipla
                    completo = False
                    break
    #Prints grafo completo:
    if completo:
        print("O grafo eh completo? Sim.")
        print("O grafo eh completo pois ele eh simples e cada vertice eh adjacente a todos os outros vertices.")
    else:
        print("O grafo eh completo? Nao.")
        if not simples:
            print("O grafo nao eh completo por conta dele nao ser simples.")
        else:
            print("O grafo nao eh completo pois, apesar de ser simples, nem todos os vertices sao adjacentes a todos os outros vertices.")

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
        print("O grafo eh regular? Sim.")
        print("O grafo eh regular pois todos os seus vertices possuem o mesmo grau.")
    else:
        print("O grafo eh regular? Nao.")
        print("O grafo nao eh regular pois nem todos os seus vertices possuem o mesmo grau.")

#Grafo bipartido:
def GrafoBipartido (Matriz):
    x = [0]
    y = []
    bipartido2 = True
    #Averiguar quando o grafo possuir laços:
    for linha in range(len(Matriz)):
        for coluna in range(len(Matriz)):
            if linha in x and int(Matriz[linha][coluna]) != 0 and coluna not in y:
                if coluna in x:
                    bipartido2 = False
                else:
                    y.append(coluna)
            elif linha in y and int(Matriz[linha][coluna]) != 0 and coluna not in x:
                if coluna in y:
                    bipartido2 = False
                else:
                    x.append(coluna)
    if bipartido2: #Prints:
        print("O grafo eh bipartido? Sim.")
        print("O grafo eh bipartido porque os seus vertices podem ser divididos em dois conjuntos disjuntos.")
        printbiparticao(x, y)
        return True, x, y
    else:
        print("O grafo eh bipartido? Nao.")
        print("O grafo nao eh bipartido pois os seus vértices nao podem ser divididos em dois conjuntos disjuntos.")
        return False, False, False

#Grafo bipartido completo:
def BipartidoCompleto (simples, bipartido, x, y):
    if simples and bipartido: #Prints:
        print("O grafo eh bipartido completo? Sim.")
        print("O grafo eh bipartido completo pois ele eh simples e bipartido.")
        printbiparticao(x, y)
    else:
        print("O grafo eh bipartido completo? Nao.")
        if not bipartido:
            print("O grafo nao eh bipartido completo pois ele nao eh bipartido.")
        elif not simples:
            print("O grafo nao eh bipartido completo pois, apesar de ser bipartido, ele nao eh simples.")
#Em caso afirmativo de grafo bipartido completo, bipartição do grafo:
def printbiparticao (x, y):
    print("Biparticao: ")
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
