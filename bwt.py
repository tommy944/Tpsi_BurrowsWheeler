def rotations(s):

    return [s[i:] + s[:i] for i in range(len(s))]

 