#membuat judul
print(('').ljust(50,'-'))
print(('SANDI CAESAR').center(50))
print(('').ljust(50,'-'))

#input data
file=input('Masukkan file teks sandi\t:')
n=int(input('Masukkan jumlah n\t\t:'))
print('')
print('Teks asli\t\t\t:',end='')

#membuka file
teks=open(file,'r')

ListOrd=[]
while True:
    huruf=teks.read(1)          #membaca isi file per karakter      
    if not huruf:
        break
    Ord=ord(huruf)              #mendapatkan nilai ASCII 
    ListOrd.append(Ord)         #menambahkannya ke dalam ListOrd  

P=open('d:/teksAsli.txt','w')   #membuat file text asli
ListChr=[]
for i in range(len(ListOrd)):            
    if ListOrd[i]==65:                
        ListOrd[i]=91
    geser=ListOrd[i]-n          #mendapatkan nilai ASCII sebelum digeser sebanyak n
    if geser+n==32:           
        geser=32                
    ListChr.append(geser)           
    P.write(chr(ListChr[i]))    #mengembalikan nilai ASCII dan menambahkannya ke file teks asli
P.close()
P2=open('d:/teksAsli.txt','r')
print(P2.read())

print('')
print(('').ljust(50,'-'))
