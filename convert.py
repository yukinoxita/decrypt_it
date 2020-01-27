def kenkan():
    print("如果你想把01转换成.-那就先输入 0 1 ，再输入 . - 。跟着我的提示走")
    li = input("请输入你想转换的字符(仅限两个且中间打个空格):")
    while len(li) != 3:
        li = input("输入错误，重新输入")
    li = li.split()
    l = input("请输入你想转换成的字符(仅限两个且中间打个空格):")
    while len(l) != 3:
        l = input("输入错误，重新输入")
    l = l.split()

    s = input("请输入你想转换的字符串:")
    ans = ''
    for i in s:
        if i == li[0]:
            ans += l[0]
        elif i == li[1]:
            ans += l[1]
        else :
            ans += ' '
    return ans
if __name__ == "__main__":
    kenkan()
    