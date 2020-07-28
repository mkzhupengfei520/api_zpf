# -*- coding:UTF-8 -*-
#f = r'C:\\Users\\HP\\Desktop\\zhanghao.txt'

#with open(r'f') as f:
 #   s = f.read()
  #  print (s)
f=open("r'C:\\Users\\HP\\Desktop\\zhanghao.txt'","r",encoding='utf-8')
f.readline()
for line in f:
    print (line)