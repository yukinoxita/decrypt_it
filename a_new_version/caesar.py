import string
def get_caesar(s):
    for i in range(1, 26):
        ans = ''
        for j in s:
            if not j.isalpha():
                ans += j
            else:
                check = ord(j)
                check += i
                if j.isupper():
                    if check > ord('Z'):
                        check -= 26
                if j.islower():
                    if check > ord('z'):
                        check -= 26
                ans += chr(check)
        print(ans)