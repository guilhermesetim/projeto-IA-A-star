class Node:
    contador = 0
    
    def __init__(self, info, g=0, h=0, mov_adjacente=0, pai=None):
        self._id = Node.contador
        Node.contador += 1

        self.info = info
        self.filhos = []
        self.mov_adjacente = mov_adjacente
        self.g = g  # Custo do caminho até o nó atual
        self.h = h  # Estimativa heurística (distância de Manhattan)
        self.pai = pai  # Referência ao nó pai

    def __str__(self) -> str:
        return self.info.getMensagem()
    
    def getValor(self):
        return self.info.getValor()

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)