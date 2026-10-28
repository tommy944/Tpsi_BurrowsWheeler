def bwt(s):
    s= s + '$'
    perms = [s[i:] + s[:i] for i in range(len(s))]
    sorted_perms = sorted(perms)
    bwt = ''.join([p[-1] for p in sorted_perms])
    return bwt

def inverse_bwt(bwt_string):
    counts = {}
    for char in bwt_string:
        counts[char] = counts.get(char,0) + 1
    sorted_chars = sorted(counts.keys())

    first_column = []
    for char in sorted_chars:
        count = counts[char]
        first_column.extend([char] * count)
    index = 0 
    original_string = ""
    for _ in bwt_string:
        char = bwt_string[index]
        original_string = char + original_string
        index = first_column.index(char)
        first_column[index] = None

    return original_string[1:]

if __name__ == '__main__':
    s = input("Write a string:")
    bw = bwt(s)
    print("BWT Of ", s, "is", bw)

    ibw = inverse_bwt(bw)
    print("Inverse BWT of ", bw, "is", ibw)



