import sys,binascii
filename = sys.argv[1]
with open(filename,'rb') as f:
    count=0
    while True:
        chunk = f.read(16)
        BTH=[]
        BTA=[]
        if chunk:
            print('{:08x}'.format(16*count),end='  ')
            for i in range(0,len(chunk)):
                BTH.append(chunk[i:i+1].hex())
                if(i==7):
                    BTH.append('')
            for b in chunk:
                if 32<=b<=126:
                    BTA.append(chr(b))
                else:
                    BTA.append('.')

            output1=' '.join(BTH)
            output2=''.join(BTA)

            print('{:08x}'.format(16*count),end='  '+output1+((16-len(chunk))*3*' ')+'  |'+output2+'|')
            print()
            count=count +1

        else:
            if(count!=0):
                print('{:08x}'.format(16*count),end='')
            break
