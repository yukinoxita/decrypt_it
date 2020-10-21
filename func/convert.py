import re


def kenkan():
    s = input("请输入你想转换的字符串:")
    while True:
        convert = input("请输入你想转换和像转换成的字符(两个字符之间加个空格),\n如果想转换成空格请输入space,结束转换请输入exit:")
        if convert == "exit":
            break
        convert = convert.split(' ')
        if len(convert) < 2:
            print("输入有误，请重试")
            continue
        if convert[1] == 'space':
            convert[1] = ' '
        s = s.replace(convert[0],convert[1])
        print("目前转化为了:",s)
    return s
    
if __name__ == "__main__":
    kenkan()