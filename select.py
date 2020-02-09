import time
import string
import os
import html
from my_base64 import *
import base64
from bacon import *
from qwe import *
from caesar import *
from zhalan import get_zhalan
from m_ascii import *
from rot import get_rot
from convert import *
from my_url import *
from vig import *


def head_show():
    print()
    print("-------------------------------------------------")
    print("|   ここは僕のプログラムだよ、ようこそ！！！    |")
    print("|   my program da you welcome!!!!               |")
    print("-------------------------------------------------")

def handle_num():
    x = input("password please input:")
    if x == "0":
        return "exit"
    elif x.isdigit():
        return x
    else:
        print('your input is wrong please re-input!!!')
        os.system('cls')
    pass
def select():
    while(1):
        print("PART ONE : 解密　パスワード\n")
        #print("11 : morse\n12 : base64 \n13 : url\n14 : bacon\n15 : Railfence\n16 : QWE password\n17 : N--->ascii\n18 : caesar\n19 : rot\n")
        print('please input "1" to enter password moudle')
        print("-------------------------------------------------\n")
        print("PART TWO : 小功能　色々なファンクション\n")
        #print("21 : kill the ' '\n22 : upper and lowercase\n23 : reverse  123 --- >321\n")
        print('please input "2" to enter password moudle')
        print("-------------------------------------------------\n")
        print("PART THREE : 加密\n")
        print('please input "3" to enter password moudle')
        print("-------------------------------------------------\n")
        print("0 : exit\n")
        n = input("数字を入力してください / please input the number : ")
        n = int(n)
        if n == 1:
            os.system('cls')
            print("PART ONE : 解密　パスワード\n")
            print("11 : morse\n12 : base64 \n13 : url\n14 : bacon\n15 : Railfence\n16 : QWE password\n17 : N--->ascii\n18 : caesar\n19 : rot\n110 : URL")
            print("111 : 维吉尼亚")
            print('0 : return to look other options')
            while(1):
                x = handle_num()
                if x == "exit":
                    break
                return x
                '''    
                x = input("password please input:")
                if x == "0":
                    break
                elif x.isdigit() and x[0] == '1':
                    return x
                else:
                    print('your input is wrong please re-input!!!')
                    os.system('cls')
                '''
        if n == 2:
            os.system('cls')
            print("PART TWO : 小功能　色々なファンクション\n")
            print(
                "21 : kill the ' '\n22 : upper and lowercase\n23 : reverse  123 --- >321\n24 : convert the string")
            print('0 : return to look other options')
            while(1):
                x = handle_num()
                if x == "exit":
                    break
                return x
        if n == 3:
            os.system('cls')
            print("PART THREE : 加密\n")
            print("31 : 字符串转16进制\n32 : 字符串转base组编码")
            print('0 : return to look other options')
            while(1):
                x = handle_num()
                if x == "exit":
                    break
                return x
        if n == 0:
            return 0
        os.system('cls')
        head_show()


