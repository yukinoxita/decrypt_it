import string

def rot13(s):
    ans = ''
    for i in s:
        if not i.isalpha():
            ans += i
        else:
            check = ord(i)
            check += 13
            if i.islower() and check > ord('z'):
                check -= 26
            if i.isupper() and check > ord('Z'):
                check -= 26
            ans += chr(check)
    return ans


def rot5(s):
    ans = ''
    for i in s:
        if not i.isdigit():
            ans += i
            continue
        check = ord(i)
        check += 5
        if check > ord('9'):
            check -= 10
        ans += chr(check)
    return ans


def rot18(s):
    return rot5(rot13(s))


def rot47(s):
    ans = ''
    for i in s:
        check = ord(i)
        check -= 47
        if check < 33:
            check += 94
        ans += chr(check)

    return ans


def get_rot(s,key):
    key = int(key)
    if key == 5:
        #print('rot5 = ', rot5(s))
        return rot5(s)
    if key == 18:
        #print('rot18 = ', rot18(s))
        return rot18(s)
    if key == 47:
        #print('rot47 = ', rot47(s))
        return rot47(s)
    if key == 13:
        #print('rot13 = ', rot13(s))
        return rot13(s)

if __name__ == '__main__':
    s = input('字符串:')
    key = input('rot几?')
    print(get_rot(s,key))