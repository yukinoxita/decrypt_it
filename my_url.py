l1 = "%21 %23 %24 %25 %26 %27 %28 %29 %2a %2b %2c %2d %2e %2f %30 %31 %32 %33 %34 %35 %36 %37 %38 %39 %3a %3b %3c %3d %3e %3f %40 %41 %42 %43 %44 %45 %46 %47 %48 %49 %4a %4b %4c %4d %4e %4f %50 %51 %52 %53 %54 %55 %56 %57 %58 %59 %5a %5b %5c %5d %5e %5f %60 %61 %62 %63 %64 %65 %66 %67 %68 %69 %6a %6b %6c %6d %6e %6f %70 %71 %72 %73 %74 %75 %76 %77 %78 %79 %7a %7b %7c %7d %7e"
l2 = "! # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~"
l1 = l1.split()
l2 = l2.split()
d = dict(zip(l1, l2))
d['%20'] = ' '
d['22'] = '"'
def m_url(s):
    ans = ''
    for i in range(0,len(s),3):
        try:
            ans += d[s[i:i+3]]
        except:
            print("你输入的某个或某些url转码不存在，请自行百度查找")
            ans += s[i:i+3]
    return ans
if __name__ == "__main__":
    s = input("请输入你的url转码(仅限百分号加十六进制数字如:%32)")
    s = s.lower()
    k = m_url(s)
    print(k)