# Projeto Quebra-Cabeça de 8 peças com o Algoritmo A*

Este projeto implementa a solução para o problema do Quebra-Cabeça de 8 peças com o Algoritmo A*, que processa matrizes como entradas, utilizando Python. O arquivo de entrada contendo a matriz inicial é lido a partir de arquivos `.txt` localizados no diretório `input`.

## Pré-requisitos

Certifique-se de ter o Python 3 instalado em seu ambiente.

- **Python 3.6 ou superior**


## Estrutura do projeto

- **src/**: Diretório contendo os módulos de classes que definem a lógica da árvore, nós e informações.
- **input/**: Diretório onde os arquivos de entrada (.txt) com as matrizes devem ser colocados.
- **main.py**: O script principal que coordena a execução do programa.
- **README.md**: Arquivo de documentação do projeto.


## Como Executar

1. Coloque o arquivo de entrada no diretório `input/`. O arquivo deve conter a matriz inicial, com elementos separados por espaços e linhas separadas por quebras de linha.

   **Exemplo (`input/nome_arquivo.txt`):**


2. No terminal, navegue até a raiz do projeto e execute o programa redirecionando o conteúdo do arquivo de entrada:

```bash
python3 main.py < input/nome_arquivo.txt
