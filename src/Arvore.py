from src import Info, Node

import copy
import heapq


class Arvore:

    def __init__(self, estadoInicial, final):
        self.raiz = estadoInicial
        self.filaNode = []
        heapq.heappush(self.filaNode, estadoInicial)
        self.HEAD = None
        self.final = final
        encontrou = False


        # Gera a árvore de possibilidades 
        while len(self.filaNode) > 0 and not encontrou:
            self.HEAD = heapq.heappop(self.filaNode)

            if self.HEAD.getValor() == final:
                encontrou = True
                break

            i, j = self.HEAD.info.posicaoVazio()
            filhos = self.realizar_movimentos(self.HEAD, i, j)


            # Adiciona os filhos ao No
            for info in filhos:
                # Custo do caminho
                g = self.HEAD.g + 1  
                # Heurística de Manhattan
                h = self.calcular_heuristica(info['estado'], final)  
                # Gera um novo Node
                novo_node = Node(Info(info['estado']), g, h, info['adjacente'], pai=self.HEAD)

                self.HEAD.filhos.append(novo_node)
                heapq.heappush(self.filaNode, novo_node)


    # Realiza os movimentos
    def realizar_movimentos(self, node, i, j):
        listaFilhos = []

        # peça movimentando de cima para baixo
        if i > 0 and node.mov_adjacente != 3:
            mov_up = copy.deepcopy(node.info.estado)
            mov_up[i][j] = node.info.estado[i-1][j]
            mov_up[i-1][j] = 0
            listaFilhos.append({'adjacente': 1, 'estado': mov_up})
        
        # peça movimentando da esquerda para direita
        if j > 0 and node.mov_adjacente != 4:
            mov_left = copy.deepcopy(node.info.estado)
            mov_left[i][j] = node.info.estado[i][j-1]
            mov_left[i][j-1] = 0
            listaFilhos.append({'adjacente': 2, 'estado': mov_left})

        # peça movimentando de baixo para cima
        if i < 2 and node.mov_adjacente != 1:
            mov_down = copy.deepcopy(node.info.estado)
            mov_down[i][j] = node.info.estado[i+1][j]
            mov_down[i+1][j] = 0
            listaFilhos.append({'adjacente': 3, 'estado': mov_down})

        # peça movimentando da direita para esquerda
        if j < 2 and node.mov_adjacente != 2:
            mov_right = copy.deepcopy(node.info.estado)
            mov_right[i][j] = node.info.estado[i][j+1]
            mov_right[i][j+1] = 0
            listaFilhos.append({'adjacente': 4, 'estado': mov_right})
        
        return listaFilhos


    # Calculo da Heurística
    def calcular_heuristica(self, estado, final):
        # Distância de Manhattan
        dist = 0
        for i in range(3):
            for j in range(3):
                valor = estado[i][j]
                if valor != 0:
                    final_i, final_j = [(x, y) for x in range(3) for y in range(3) if final[x][y] == valor][0]
                    dist += abs(i - final_i) + abs(j - final_j)
        return dist

    # Reconstroe o caminho para o início 
    def reconstruir_caminho(self, node):
        caminho = []
        while node:
            caminho.append(node)
            node = node.pai
        caminho.reverse()
        return caminho

    # Apresenta o caminho
    def imprimir_caminho(self, caminho):
        if caminho:
            for i, node in enumerate(caminho):
                print(node)
        else:
            print("Caminho não encontrado.")