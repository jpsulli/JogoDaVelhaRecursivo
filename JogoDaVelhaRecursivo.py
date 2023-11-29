import copy

class Jogo:
    def __init__(self, matriz, peca=None, numPecas=0, modLinha=None, modColuna=None):
        self.matriz = matriz
        self.peca = peca
        self.numPecas = numPecas
        self.modLinha = modLinha
        self.modColuna = modColuna

    def addPeca(self, l, c, valor):
        self.matriz[l][c] = valor
        self.numPecas += 1
        self.modLinha = l
        self.modColuna = c
        self.peca = self.definirPeca()

    def jogadorVenceu(self):
        for i in range(len(self.matriz)):
            if sum(self.matriz[i]) == 3:  # verifica as linhas do tabuleiro
                return True
            # verificando as colunas
            coluna = []
            for j in range(len(self.matriz)):
                coluna += [self.matriz[j][i]]
                if sum(coluna) == 3:
                    return True

            # verificando as diagonais
        diagonalprincipal = [self.matriz[0][0], self.matriz[1][1], self.matriz[2][2]]
        diagonalsecundaria = [self.matriz[0][2], self.matriz[1][1], self.matriz[2][0]]
        if sum(diagonalsecundaria) == 3 or sum(diagonalprincipal) == 3:
            return True
        return False

    def maquinaVenceu(self):
        for i in range(len(self.matriz)):
            if sum(self.matriz[i]) == -3:  # verifica as linhas do tabuleiro
                return True
            # verificando as colunas
            coluna = []
            for j in range(len(self.matriz)):
                coluna += [self.matriz[j][i]]
                if sum(coluna) == -3:
                    return True

            # verificando as diagonais
        diagonalprincipal = [self.matriz[0][0], self.matriz[1][1], self.matriz[2][2]]
        diagonalsecundaria = [self.matriz[0][2], self.matriz[1][1], self.matriz[2][0]]
        if sum(diagonalsecundaria) == -3 or sum(diagonalprincipal) == -3:
            return True
        return False

    def jogoCheio(self):
        if self.matriz[0][0] != 0 and self.matriz[0][1] != 0 and self.matriz[0][2] != 0 and self.matriz[1][0] != 0 and self.matriz[1][1] != 0 and self.matriz[1][2] != 0 and self.matriz[2][0] != 0 and self.matriz[2][1] != 0 and self.matriz[2][2] != 0:
            return True
        else:
            return False

    def definirPeca(self):
        if self.jogadorVenceu():
            return "X"
        elif self.maquinaVenceu():
            return "O"
        elif self.jogoCheio():
            return "Y"
        else:
            return None

    def chancesJogador(self):
        i = 0
        for l in range(3):
            if self.matriz[l][0] != -1 and self.matriz[l][1] != -1 and self.matriz[l][2] != -1:
                i += 1
        for c in range(3):
            if self.matriz[0][c] != -1 and self.matriz[1][c] != -1 and self.matriz[2][c] != -1:
                i += 1
        if self.matriz[0][0] != -1 and self.matriz[1][1] != -1 and self.matriz[2][2] != -1:
            i += 1
        if self.matriz[0][2] != -1 and self.matriz[1][1] != -1 and self.matriz[2][0] != -1:
            i += 1
        return i

    def chancesMaquina(self):
        i = 0
        for l in range(3):
            if self.matriz[l][0] != 1 and self.matriz[l][1] != 1 and self.matriz[l][2] != 1:
                i += 1
        for c in range(3):
            if self.matriz[0][c] != 1 and self.matriz[1][c] != 1 and self.matriz[2][c] != 1:
                i += 1
        if self.matriz[0][0] != 1 and self.matriz[1][1] != 1 and self.matriz[2][2] != 1:
            i += 1
        if self.matriz[0][2] != 1 and self.matriz[1][1] != 1 and self.matriz[2][0] != 1:
            i += 1
        return i

    def heuristica(self):
        if self.maquinaVenceu():
            return 100000
        elif self.jogadorVenceu():
            return -100000
        else:
            return self.chancesMaquina() - self.chancesJogador()

    def printJogo(self):
        for linha in self.matriz:
            print(linha)


class No:
    def __init__(self, valor, pai=None, peso=None):
        self.valor = valor
        self.filhos = []
        self.pai = pai
        self.peso = peso

    def adicionarFilho(self, filho):
        filho.pai = self
        self.filhos.append(filho)

def empate(jogo):
    for l in range(3):
        if jogo[l][0].peca == "Y" and jogo[l][1].peca == "Y" and jogo[l][2].peca == "Y":
            return True
    for c in range(3):
        if jogo[0][c].peca == "Y" and jogo[1][c].peca == "Y" and jogo[2][c].peca == "Y":
            return True
    if jogo[0][0].peca == "Y" and jogo[1][1].peca == "Y" and jogo[2][2].peca == "Y":
        return True
    if jogo[0][2].peca == "Y" and jogo[1][1].peca == "Y" and jogo[2][0].peca == "Y":
        return True
    return False
