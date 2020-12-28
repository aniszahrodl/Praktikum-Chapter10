def Input():
    nim=input('Masukkan NIM\t\t:')
    nama=input('Masukkan Nama Mhs\t:')
    almt=input('Masukkan Alamat\t\t:')
    file.write(nim)
    file.write('|')
    file.write(nama)
    file.write('|')
    file.write(almt)
    file.write('\n')
    print('')
    global lagi
    lagi=input('Input lagi? (y/n)\t:')
    print('')

file=open('d:\dataMhs.txt','w') 
Input()                         
while True:
    if lagi=='y':
        Input()
    elif lagi=='n':
        file.close()
        print('')
        file2=open('d:\dataMhs.txt','r')
        print(file2.read())
        break
    else:
        break

    

