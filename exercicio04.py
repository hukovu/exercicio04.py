## Primeira questão:
def ordenar_por_vetor(vetor):
    n = len(vetor)
    for i in range(n - 1):
        indice_minimo = 1
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]
#Exemplo de uso:
        vetor = [64, 25, 14, 55, 77]
        ordenar_por_vetor(vetor)
        print("Vetor ordenado por seleção:", vetor)

## Segunda questão:
    def ordenar_vetor(vetor, crescente=true):
        if crescente:
            return sorted(vetor)
        else:
            return sorted(vetor, reverse=true)

    # Exemplos de usos:
    vetor + [64, 35, 12, 22, 11]
    vetor_crescente = ordenar_vetor(vetor)
    print("Vetor ordenado em ordem crescente:", vetor_crescente)
    #decrescente:
    vetor_decrescente = ordenar_vetor(vetor, crescente=False)
    print("Vetor ordenado em ordem decrescente:", vetor_decrescente)

## Terceira questão:
    def encontrar_maximo(vetor):
        if not vetor:
            return None
        maximo = vetor[0]
        for elemento in vetor[1:]:
            if elemento > maximo:
                maximo = elemento
        return maximo
    def encontrar_minimo(vetor):
        if not vetor:
            return None
        minimo = vetor[0]
        for elemento in vetor[1:]:
            if elemento < minimo:
                minimo = elemento
        return minimo

## Quarta questão:
    def segundo_menor(vetor):
        vetor_sem_duplicatas = list(set(vetor))
        if len(vetor_sem_duplicatas) < 2:
            return None
    return vetor_sem_duplicatas[1]

## Quinta questão:
def remover_duplicatas(vetor):
    conjunto_sem_duplicatas = set (vetor)
    vetor_sem_duplicatas = list(conjunto_sem_duplicatas)
    return vetor_sem_duplicatas

## Sexta questão:
def contar_pares_impares(vetor):
    vetor.sort(reverse=True)
    pares = 0 
    impares = 0
    for numero in vetor:
        if numero % 2 == 0:
            pares += 1
    else:
        impares += 1
    return pares, impares

## Sétima questão:
def terceito_maior(vetor):
    vetor_sem_duplicatas = list(set(vetor))
    vetor_sem_duplicatas.sort(reverse=True)
    if len(vetor_sem_duplicatas) <3:
        return None
    return vetor_sem_duplicatas[2]

## Oitava questão:
def mediana(vetor):
    vetor_ordenado = sorted(vetor)
    tamanho = len(vetor_ordenado)
    if tamanho % 2 == 1:
        return vetor_ordenado[tamanho // 2]
    else:
        meio_esquerda = tamanho // 2 - 1
        meio_direita = tamanho // 2
        return (vetor_ordenado[meio_esquerda] + vetor_ordenado[meio_direita]) /2