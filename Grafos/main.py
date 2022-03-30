#-----------------------
# BIBLIOTECAS
#-----------------------
import os
import sys
#-----------------------
# CLASSES
#-----------------------
class matrizDeGrafos:
    def __init__(self,vertices:int=0)->None:
        self.vertices = vertices;
        self.grafo = [[None] * self.vertices for i in range(self.vertices)];

    def adicionarAresta(self,v1:int=0,v2:int=0,peso:int=0)->None:
        self.grafo[v1-1][v2-1] = peso;
        self.grafo[v2-1][v1-1] = peso;

    def tostring(self)->str:
        [k,l] = [1,1];
        mensagem = f"Matriz de Adjacencia:\n";
        for i in range(self.vertices):
            if i == 0:
                while k <= self.vertices:
                    mensagem += f"\t{k}";
                    k += 1
            for j in range(self.vertices):
                if j == 0:
                    mensagem += f"\n{l}";
                    l += 1
                mensagem += f"\t{self.grafo[i][j]}";
        return mensagem;
#-----------------------
# FUNÇÕES
#-----------------------
def pausarTela()->None:
    mensagem = f"\nDigite o enter para continuar!\n"
    input(mensagem);

def limparTela()->None:
    os.system("clear || cls")
#-----------------------
# M A I N ()
#-----------------------
if __name__ == '__main__':
    numerosDeVertices = 0; 
    opcao = 0;
    while((numerosDeVertices <= 0) or (numerosDeVertices > 20)):
        mensagem = f"Digite a quantidade de vertices entre 1-20: ";
        numerosDeVertices = int(input(mensagem));
    grafo = matrizDeGrafos(vertices=numerosDeVertices);

    while(True):
        limparTela();
        mensagem = f"\tMenu\n1 - Inserir arestas\n2 - Imprimir matriz\n3 - Sair";
        print(mensagem);
        mensagem = f"Opcao: ";
        opcao = int(input(mensagem))
        if opcao == 1:
            vertice = [];
            for i in range(2):
                limparTela();
                if i == 0:
                    ponto = 'inicial';
                else:
                    ponto = 'de chegada';
                mensagem = f"Digite o ponto {ponto} de 1 até {numerosDeVertices}: ";
                vertice.append(int(input(mensagem)));
                if i == 0:
                    while((vertice[i] < 1) or (vertice[i] > numerosDeVertices)):
                        print("\nValor inválido\nDigite novamente\n");
                        vertice[i] = int(input(mensagem));
                else:
                    while((vertice[i] < 1) or (vertice[i] > numerosDeVertices) or (vertice[i] == vertice[i-1])):
                        print("\nValor inválido\nDigite novamente\n");
                        vertice[i] = int(input(mensagem));
                    mensagem = f"\nDigite o peso da aresta: ";
                    peso = int(input(mensagem));
                    grafo.adicionarAresta(v1=vertice[i-1],v2=vertice[i],peso=peso);
        elif opcao == 2:
            limparTela();
            print(grafo.tostring());
            pausarTela();
        elif opcao == 3:
            limparTela();
            sys.exit(0);
        else:
            limparTela();
            print("Digite novamente um valor válido entre 1-3");
            pausarTela();
#-----------------------