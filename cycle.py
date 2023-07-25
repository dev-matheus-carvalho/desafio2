# Função que verifica se uma lista encadeada possui um ciclo.
def ciclo(head):
    # Inicializa dois ponteiros "dev = devagar" e "rap = rapido" apontando para a head da lista.
    dev = rap = head

    # Executa um loop enquanto o ponteiro "rap" não for None e seu próximo nó também não for None.
    while rap != None and rap.next != None:
        # Move o ponteiro "dev" uma posição à frente.
        dev = dev.next
        # Move o ponteiro "rap" duas posições à frente.
        rap = rap.next.next

        # Verifica se os ponteiros "dev" e "rap" apontam para o mesmo nó.
        # Se isso acontecer, significa que a lista tem um ciclo e a função retorna True.
        if dev == rap:
            return True

    # Se o loop terminar sem encontrar um ciclo, a função retorna False.
    return False
