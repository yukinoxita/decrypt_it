import os
def get_ms(s):
    with open("MorseTable") as fo:
        fo = fo.read().split('\n')

    dic = dict([])
    fo.pop()
    for i in fo:
        li = i.split(' ')
        dic[li[0]] = li[1]

    ans = ''
    s = s.split()
    for i in s:
        ans += dic[i]
    return ans

if __name__ == '__main__':
    s = input('两个莫斯之间空格 : ')
    ans = get_ms(s)
    print(ans)

