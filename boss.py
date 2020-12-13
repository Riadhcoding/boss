import os,sys,time,datetime
from os import system,remove
import marshal
import compileall
system('git pull')
system('apt-get install nodejs -y')
system('npm install -g bash-obfuscate')
system('clear')
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.02)
def main():
    print('[1] Py to Pyc')
    print('[2] Marshal')
    print('[3] encrypt Bash shell')
main()
choose = input('[?] Choose: ')
if choose == 1:
    tool_list = str(input('File > '))
    compileall.compile_file(tool_list)
    print('success')
    print('Save to /sdcard/__pycache__')
elif choose ==2:
    file = input('File >')
    openfile = open(file, 'r').read()
    com = compile(openfile, ' ', 'exec')
    encrypt = marshal.dumps(com)
    enc = open('enc_' + str(file), 'w')
    enc.write('import marshal\n')
    enc.write('exec(marshal.loads(' + repr(encrypt) + '))')
    print('success encrypt | file save as enc_' + str(file))
elif choose ==3:
    file3 = input('File >')
    com3 = 'bash-obfuscate '+file3+ ' -o enc.sh'
    system(com3)