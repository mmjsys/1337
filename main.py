import sys
dict_of_leet = {
    'A': '4',
    'B': '13',
    'C': '<',
    'D': '|)',
    'E': '3',
    'F': '|=',
    'G': '6',
    'H': '|-|',
    'I': '1',
    'J': ']',
    'K': '|{',
    'L': '|_',
    'M': '|V|',
    'N': '|\|',
    'O': '0',
    'P': '|*',
    'Q': '(,)',
    'R': '|2',
    'S': '$',
    'T': '7',
    'U': '|_|',
    'V': '\/',
    'W': '\/\/',
    'X': '}{',
    'Y': "'/",
    'Z': '2',
    '.': '.',
}
list_of = sys.argv
del list_of[0]
for w in list_of:
    for c in w:
        print(dict_of_leet[c.upper()] , end='')
    print(" ",end='')
print('')