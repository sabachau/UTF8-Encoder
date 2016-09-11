from sys import argv
import struct
import string


def main():

    script,path=argv
    #path = 'files1/japanese_in.txt'
    input_file=open(path, 'rb')
    output_file=open('utf8encoder_out.txt', 'wb')

    try:
        byte = input_file.read()
        hexStr=""
       
        for x in range(0,len(byte)):
            hexStr=hexStr+(hex(ord(byte[x]))[2:].zfill(2))
        finalhexchar=''
       
        while(hexStr!=""):
            concat="0x"+hexStr[:4]
            if(0x0000<=int(concat,16)<=0x007f):
                storebin1=bin(int(concat,16))[2:].zfill(8)
                finalhexchar+= hex(int(storebin1,2))[2:]
            elif(0x0080<=int(concat,16)<=0x07ff):
                storebin=bin(int(concat,16))[2:].zfill(11)
                prefix='110'
                cont_char='10'
                finalhexchar+= hex(int(prefix+storebin[:5]+cont_char+storebin[5:],2))[2:]
            elif(0x0800<=int(concat,16)<=0xffff):
                storebin3=bin(int(concat,16))[2:].zfill(16)
                prefix='1110'
                cont='10'
                finalhexchar+= hex(int(prefix+storebin3[:4]+cont+storebin3[4:10]+cont+storebin3[10:16],2))[2:]
            hexStr=hexStr[4:]

        while( finalhexchar!=''):
            taketwo='0x'+finalhexchar[:2]
            finalhexchar=finalhexchar[2:]
            output_file.write(chr(int(taketwo, 16)))
    
    finally:
        input_file.close()


if __name__=='__main__':
    main()
