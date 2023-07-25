# Definição da classe No que representa os nós da árvore binária de busca.
class No:
    def __init__(self, valor):
        # Valor armazenado no nó.
        self.valor = valor
        # Altura do nó na árvore.
        self.altura = 0
        # Referência para o nó filho esquerdo.
        self.esquerda = None
        # Referência para o nó filho direito.
        self.direita = None


# Função para inserir um novo valor na árvore binária de busca.
def inserir(raiz, valor):
    # Caso base: se a árvore está vazia (raiz é None), cria um novo nó com o valor e altura adequados e o torna a nova raiz.
    if raiz is None:
        raiz = No(valor)
    else:
        # Caso contrário, insere o valor na subárvore esquerda ou direita, de acordo com o valor do nó atual.
        if valor <= raiz.valor:
            raiz.esquerda = inserir(raiz.esquerda, valor)
        else:
            raiz.direita = inserir(raiz.direita, valor)

    # Atualiza a altura do nó e realiza o balanceamento da árvore após a inserção.
    raiz = balancear(raiz)
    return raiz


# Função para calcular a altura de um nó na árvore.
def altura(raiz):
    if raiz is None:
        return -1
    else:
        return raiz.altura


# Função para calcular o fator de balanceamento de um nó na árvore.
def fator_balanceamento(raiz):
    return altura(raiz.esquerda) - altura(raiz.direita)


# Função para ajustar a altura de um nó após a inserção ou rotação.
def definir_altura(raiz):
    return max(altura(raiz.esquerda), altura(raiz.direita)) + 1


# Função para balancear a árvore após a inserção.
def balancear(raiz):
    if raiz is None:
        return None

    # Atualiza a altura do nó com base na altura dos filhos.
    raiz.altura = definir_altura(raiz)

    # Calcula o fator de balanceamento para verificar se o nó está desbalanceado.
    balanceamento = fator_balanceamento(raiz)

    # Verifica se a árvore está desbalanceada para a esquerda.
    if balanceamento > 1:
        # Verifica qual tipo de rotação é necessária (simples ou dupla) e realiza a rotação apropriada.
        if altura(raiz.esquerda.esquerda) >= altura(raiz.esquerda.direita):
            raiz = rotacao_direita(raiz)
        else:
            raiz.esquerda = rotacao_esquerda(raiz.esquerda)
            raiz = rotacao_direita(raiz)
    # Verifica se a árvore está desbalanceada para a direita.
    elif balanceamento < -1:
        # Verifica qual tipo de rotação é necessária (simples ou dupla) e realiza a rotação apropriada.
        if altura(raiz.direita.direita) >= altura(raiz.direita.esquerda):
            raiz = rotacao_esquerda(raiz)
        else:
            raiz.direita = rotacao_direita(raiz.direita)
            raiz = rotacao_esquerda(raiz)

    return raiz


# Função para realizar uma rotação à direita em torno do nó 'raiz'.
def rotacao_direita(raiz):
    nova_raiz = raiz.esquerda
    raiz.esquerda = nova_raiz.direita
    nova_raiz.direita = raiz

    # Atualiza as alturas dos nós envolvidos na rotação.
    raiz.altura = definir_altura(raiz)
    nova_raiz.altura = definir_altura(nova_raiz)
    return nova_raiz


# Função para realizar uma rotação à esquerda em torno do nó 'raiz'.
def rotacao_esquerda(raiz):
    nova_raiz = raiz.direita
    raiz.direita = nova_raiz.esquerda
    nova_raiz.esquerda = raiz

    # Atualiza as alturas dos nós envolvidos na rotação.
    raiz.altura = definir_altura(raiz)
    nova_raiz.altura = definir_altura(nova_raiz)
    return nova_raiz


# Função principal para interação com o usuário e teste da árvore binária de busca.
def main():
    raiz = None
    while True:
        try:
            valor = int(input("Digite um valor para inserir na árvore (ou qualquer outra tecla para sair): "))
            raiz = inserir(raiz, valor)
            print("Árvore atualizada:")
            imprimir_arvore(raiz)
        except ValueError:
            print("Saindo do programa.")
            break


# Função para imprimir a árvore em formato de árvore binária.
def imprimir_arvore(raiz, nivel=0, prefixo="Raiz: "):
    if raiz is not None:
        print(" " * (nivel * 4) + prefixo + str(raiz.valor))
        imprimir_arvore(raiz.esquerda, nivel + 1, "E --- ")
        imprimir_arvore(raiz.direita, nivel + 1, "D --- ")


# Chama a função principal para iniciar a interação com o usuário e construir a árvore binária de busca.
if __name__ == "__main__":
    main()
