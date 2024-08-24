import sys
from src.Info import Info
from src.Node import Node
from src.Arvore import Arvore

def carregar_entrada():
    matriz = []
    for linha in sys.stdin:
        elementos = list(map(int, linha.split()))
        matriz.append(elementos)
    return matriz

if __name__ == '__main__':
    # Carregar a matriz da entrada padrão
    inicio = carregar_entrada()
    
    # Estado objetivo
    final = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    # Cria a árvore e executa o algoritmo
    arvore = Arvore(Node(Info(inicio)), final)
    
    # Reconstruir o caminho completo do nó final até o nó inicial
    caminho_no_buscado = arvore.reconstruir_caminho(arvore.HEAD)

    # Imprime o caminho
    arvore.imprimir_caminho(caminho_no_buscado)
