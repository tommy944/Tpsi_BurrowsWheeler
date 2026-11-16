def bubbleSort(dati):
    lista = dati.copy()
    n = len(lista)

    for i in range(n):
        scambiato = False
        for j in range(0, n -i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j + 1], lista[j]
                scambiato = True
        if not scambiato:
            break
    return lista

        
