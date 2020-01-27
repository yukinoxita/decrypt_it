import  os
import math
def find_num(num):
    li = []
    fnum = int(math.sqrt(num))
    for i in range(2,fnum+1):
        if num % i == 0:
            li.append(i)
            li.append(int(num/i))

    return li
def get_zhalan(s):
    li = find_num(len(s))
    li.sort()
    print('0 row: ', s)
    for i in range(len(li)):
        ans = ''
        start = 0
        while len(ans) < len(s):
            for k in range(start, len(s), int(li[i])):
                ans += s[k]

            start += 1
            if start == int(li[i]):
                break

        print(li[i], 'row: ', ans)

if __name__ == '__main__':
    s = input()
    get_zhalan(s)