def jogadorVenceuJogo(jogo):
    for l in range(3):
        if (jogo[l][0].peca == "X" or jogo[l][0].peca == "Y") and (
                jogo[l][1].peca == "X" or jogo[l][1].peca == "Y") and (
                jogo[l][2].peca == "X" or jogo[l][2].peca == "Y"):
            return True
    for c in range(3):
        if (jogo[0][c].peca == "X" or jogo[0][c].peca == "Y") and (
                jogo[1][c].peca == "X" or jogo[1][c].peca == "Y") and (
                jogo[2][c].peca == "X" or jogo[2][c].peca == "Y"):
            return True
    if (jogo[0][0].peca == "X" or jogo[0][0].peca == "Y") and (
            jogo[1][1].peca == "X" or jogo[1][1].peca == "Y") and (
            jogo[2][2].peca == "X" or jogo[2][2].peca == "Y"):
        return True
    if (jogo[0][2].peca == "X" or jogo[0][2].peca == "Y") and (
            jogo[1][1].peca == "X" or jogo[1][1].peca == "Y") and (
            jogo[2][0].peca == "X" or jogo[2][0].peca == "Y"):
        return True
    return False
def maquinaVenceuJogo(jogo):
    for l in range(3):
        if (jogo[l][0].peca == "O" or jogo[l][0].peca == "Y") and (
                jogo[l][1].peca == "O" or jogo[l][1].peca == "Y") and (
                jogo[l][2].peca == "O" or jogo[l][2].peca == "Y"):
            return True
    for c in range(3):
        if (jogo[0][c].peca == "O" or jogo[0][c].peca == "Y") and (
                jogo[1][c].peca == "O" or jogo[1][c].peca == "Y") and (
                jogo[2][c].peca == "O" or jogo[2][c].peca == "Y"):
            return True
    if (jogo[0][0].peca == "O" or jogo[0][0].peca == "Y") and (
            jogo[1][1].peca == "O" or jogo[1][1].peca == "Y") and (
            jogo[2][2].peca == "O" or jogo[2][2].peca == "Y"):
        return True
    if (jogo[0][2].peca == "O" or jogo[0][2].peca == "Y") and (
            jogo[1][1].peca == "O" or jogo[1][1].peca == "Y") and (
            jogo[2][0].peca == "O" or jogo[2][0].peca == "Y"):
        return True
    return False

def jogoTotalmenteCheio(jogo):
    for l in range(3):
        for c in range(3):
            if not jogo[l][c].jogoCheio():
                return False
    return True

def fimDeJogo(jogo):
    if maquinaVenceuJogo(jogo) or jogadorVenceuJogo(jogo) or jogoTotalmenteCheio(jogo):
        return True
    else:
        return False

def acharJogo(jogo):
    pecas = 10
    linha, coluna = None, None
    for i in range(3):
        for j in range(3):
            if jogo.valor[i][j].peca is None:
                if jogo.valor[i][j].numPecas < pecas:
                    linha = i
                    coluna = j
    return linha, coluna

def acharJogo2(jogo):
    pecas = 10
    linha, coluna = None, None
    for i in range(3):
        for j in range(3):
            if jogo[i][j].peca is None:
                if jogo[i][j].numPecas < pecas:
                    linha = i
                    coluna = j
    return linha, coluna

def chancesMaquina(jogo):
    i = 0
    for l in range(3):
        if jogo[l][0].peca != "X" and jogo[l][1].peca != "X" and jogo[l][2].peca != "X":
            i += 1
    for c in range(3):
        if jogo[0][c].peca != "X" and jogo[1][c].peca != "X" and jogo[2][c].peca != "X":
            i += 1
    if jogo[0][0].peca != "X" and jogo[1][1].peca != "X" and jogo[2][2].peca != "X":
        i += 1
    if jogo[0][2].peca != "X" and jogo[1][1].peca != "X" and jogo[2][0].peca != "X":
        i += 1
    return i


def chancesJogador(jogo):
    i = 0
    for l in range(3):
        if jogo[l][0].peca != "O" and jogo[l][1].peca != "O" and jogo[l][2].peca != "O":
            i += 1
    for c in range(3):
        if jogo[0][c].peca != "O" and jogo[1][c].peca != "O" and jogo[2][c].peca != "O":
            i += 1
    if jogo[0][0].peca != "O" and jogo[1][1].peca != "O" and jogo[2][2].peca != "O":
        i += 1
    if jogo[0][2].peca != "O" and jogo[1][1].peca != "O" and jogo[2][0].peca != "O":
        i += 1
    return i

def heuristica(jogo):
    if maquinaVenceuJogo(jogo):
        return 100000
    elif jogadorVenceuJogo(jogo):
        return -100000
    else:
        return chancesMaquina(jogo) - chancesJogador(jogo)
