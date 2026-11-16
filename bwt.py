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

def BWT(testo):
    testo_modificato = testo + "$"
    lunghezza = len(testo_modificato)
    rotazioni = []

    for i in range(lunghezza):
        rotazione = testo_modificato[i:] + testo_modificato[:i]
        rotazioni.append(rotazione)

    print("rotazione completa dell'algortimo: ", rotazioni)

    rotazioni = bubbleSort(rotazioni)
    risultato = "".join(riga[-1] for riga in rotazioni)

    print("Stringa con implementazione dell'algortimo: ", risultato)
    
    return rotazioni 





           
