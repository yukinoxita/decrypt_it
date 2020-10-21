import time
import subprocess
import string
import os
import html
import json
import func.my_base64 
import base64
from func.bacon import *
from func.qwe import *
from func.caesar import *
from func.zhalan import get_zhalan
from func.m_ascii import *
from func.rot import get_rot
from func.convert import *
from func.my_url import *
from func.vig import *
from func.ms import *

class handle:
    status = "" # 记录初始化后得到的字符串
    def __init__(self,n):
        if n == 1:
            self.status = 'first is NONE...'
        elif n == 11:
            s = input("please input the string(last char is space): ")
            try:
                ans = get_ms(s)
                self.status = 'morse decode is : ' + ans
            except:
                self.status = "ERROR string"
        elif n == 12:
            s = input('please input the string :')
            key = int(input('please input base what? 64 ? 32? 16?'))
            try:
                ans = get_base(s, key)
                self.status = 'base decode is :' + ans
            except:
                self.status = 'ERROR string'
        elif n == 13:
            s = input('please input the string :')
            try:
                ans = html.unescape(s)
                self.status = 'html decode is :' + ans
            except:
                self.status = 'ERROR string'
        elif n == 14:
            l = input('please input the string :')
            l = l.lower()
            try:
                ans = get_bacon(l)
                self.status = 'bacon decode is :' + ans
            except:
                self.status = 'ERROR string'
        elif n == 15:
            key = input('reilfence please input 0,W railfence input 1 :')
            #w zhalan 
            key = int(key)
            if key == 0:
                s = input('please input the string :')
                try:
                    ans = get_zhalan(s)
                    self.status = 'reilfence decode is :\n' + ans
                except:
                    self.status = 'ERROR string'
            else :
                print("先输入字符串，再按下一个空格，然后输入你的密钥(例如5)，再按空格即可得出答案")
                try:
                    os.system('./wzhalan.exe')
                except:
                    self.status = 'ERROR string'
        elif n == 16:
            li = input('please input the string :')
            li = li.upper()
            try:
                ans = get_qwe(li)
                self.status = 'qwe decode is :' + ans
            except:
                self.status = 'ERROR string'
        elif n == 17:
            s = input('please input the string :')
            g = input(' 你的分隔符是啥 ')
            try:
                ans = get_ascii(s,g)
                self.status = 'ascii decode is :' + ans
            except:
                self.status = 'ERROR string'

        elif n == 18:
            s = input('please input the string :')
            try:
                ans = get_caesar(s)
                self.status = 'caesar decide is :' + ans
            except:
                self.status = 'ERROR string'
        elif n == 19:
            s = input('please input the string :')
            key = int(input('rot13? 5? 18? 47?'))
            try:
                ans = get_rot(s,key)
                self.status = 'rot decode is :' + ans
            except:
                self.status = 'ERROR string'
        elif n == 110:
            s = input("请输入你的url转码(仅限百分号加十六进制数字如:%32)")
            s = s.lower()
            try:
                ans = m_url(s)
                self.status = 'url decode is :' + ans
            except:
                self.status = 'ERROR string'
        elif n == 111:
            s = int(input("请选择你要解决的类型\n1:求密钥\n2:解密\n3:加密\n"))
            if s == 1:
                while True:
                    mingwen = input("请输入明文 : ")
                    miwen = input("请输入密文 : ")
                    if len(mingwen) == len(miwen):
                        ans = find_key(mingwen,miwen)
                        self.status = "维吉尼亚密钥为 :" + ans
                    else:
                        print('输入的明文和密文长度不一致,请重新输入')
                        os.system('clear')
            if s == 2:
                miwen = input("请输入密文 : ")
                key = input("请输入密钥 : ")
                ans = find_mingwen(miwen,key)
                self.status = "维吉尼亚明文为 :" + ans
            if s == 3:
                mingwen = input("请输入明文 : ")
                key = input("请输入密钥 : ")
                ans = find_mingwen(mingwen,key)
                self.status = "维吉尼亚密文为 :" + ans

        elif n == 21:
            s = input('please input the string :')
            s = s.split(' ')
            ans = ''.join(s)
            self.status = 'kill decode is :' + ans
        elif n == 22:
            s = input('please input the string :')
            key = int(input('rule : upper ---> 1    lower--->2  please input the number:'))
            if key == 1:
                ans = s.upper()
            else:
                ans = s.lower()
            self.status = 'Aa decode is :' + ans
        elif n == 23:
            s = input('please input the string :')
            ans = s[::-1]
            self.status = 'reverse decode is :' + ans
        elif n == 24:
            try:
                self.status = 'kenkan decide is :' + kenkan()
            except:
                self.status = 'ERROR string'
        elif n == 31:
            s = input('please input the string :')
            ans = ''
            for i in s:
                ans += str(hex(ord(i)))[2:]
            ans = '0x'+ans
            self.status = "字符串转16进制得 :"+ans
        elif n == 32:
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
            self.status = "base加密得 :"+ans

        pass
    pass
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
        print("PART ONE : %s"%list(data['Function'][0].keys())[0])
        print('please input "1" to enter password moudle')
        print("-------------------------------------------------\n")
        print("PART TWO : %s"%list(data['Function'][1].keys())[0])
        print('please input "2" to enter password moudle')
        print("-------------------------------------------------\n")
        print("PART THREE : %s"%list(data['Function'][2].keys())[0])
        print('please input "3" to enter password moudle')
        print("-------------------------------------------------\n")
        print("0 : exit\n")
        n = input("数字を入力してください / please input the number : ")
        n = int(n)
        if n == 1:
            os.system('clear')
            print("PART ONE : 解密　パスワード\n")
            name =  list(data['Function'][0].keys())[0]
            for i in data['Function'][0][name]:
                print("%s : %s"%(data['Convert_Decrypt'][0][i],i))
            print('0 : return to look other options')
            while(1):
                x = handle_num()
                if x == "exit":
                    break
                return x
        if n == 2:
            os.system('clear')
            print("PART TWO : 小功能　色々なファンクション\n")
            name =  list(data['Function'][2].keys())[0]
            print(name)
            for i in data['Function'][2][name]:
                print("%s : %s"%(data['Convert_Function'][0][i],i))
            print('0 : return to look other options')
            while(1):
                x = handle_num()
                if x == "exit":
                    break
                return x
        if n == 3:
            os.system('clear')
            print("PART THREE : 加密\n")
            name =  list(data['Function'][1].keys())[0]
            print(name)
            for i in data['Function'][1][name]:
                print("%s : %s"%(data['Convert_Encrypt'][0][i],i))
            print('0 : return to look other options')
            while(1):
                x = handle_num()
                if x == "exit":
                    break
                return x
        if n == 0:
            return 0
        os.system('clear')
        head_show()

def main(f):
    global data
    H = handle(1)
    with open("config.json") as fo:
        data = json.load(fo)
    n = 718
    ans = 'first is NONE...'
    ans = H.status
    while(n != 0):
        head_show()
        print('-----------------------------------------------')
        print(ans)
        print('Notice :最初は何もないよ')
        print('-----------------------------------------------')
        print()
        n = select()
        os.system("clear")
        n = int(n)
        if n == 0:
            os.system('clear')
            print('Thanks for using.Closed by your self or autoclose before 5s ')
            break
        H = handle(n)
        ans = H.status
        #f.write(ans+'\n')

    print("Author    : %s"%data["Author"])
    print("Version   : %s"%data["Version"])

if __name__ == '__main__':
    f = open("log.txt","w",encoding="utf-8")
    main(f)
    f.close()
    #time.sleep(5)
