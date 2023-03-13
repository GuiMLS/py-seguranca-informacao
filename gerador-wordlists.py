import itertools

string = input("String a ser permutada: ")
resultado = itertools.permutations(string, len(string))  # Permuta caracteres wordlist

for i in resultado:
    print(''.join(i))
