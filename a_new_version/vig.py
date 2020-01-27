def find_key(mingwen,miwen):
    mingwen = mingwen.lower()
    miwen = miwen.lower()
    key = ''
    for i in range(len(mingwen)):
        if mingwen[i].isalpha():
            a = ord(miwen[i]) - ord(mingwen[i]) + 1
            if a < 0:
                a += 26
            key += chr(96+a)
    return key

def find_mingwen(miwen,key):
    miwen = miwen.lower()
    key = key.lower()
    mingwen = ''
    for i in range(len(miwen)):
        if miwen[i].isalpha():
            a = ord(miwen[i]) - ord(key[i%len(key)]) + 1
            if a < 0:
                a += 26
            mingwen += chr(96+a)
        else:
            mingwen += miwen[i]
    return mingwen

def find_miwen(mingwen, key):
    mingwen = mingwen.lower()
    key = key.lower()
    miwen = ''
    for i in range(len(mingwen)):
        if mingwen[i].isalpha():
            a = ord(mingwen[i]) + ord(key[i%len(key)]) - 1 - 96*2
            if a > 26:
                a -= 26
            miwen += chr(96+a)
        else:
            miwen += mingwen[i]
    return miwen
