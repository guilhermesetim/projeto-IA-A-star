class Info:

    def __init__(self, estado):
        self.estado = estado

    def getMensagem(self):
        msg = '\n'
        for i in range(3):
            for j in range(3):
                msg += str(self.estado[i][j]) + ' '
            msg += '\n' 
        return msg
    
    def getValor(self):
        return self.estado
    
    def posicaoVazio(self):
        for i in range(3):
            for j in range(3):
                if self.estado[i][j] == 0:
                    return i, j