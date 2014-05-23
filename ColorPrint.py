"""
格式：\033[显示方式;前景色;背景色m
 
说明：
前景色            背景色           颜色
---------------------------------------
30                40              黑色
31                41              红色
32                42              绿色
33                43              黃色
34                44              蓝色
35                45              紫红色
36                46              青蓝色
37                47              白色
显示方式           意义
-------------------------
0                终端默认设置
1                高亮显示
4                使用下划线
5                闪烁
7                反白显示
8                不可见
 
例子：
\033[1;31;40m    <!--1-高亮显示 31-前景色红色  40-背景色黑色-->
\033[0m          <!--采用终端默认设置，即取消颜色设置-->
"""
def B_Red(*s):
   if len(s)>1:
      print '\033[7;31;40m',
      for i in s:
         print i,
      print '\033[0m'
   else:
      print '\033[7;31;40m%s\033[0m'%(s)
def F_Red(*s):
   if len(s)>1:
      print '\033[1;31;40m',
      for i in s:
         print i,
      print '\033[0m'
   else:
      print '\033[1;31;40m%s\033[0m'%(s)
def B_Green(*s):
   if len(s)>1:
      print '\033[7;32;40m',
      for i in s:
         print i,
      print '\033[0m'
   else:
      print '\033[7;32;40m%s\033[0m'%(s)
def F_Green(*s):
   if len(s)>1:
      print '\033[1;32;40m',
      for i in s:
         print i,
      print '\033[0m'
   else:
      print '\033[1;32;40m%s\033[0m'%(s)
def B_Yellow(*s):
   if len(s)>1:
      print '\033[7;33;40m',
      for i in s:
         print i,
      print '\033[0m'
   else:
      print '\033[7;33;40m%s\033[0m'%(s)
def F_Yellow(*s):
   if len(s)>1:
      print '\033[1;33;40m',
      for i in s:
         print i,
      print '\033[0m'
   else:
      print '\033[1;33;40m%s\033[0m'%(s)
def B_Purple(*s):
   if len(s)>1:
      print '\033[7;35;40m',
      for i in s:
         print i,
      print '\033[0m'
   else:
      print '\033[7;35;40m%s\033[0m'%(s)
def F_Purple(*s):
   if len(s)>1:
      print '\033[1;35;40m',
      for i in s:
         print i,
      print '\033[0m'
   else:
      print '\033[1;35;40m%s\033[0m'%(s)
def B_Blue(*s):
   if len(s)>1:
      print '\033[7;34;40m',
      for i in s:
         print i,
      print '\033[0m'
   else:
      print '\033[7;34;40m%s\033[0m'%(s)
def F_Blue(*s):
   if len(s)>1:
      print '\033[1;34;40m',
      for i in s:
         print i,
      print '\033[0m'
   else:
      print '\033[1;34;40m%s\033[0m'%(s)
def B_Cyanine(*s):
   if len(s)>1:
      print '\033[7;36;40m',
      for i in s:
         print i,
      print '\033[0m'
   else:
      print '\033[7;36;40m%s\033[0m'%(s)
def F_Cyanine(*s):
   if len(s)>1:
      print '\033[1;36;40m',
      for i in s:
         print i,
      print '\033[0m'
   else:
      print '\033[1;36;40m%s\033[0m'%(s)
