
def get_bacon(l):
    ans = ''
    d = {'a':'aaaaa',
    'b':'aaaab',  'c':'aaaba',  'd':'aaabb',  'e':'aabaa',  'f':'aabab',  'g':'aabba',  'h':'aabbb',
    'i':'abaaa',  'j':'abaab',  'k':'ababa',  'l':'ababb',  'm':'abbaa',  'n':'abbab',  'o':'abbba',
    'p':'abbbb',  'q':'baaaa',  'r':'baaab',  's':'baaba',  't':'baabb',  'u':'babaa',  'v':'babab',
    'w':'babba',  'x':'babbb',  'y':'bbaaa',  'z':'bbaab'}
    len_str = len(l)
    for i in range(5, len_str + 5, 5):
        check_str = l[i - 5:i]
        for j in d:
            if d[j] == check_str:
               #print(j, end='')
               ans += j
    return ans