def handle(n):
    if n == 11:
        print("please input the string(last char is space): ")
        try:
            os.system("ms.exe")
        except:
            print("ERROR string!!!")
    if n == 12:
        s = input('please input the string :')
        key = int(input('please input base what? 64 ? 32? 16?'))
        #print ('base decode is :',get_base(s,key))
        try:
            ans = get_base(s, key)
            return ('base decode is :' + ans)
        except:
            return ('ERROR stirng')
    if n == 13:
        s = input('please input the string :')
        try:
            ans = html.unescape(s)
            return ('html decode is :' + ans)
        except:
            return ('ERROR string')
    if n == 14:
        l = input('please input the string :')
        l = l.lower()
        try:
            ans = get_bacon(l)
            return ('bacon decode is :' + ans)
        except:
            return ('ERROR string')
    if n == 15:
        key = input('reilfence please input 0,W railfence input 1 :')
        #w zhalan 
        key = int(key)
        if key == 0:
            s = input('please input the string :')
            try:
                get_zhalan(s)
                return ('please look at the top')
            except:
                return ("ERROR string")
        else :
            print("先输入字符串，再按下一个空格，然后输入你的密钥(例如5)，再按空格即可得出答案")
            try:
                os.system('wzhalan.exe')
            except:
                return ("ERROR string")
    if n == 16:
        li = input('please input the string :')
        li = li.upper()
        try:
            ans = get_qwe(li)
            return ('qwe decode is :' + ans)
        except:
            return ("ERROR string")
    if n == 17:
        s = input('please input the string :')
        g = input(' 你的分隔符是啥 ')
        try:
            ans = get_ascii(s,g)
            return ('ascii decode is :' + ans)
        except:
            return ("ERROR string")

    if n == 18:
        s = input('please input the string :')
        try:
            get_caesar(s)
            return ('please look at the top')
        except:
            return ("ERROR string")
    if n == 19:
        s = input('please input the string :')
        key = int(input('rot13? 5? 18? 47?'))
        try:
            ans = get_rot(s,key)
            return ('rot decode is :' + ans)
        except:
            return ("ERROR string")
    if n == 110:
        s = input("请输入你的url转码(仅限百分号加十六进制数字如:%32)")
        s = s.lower()
        try:
            ans = m_url(s)
            return ('url decode is :' + ans)
        except:
            return ("ERROR string")
    if n == 111:
        s = int(input("请选择你要解决的类型\n1:求密钥\n2:解密\n3:加密\n"))
        if s == 1:
            while True:
                mingwen = input("请输入明文 : ")
                miwen = input("请输入密文 : ")
                if len(mingwen) == len(miwen):
                    ans = find_key(mingwen,miwen)
                    return("维吉尼亚密钥为 :" + ans)
                else:
                    print('输入的明文和密文长度不一致,请重新输入')
                    os.system('cls')
        if s == 2:
            miwen = input("请输入密文 : ")
            key = input("请输入密钥 : ")
            ans = find_mingwen(miwen,key)
            return ("维吉尼亚明文为 :" + ans)
        if s == 3:
            mingwen = input("请输入明文 : ")
            key = input("请输入密钥 : ")
            ans = find_mingwen(mingwen,key)
            return ("维吉尼亚密文为 :" + ans)

    if n == 21:
        s = input('please input the string :')
        s = s.split(' ')
        ans = ''
        for i in s:
            ans += i
        retrun ('kill decode is :' + ans)
    if n == 22:
        s = input('please input the string :')
        key = int(input('rule : upper ---> 1    lower--->2  please input the number:'))
        if key == 1:
            ans = s.upper()
        else:
            ans = s.lower()
        return ('Aa decode is :' + ans)
    if n == 23:
        s = input('please input the string :')
        ans = s[::-1]
        return ('reverse decode is :' + ans)
    if n == 24:
        try:
            return('kenkan decide is :' + kenkan())
        except:
            return ("ERROR string")
    if n == 31:
        s = input('please input the string :')
        ans = ''
        for i in s:
            ans += str(hex(ord(i)))[2:]
        ans = '0x'+ans
        return ("字符串转16进制得 :"+ans)
    if n == 32:
        s = input('please input the string :')
        while 1:
            try:    
                num = int(input('64?32?16?:'))
                break
            except:
                print("输入有误")
                os.system('cls')
        if num == 64:
            ans = base64.b64encode(s.encode('utf-8')).decode('utf-8')
        elif num == 32:
            ans = base64.b32encode(s.encode('utf-8')).decode('utf-8')
        elif num == 16:
            ans = base64.b16encode(s.encode('utf-8')).decode('utf-8')
        else:
            ans = "ERROR_Stirng"
        return ("base加密得 :"+ans)




def main(f):
    n = 718
    ans = 'first is NONE...'
    while(n != 0):
        head_show()
        print('-----------------------------------------------')
        print(ans)
        print('Notice :最初は何もないよ')
        print('-----------------------------------------------')
        print()
        n = select()
        os.system("cls")
        n = int(n)
        if n == 0:
            print('thanks for using.closed by your self or autoclose before 5s ')
            break
        ans = handle(n)
        f.write(ans+'\n')

    print("Author    : AHGAXY_MZH")
    print("Time      : 2019.9")
    print("Version   : 1.2.2")

if __name__ == '__main__':
    f = open("log.txt","w",encoding="utf-8")
    main(f)
    f.close()
    time.sleep(5)
