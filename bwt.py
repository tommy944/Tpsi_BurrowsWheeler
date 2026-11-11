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


