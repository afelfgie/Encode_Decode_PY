# -*- CODING : UTF:8/bin -*-

from util.colors import *
from util.misc   import *
from util.banner import *
from util.inputs import *
from util.binary import binary
def bak():
 cc(cont)
 while xoxo:
  cmd=x(choice)
  if not cmd:xoxo
  elif cmd == '1':main()
  elif cmd == '2':quit("")
class base():
 def b64(self,fakyu):
  a=[{1:b64encode,2:b64decode},\
     {1:b32encode,2:b32decode},\
     {1:b16encode,2:b16decode}]
  cc(ende)
  while xoxo:
   try:
    b=int(x(choice))
    if (b > 2): sys.exit()
    print("")
    s=x(edr[b])
    cc(edr[0]+a[fakyu][b](s));bak()
   except ValueError:xoxo
def fn():
  cc(ende)
  while xoxo:
   try:
    a=int(x(choice))
    cc("")
    if (a > 2): sys.exit()
    b=x(edr[a])
    return a,b
   except ValueError:xoxo
class bin():
 def binx(self):
  Color.pl(ende)
  while xoxo:
   try:
    a=int(x(choice))
    cc("")
    if (a > 2): sys.exit()
    b=x(edr[a])
    return a,b
   except ValueError:xoxo
 def rot13(self):
  cc(ende)
  while True:
   try:
    a=int(x(choice))
    if (a > 2): quit("")
    cc("")
    s=x(edr[a])
    cc("{}{}".format(edr[0],s.encode('rot_13')));bak()
   except ValueError:xoxo
 def rev_txt(self):
  cc("")
  cc('{}{}'.format(edr[0],x(rtxt)[::-1]))
  bak()
def csr(n, s_csr):
  s_out = ''
  for x in xrange(len(s_csr)):
   if s_csr[x].isalpha():
    if s_csr[x].islower():s_out+=lowercase[(lowercase.find(s_csr[x])+n)%26]
    else:s_out+=uppercase[(uppercase.find(s_csr[x])+n)%26]
   else:s_out+=s_csr[x]
   return s_out
class decimal():
 def dec(self):
   cc(ende)
   while True:
    try:
     o=int(x(choice))
     print ''
     if (o > 2): break
     s=x(edr[o])
     cc('{}{}'.format(edr[0],''.join([str(ord(c)) for c in s]) if (o==1) else re.sub('1?..', lambda m: chr(int(m.group())),s) if (o==2) else ''));bak()
    except ValueError:xoxo
class xor():
 def withkey(self):
  while xoxo:
   try:
    cc("")
    a=x(xors);b=x(key)
    hasil=''
    for c,k in zip(a,cycle(b)):
     hasil+=chr(ord(c)^ord(k))
    cc('{}{}'.format(edr[0],hasil));bak()
   except ValueError:xoxo
 def bruteforce(self):
  try:
   a=x(xtb)
   for i in xrange(256):cc('ww{} rr=> wwOutput rr===> ww\033[01m{}ww'.format(str(i),''.join([chr(ord(l)^i) for l in a])));print("")
  except ValueError:xoxo
class hash():
 def md4(self):
  x=raw_input(string).new("md4").update().hexdigest()
 def allhash(self,fakyu):
  a=[{0:md5,1:string},\
     {0:sha1,1:string},\
     {0:sha224,1:string},\
     {0:sha256,1:string},\
     {0:sha384,1:string},\
     {0:sha512,1:string}]
  cc(edr[0]+a[fakyu][0](x(a[fakyu][1]).encode('utf')).hexdigest());bak()
 def ihash(self):
  cc(algorithm)
  while xoxo:
   a=x(choice)
   if(a=='1'):self.allhash(0)
   elif(a=='2'):self.allhash(1)
   elif(a=='3'):self.allhash(2)
   elif(a=='4'):self.allhash(3)
   elif(a=='5'):self.allhash(4)
   elif(a=='6'):self.allhash(5)
   elif(a=='7'):self.md4()
   elif(a=='0'):main()
def main():
 global BALIHO
 clear()
 BALIHO.banner()
 BALIHO.author_info()
 cc(menu)
 while xoxo:
  try:
   cmd=x(endech)
   if not cmd:False
   elif(cmd=='1'):base().b64(0);quit("")
   elif(cmd=='2'):base().b64(1);quit("")
   elif(cmd=='3'):base().b64(2);it()
   elif(cmd=='4'):binary(),bak()
   elif(cmd=='5'):o,s=bin().binx();cc('{}{}'.format(edr[0],binascii.hexlify(s) if (o == 1) else binascii.unhexlify(s) if (o == 2) else ''));bak()
   elif(cmd=='6'):decimal().dec()
   elif(cmd=='7'):bin().rot13()
   elif(cmd=='8'):xor().withkey()
   elif(cmd=='9'):xor().bruteforce()
   elif(cmd=='10'):hash().ihash()
   elif(cmd=='11'):bin().rev_txt()
   elif(cmd=='12'):
    try:cc(ende);o=int(x(choice))
    except ValueError:cc("Invalid")
    cc("")
    if o == 1:
     while xoxo:
      try:
       en=x(edr[o])
       n=x(key)
       cc('{}{}'.format(edr[0],csr(n,en)));x();main()
      except TypeError:cc("\nrr[yy-rr]ww TYPE ERROR\n");xoxo
    if o==2:
     en=x(""+r+"["+y+"?"+r+"] "+w+"Caesar to Bruteforce "+r+": "+g+"")
     for i in xrange(26):cc('ww{} rr=> wwOutput rr===> ww\033[01m{}ww'.format(str(i), csr(i, en)));cc("")
   elif(cmd=='0' or cmd=='00'):quit(cc("\n!! wwExiting ...\n"));time.sleep(2)
   else:cc("Invalid")
  except KeyboardInterrupt:main()
  except EOFError:quit(cc("\n\n!! Exiting\n"))
































#-------"""MAIN"""-------#
if __name__ == '__main__':
 try:main()
 except(SystemExit,OSError):pass
##########################


