#membuat judul
print(('').ljust(50,'-'))
print(('SANDI CAESAR').center(50))
print(('').ljust(50,'-'))

#input data
file=input('Masukkan file teks asli\t:')
n=int(input('Masukkan jumlah n\t:'))
print('')
print('Teks sandi\t\t:',end='')

#membuka file
teks=open(file,'r')

ListOrd=[]
while True:
    huruf=teks.read(1)          #membaca isi file per karakter
    if not huruf:
        break
    Ord=ord(huruf)              #mendapatkan nilai ASCII
    ListOrd.append(Ord)         #menambahkannya ke dalam ListOrd

P=open('d:/hasilSandi.txt','w') #membuat file text hasil sandi

ListChr=[]
for i in range(len(ListOrd)):
    geser=ListOrd[i]+n          #mendapatkan nilai ASCII hasil geser    
    if geser>90:                #karna nilai ASCII 90=Z, maka jika lebih dari 90,
        geser=65                #dikembalikan ke huruf A yang memiliki nilai ASCII 65
    elif geser-n==32:           #karna nilai ASCII 32=(spasi),maka tidak perlu digeser,
        geser=32                #dengan membuatnya tetap bernilai 32
    ListChr.append(geser)       #menambahkan hasil geser ke ListChr       
    P.write(chr(ListChr[i]))    #mengembalikan nilai ASCII dan menambahkannya ke file teks hasil Sandi
P.close()
P2=open('d:/hasilSandi.txt','r')#membunka file teks hasil sandi
print(P2.read())

print('')
print(('').ljust(50,'-'))


