#QWE 码表
import string
def get_qwe(li):
    ans = ''
    a=string.ascii_uppercase
    l1=list(a)
    s="QWERTYUIOPASDFGHJKLZXCVBNM"
    l2=list(s)
    d=dict(zip(l2,l1))

    li=list(li)
    for i in li:
        #print(d[i],end='')
        ans += d[i]
    return ans