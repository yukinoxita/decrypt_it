# 简介：在做题过程中解密码，变换字串.
作者： YUKKI  
时间：2019.9.7 (version 1.0.0)  
说明：部署在linux环境下

----------------------------------------------------------------------------
//使用说明  
> python3 select.py  
### 暂时没有写自动编译脚本，clone后请自行执行以下命令:
> g++ -g -o ms ms.cpp  
> g++ -g -o wzhalan wzhalan.cpp

----------------------------------------------------------------------------
//版本更新说明会放在这里  

  时间  	  版本		说明  
2019.9.7	v 1.0.0		20:15为止一共收录了10种功能  
2019.9.12   	v 1.0.1		修复了caesar模块的数字也变换的bug，并添加了rot族的模块  
2019.9.13	v 1.0.2		修复了caesar模块的特殊字符也变换的bug，并添加了普通的栅栏密码  
						备注：功能太少，且并未经过大量测试，可能还会有bug（大概会体现在特殊字符上）  
2019.9.13	v 1.0.2		文件丢失！！！  
2019.9.19	v 1.0.2		修复rot模块的小bug，并准备再次进行优化(重做)	下一版本：1.1.0  
2019.9.21	v 1.1.0		基本重做完毕，相比较1.0.x版本在功能上进行了细化，密码与其他功能做了区分  
2019.9.2x	v 1.1.1		优化调用速度同时修正了选择界面的小错误  
2019.9.23	V 1.1.1		发现了一些错误，正在修改，可能还要重做  
2019.9.28	v 1.1.1		由于主程序是由c写的，不方便，故国庆重做  
2019.9.30	v 1.1.1		选择程序冗余，重做  
2019.10.2	v 1.2.0		修复了因选项太多不够可观的情况,主程序完全由c移植到了python上  
2019.12.5	v 1.2.1		增加了URL转码模块  
2020.1.27	v 1.2.2		增加了维吉尼亚密码,可通过明文密文求密钥，也可求密文  
2020.2.1	v 1.2.3		修复rot模块的bug  

2020.2.9	v 1.2.4		更新了convert模块，添加了log日志功能，创造并添加了PART 3，简化了代码    
---------------------------------------------------------------------------
# 使用说明  
双击文件或者在文件夹下用命令行:
```shell  
python3 select.py  
```
出现一个选择界面，输入相对应的数字进入到你需要的模块  
1:CTF部分密码学解密  
2:一些小功能  
3:编写payload时可能用到的字符变换~~//TODO~~  

