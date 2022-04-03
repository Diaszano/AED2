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
        self.valorMaximo = 0;

    def adicionarAresta(self,v1:int=0,v2:int=0,peso:int=0)->None:
        self.grafo[v1-1][v2-1] = peso;
        self.grafo[v2-1][v1-1] = peso;
        self.valorMaximo = self.maximo();

    def tostring(self)->str:
        [k,l] = [1,1];
        mensagem = f"Matriz de Adjacencia:\n";
        for i in range(self.vertices):
            if(i == 0):
                while k <= self.vertices:
                    mensagem += f"\t{k}";
                    k += 1;
            for j in range(self.vertices):
                if(j == 0):
                    mensagem += f"\n{l}";
                    l += 1;
                if(i == j):
                    mensagem += f"\tX";
                else:
                    mensagem += f"\t{self.grafo[i][j]}";
        return mensagem;

    def maximo(self)->int:
        total = 0;
        for i in range(self.vertices):
            for j in range(self.vertices):
                if(self.grafo[i][j] != None):
                    print(self.grafo[i][j])
                    total += self.grafo[i][j];
        return int(total);

    def dijkstra(self,origem:int=0,destino:int=0)->str:
        nulo  = -1;
        tmp   = [origem for _ in range(self.vertices)];
        custo = [[None] * self.vertices for i in range(self.vertices)];
        for i in range(self.vertices):
            for j in range(self.vertices):
                if(self.grafo[i][j] == None):
                    custo[i][j] = nulo;
                else:
                    custo[i][j] = self.grafo[i][j];
        distancia  = [custo[origem][i] for i in range(self.vertices)];
        vizinho    = [0 for _ in range(self.vertices)];
        [distancia[origem],vizinho[origem]] = [0,1];
        melhor = 0;
        for _ in range(self.vertices-1):
            menorDistancia = self.valorMaximo;
            for i in range(self.vertices):
                if((distancia[i] < menorDistancia) and (vizinho[i] == 0) and (distancia[i] != nulo)):
                    menorDistancia = distancia[i];
                    melhor = i;
            vizinho[melhor] = 2;
            for i in range(self.vertices):
                if(vizinho[i] == 0):
                    if((menorDistancia + custo[melhor][i]) < distancia[i]):
                        distancia[i] = menorDistancia + custo[melhor][i];
                        tmp[i] = melhor;
        mensagem = f"{self.tostring()}\n\n";
        
        for i in range(self.vertices):
            if((i != origem) and (i == destino)):
                mensagem += f"O melhor caminho até vertice {i+1} tem um peso de {distancia[i]}\n";
                mensagem += f"O caminho é: {i+1}";
                j = tmp[i];
                mensagem += f"...{j+1}";
                while j != origem:
                    j = tmp[j]
                    mensagem += f"...{j+1}";
        return mensagem;
#-----------------------
# FUNÇÕES
#-----------------------
def pausarTela()->None:
    mensagem = f"\nDigite o enter para continuar!\n";
    input(mensagem);

def limparTela()->None:
    os.system("clear || cls");

def scanfInt(mensagem:str = '')->int:
    limparTela();
    valor = input(mensagem);
    if not(valor.isdigit()):
        valor = scanfInt(mensagem=mensagem);
    return int(valor);
#-----------------------
# M A I N ()
#-----------------------
if __name__ == '__main__':
    [numerosDeVertices,opcao] = [0,0]; 
    while((numerosDeVertices <= 0) or (numerosDeVertices > 20)):
        mensagem = f"Digite a quantidade de vertices entre 1-20: ";
        numerosDeVertices = scanfInt(mensagem=mensagem);
    grafo = matrizDeGrafos(vertices=numerosDeVertices);

    while(True):
        limparTela();
        mensagem = f"\tMenu\n1 - Inserir arestas com seus pesos\n2 - Imprimir a matriz de adjacência\n3 - Imprimir o menor caminho\n4 - Sair";
        mensagem += f"\nOpcao: ";
        opcao = scanfInt(mensagem=mensagem)
        if opcao == 1:
            vertice = [];
            for i in range(2):
                limparTela();
                if i == 0:
                    ponto = 'inicial';
                else:
                    ponto = 'de chegada';
                mensagem = f"Digite o ponto {ponto} de 1 até {numerosDeVertices}: ";
                vertice.append(scanfInt(mensagem=mensagem));
                if i == 0:
                    while((vertice[i] < 1) or (vertice[i] > numerosDeVertices)):
                        print("\nValor inválido\nDigite novamente\n");
                        vertice[i] = scanfInt(mensagem=mensagem);
                else:
                    while((vertice[i] < 1) or (vertice[i] > numerosDeVertices) or (vertice[i] == vertice[i-1])):
                        print("\nValor inválido\nDigite novamente\n");
                        vertice[i] = scanfInt(mensagem=mensagem);
                    mensagem = f"\nDigite o peso da aresta: ";
                    peso = scanfInt(mensagem=mensagem);
                    grafo.adicionarAresta(v1=vertice[i-1],v2=vertice[i],peso=peso);
        elif opcao == 2:
            limparTela();
            print(grafo.tostring());
            pausarTela();
        elif opcao == 3:
            limparTela();
            print(grafo.tostring());
            valor = [];
            for i in range(2):
                if i == 0:
                    ponto = 'inicial';
                else:
                    ponto = 'de chegada';
                mensagem = f"\nDigite o vertice {ponto}: ";
                valor.append(scanfInt(mensagem=mensagem));
                if i == 0:
                    while((valor[i] < 1) or (valor[i] > numerosDeVertices)):
                        print("\nValor inválido\nDigite novamente\n");
                        valor[i] = scanfInt(mensagem=mensagem);
                else:
                    while((valor[i] < 1) or (valor[i] > numerosDeVertices) or (valor[i] == valor[i-1])):
                        print("\nValor inválido\nDigite novamente\n");
                        valor[i] = scanfInt(mensagem=mensagem);
            limparTela();
            print(grafo.dijkstra(origem=valor[0]-1,destino=valor[1]-1));
            pausarTela();
        elif opcao == 4:
            limparTela();
            sys.exit(0);
        else:
            limparTela();
            print("Digite novamente um valor válido entre 1-4");
            pausarTela();
#-----------------------