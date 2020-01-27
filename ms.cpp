#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
char msb[61][26];
char ans[50];
char str[2600];
char tmp[50];
int head,tail;
void init()
{
    strcpy(msb[0],".-");   
    strcpy(msb[1],"-...");    
    strcpy(msb[2],"-.-.");    
    strcpy(msb[3],"-..");    
    strcpy(msb[4],".");    
    strcpy(msb[5],"..-.");    
    strcpy(msb[6],"--.");    
    strcpy(msb[7],"....");    
    strcpy(msb[8],"..");    
    strcpy(msb[9],".---");    
    strcpy(msb[10],"-.-");//k    
    strcpy(msb[11],".-..");    
    strcpy(msb[12],"--");    
    strcpy(msb[13],"-.");    
    strcpy(msb[14],"---");    
    strcpy(msb[15],".--.");    
    strcpy(msb[16],"--.-");    
    strcpy(msb[17],".-.");    
    strcpy(msb[18],"...");    
    strcpy(msb[19],"-");    
    strcpy(msb[20],"..-");    
    strcpy(msb[21],"...-");    
    strcpy(msb[22],".--");    
    strcpy(msb[23],"-..-");    
    strcpy(msb[24],"-.--");    
    strcpy(msb[25],"--..");//z    
    strcpy(msb[26],".----");    
    strcpy(msb[27],"..---");    
    strcpy(msb[28],"...--");    
    strcpy(msb[29],"....-");    
    strcpy(msb[30],".....");    //5
    strcpy(msb[31],"-....");  //6  
    strcpy(msb[32],"--...");    
    strcpy(msb[33],"---..");    
    strcpy(msb[34],"----.");    
    strcpy(msb[35],"-----");//0    
    strcpy(msb[36],"..--..");// ?    
    strcpy(msb[37],"-..-.");//  /    
    strcpy(msb[38],".-.-.-");// .    
    strcpy(msb[39],".--.-.");// @    
    strcpy(msb[40],"-.-.--");// ! 
    strcpy(msb[41],"-....-");// -    
    strcpy(msb[42],"----.--");//{}
    strcpy(msb[43],"-----.-");// }
    strcpy(msb[44],"..--.-");// _
   // strcpy(msb[42],"");  
}
void make()
{
    int i;
    for(i=0;i<=25;i++)ans[i]='A'+i;
    for(i=0;i<=9;i++)ans[i+26]='1'+i;
    ans[35]='0';
    ans[36]='?';
    ans[37]='/';
    ans[38]='.';
    ans[39]='@';
    ans[40]='!';
    ans[41]='-';
    ans[42]='{';
    ans[43]='}';
    ans[44]='_';
}
void sagasu()
{
    memset(tmp,0,sizeof(tmp));
    int i;
    for(i=head;i<=tail;i++)
        tmp[strlen(tmp)]=str[i];
    
    //cout<<tmp;
    for(i=0;i<=60;i++)
        if(!strcmp(tmp,msb[i])){cout<<ans[i];return;}
}
void test()
{
    int  i;
    for(i=0;i<=60;i++)cout<<ans[i]<<" = "<<msb[i]<<endl;
}
int main()
{
    init();
    make();
   // test();
    cin.getline(str,10000);
    int i;
    for(i=0;i<strlen(str);i++)
    {
        if(str[i]!='.' && str[i]!='-')
        {
            tail=i-1;
            sagasu();
            head=i+1;
        }   
    }
    return 0;
}
/*---------------------------------------
正体。。。。。
---------------------------------------*/