def get_ascii(s,g):
    ans = ''
    bit = int(input('please input N : '))
    li = s.split(g)
    if g == "null":
        for i in range(0,len(s),2):
            ans += chr(int(s[i:i+2],bit))
        return ans
    for i in li:
        #print((chr(int(i, bit))), end='')
        ans += chr(int(i, bit))
    return ans

if __name__ == '__main__':
    s = input('str:')
    g = input('split:')
    ans = get_ascii(s,g)
    print(ans)
