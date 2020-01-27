#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
char str[10000];
char ans[1000];
int line=0;
int key;
int len;
int sit;
int ssit;
int check()
{
    if(line==1 ||line==key)return sit+(key-1)*2;
    else
    {
        if(ssit%2==1)return sit+(key-line)*2;
        else return sit+2*(line-1);
    }
}
int main()
{
    int i;
    cin>>str;
    scanf("%d",&key);
    len=strlen(str);
    for(i=len;i>0;i--)str[i]=str[i-1];
    line=1;
    sit=1;
    ssit=1;

    for(i=1;i<=len;i++)
    {
        ans[sit]=str[i];
        sit=check();
        ssit++;
        if(sit>len)
        {
            line++;
            sit=line;
            ssit=1;
        }
    }
    for(i=1;i<=len;i++)printf("%c",ans[i]);
    return 0;
}