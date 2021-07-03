import codecs

bfile = codecs.open("file.txt",'r',"utf-8")
ss = bfile.read()

# print (ss)

bfile.close()
s = codecs.open("file.txt","w","utf-16")
s.write(ss)
s.close()
