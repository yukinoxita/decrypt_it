def get_ascii(s,g):
    ans = ''
    bit = int(input('please input N : '))
    li = s.split(g)
    for i in li:
        #print((chr(int(i, bit))), end='')
        ans += chr(int(i, bit))
    return ans
