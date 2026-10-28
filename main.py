def bwt_visual(s):
    s = s + '$'
    n = len(s)
    
    # Generazione delle rotazioni cicliche
    perms = [s[i:] + s[:i] for i in range(n)]
    
    # Ordinamento lessicografico della matrice
    sorted_perms = sorted(perms)
    
    # Estrazione del risultato BWT (colonna Last)
    bwt_result = ''.join([p[-1] for p in sorted_perms])
    
    # Visualizzazione della tabella
    print(f"Stringa di input: '{s[:-1]}' (estesa con '$': '{s}')\n")
    print(f"{'Idx':<5} | {'Matrice Rotazioni Ordinate':<{n+4}} | {'F (First)':<10} | {'L (Last / BWT)'}")
    print("-" * (n + 45))
    
    for i, perm in enumerate(sorted_perms):
        first_col = perm[0]
        last_col = perm[-1]
        print(f"{i:<5} | {perm:<{n+4}} | {first_col:<10} | {last_col}")
        
    print("-" * (n + 45))
    print(f"Risultato BWT: {bwt_result}\n")
    return bwt_result

if __name__ == '__main__':
    stringa = input("Inserisci una stringa: ") or "banana"
    bwt_visual(stringa)