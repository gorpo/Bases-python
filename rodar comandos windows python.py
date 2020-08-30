import subprocess
import os

text = "dir"
proc = subprocess.Popen(text, shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = proc.communicate()
f =  open('foo.txt', 'a')
f.write(str(stdout.decode('Windows-1252')))
f.close()
r = open('foo.txt','r').readlines()
todas = []
separador = ' '
for line in r:
    line1 = line.replace('   ','')
    if line1 == '\n':
        pass
    else:
        todas.append(line1)
os.remove('foo.txt')
print(todas)