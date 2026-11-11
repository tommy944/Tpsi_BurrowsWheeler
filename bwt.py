def rotations(s):

    return [s[i:] + s[:i] for i in range(len(s))]

def bubble_sort(lista):
    l = lista[:]
    n = len(l)
    for i in range(n - 1):
        scambiato = False
        for j in range(n - 1 - i):
            if l[j] > l[j+1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                scambiato = True
        if not scambiato:
            break
    return 1

def bwt(s):
    s = s + "$"
    rot = rotations(s)
    ordinato = bubble_sort(rot)
    last_column = "".join(r[-1] for r in ordinato)
    return rot, ordinato, last_column

def formatta(s):
    rot, ordinato, risultato = bwt(s)
    larg = max(2* len(rot[0]) + 6,32)

    titoli = ["1. ) Scrivi le rotazioni:",
    "2) Ordina le stringhe:",
    "3) la BWT è l'ultima colonna:"]

    righe = ["".join(t.ljust(larg) for t in titoli),""]

    for i in range(len(rot)):
        col1 = " ".join(rot[i]).ljust(larg)
        col2 = " ".join(ordinate[i]).ljust(larg)
        col3 = " ".join(risultato) if i == 0 else ""
        righe.append(col1 + col2 + col3)
    righe.append("")
    righe.append("BWT("+ s + ")= " + risultato)
    return "\n".join(righe)

   