def MinMax(raiz, nivel, cont, l, c):
    if (nivel-cont) % 2 == 0:
        max = True
    else:
        max = False

    if raiz.valor[l][c].peca is not None:
        linha, coluna = acharJogo(raiz)
        l = linha
        c = coluna

    for i in range(3):
        for j in range(3):
            if raiz.valor[l][c].matriz[i][j] == 0:
                jogoG = copy.deepcopy(raiz.valor)
                jogo = copy.deepcopy(raiz.valor[l][c])
                if max:
                    ## jogo.valor[l][c].matriz[i][j] = -1
                    jogo.addPeca(i, j, -1)
                else:
                    ##jogo.valor[l][c].matriz[i][j] = 1
                    jogo.addPeca(i, j, 1)
                jogoG[l][c] = jogo
                filho = No(jogoG)
                raiz.adicionarFilho(filho)
                if cont-1 > 0 and not fimDeJogo(jogoG): ##and jogo.peca is None
                    MinMax(filho, nivel, cont - 1, i, j)
                    # if filho.valor[i][j].peca is None:
                    #     MinMax(filho, nivel, cont-1, i, j)
                    # else:
                    #     linha, coluna = acharJogo(filho)
                    #     MinMax(filho, nivel, cont-1, linha, coluna)
                else:
                    filho.peso = 2*heuristica(filho.valor) + filho.valor[i][j].heuristica()
    if max:
        raiz.peso = -500000
        for filho in raiz.filhos:
            if filho.peso > raiz.peso:
                raiz.peso = filho.peso
    else:
        raiz.peso = 500000
        for filho in raiz.filhos:
            if filho.peso < raiz.peso:
                raiz.peso = filho.peso


def maquinaJogaPadrao(raiz, nivel, l, c):
    MinMax(raiz, nivel, nivel, l, c)

    for filho in raiz.filhos:
        if filho.peso == raiz.peso:
            return filho.valor, filho.valor[l][c].modLinha, filho.valor[l][c].modColuna

def printJogoAtual(jogoAtual):
    for linha in jogoAtual:
        print(linha[0].matriz[0], "     |     ", linha[1].matriz[0], "     |     ", linha[2].matriz[0])
        print(linha[0].matriz[1], "     |     ", linha[1].matriz[1], "     |     ", linha[2].matriz[1])
        print(linha[0].matriz[2], "     |     ", linha[1].matriz[2], "     |     ", linha[2].matriz[2])
        print(linha[0].peca, linha[1].peca, linha[2].peca)
        print("------------------------------------------------------------------------------")


nivel = int(input("Qual é o nível de profundidade desejado para o MinMax? "))

print("\nInicio do Jogo \n")

matriz1 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz2 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz3 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz4 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz5 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz6 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz7 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz8 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz9 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

jogo1 = Jogo(matriz1)
jogo2 = Jogo(matriz2)
jogo3 = Jogo(matriz3)
jogo4 = Jogo(matriz4)
jogo5 = Jogo(matriz5)
jogo6 = Jogo(matriz6)
jogo7 = Jogo(matriz7)
jogo8 = Jogo(matriz8)
jogo9 = Jogo(matriz9)

jogoAtual = [[jogo1, jogo2, jogo3],
             [jogo4, jogo5, jogo6],
             [jogo7, jogo8, jogo9]]

printJogoAtual(jogoAtual)

# for i in range(3):
#     for j in range(3):
#         jogoAtual[i][j].printJogo()
#         print()

jogol, jogoc = map(int, input("Indique o jogo em que deseja começar: ").split())

print("\n")

while True:

    if jogoAtual[jogol][jogoc].peca is not None:
        jogol, jogoc = acharJogo2(jogoAtual)

    print("Você está jogando no jogo: ", jogol, jogoc)
    l, c = map(int, input("Indique a posição desejada: ").split())
    jogoAtual[jogol][jogoc].addPeca(l,c,1)


    printJogoAtual(jogoAtual)

    # for i in range(3):
    #     for j in range(3):
    #         jogoAtual[i][j].printJogo()
    #         print()

    if empate(jogoAtual):
        print("\nDEU VELHA!!!\n")
        break

    if jogadorVenceuJogo(jogoAtual):
        print("\nJOGADOR VENCEU!!!\n")
        break

    if jogoTotalmenteCheio(jogoAtual):
        print("\nDEU VELHA!!!\n")
        break

    raiz = No(jogoAtual)

    jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, l, c)

    print("\nVez da Máquina")

    if raiz.valor[l][c].peca is not None:
        l, c = acharJogo(raiz)

    print("Máquina está jogando no jogo: ", l, c)
    printJogoAtual(jogoAtual)

    # for linha in range(3):
    #     for coluna in range(3):
    #         jogoAtual[linha][coluna].printJogo()
    #         print()

    print("\n")

    if empate(jogoAtual):
        print("\nDEU VELHA!!!\n")
        break

    if maquinaVenceuJogo(jogoAtual):
        print("MAQUINA VENCEU!!!")
        break

