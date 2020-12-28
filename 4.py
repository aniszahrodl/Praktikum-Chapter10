#membuat dictionary sama seperti nomor 3
file2=open('d:\dataMhs.txt','r')
isi= list(file2.readlines())

List1=[]
for i in range(len(isi)):
    ekstrak=(isi[i]).split()
    List1.append(ekstrak[0])

List2=[]
for x in range(len(List1)):
    ekstrak2=List1[x].split('|')
    List2.append(ekstrak2)

dataMhs=[]
for y in range (len(List2)):
    P=List2[y]
    D=dict(nim=P[0],nama=P[1],alamat=P[2])
    dataMhs.append(D)

#memecah data dan masing-masing dibuat list
nim=[]
nama=[]
alamat=[]
for i in range(len(dataMhs)):
    a=dataMhs[i]
    nim.append(a['nim'])
    nama.append(a['nama'])
    alamat.append(a['alamat'])

#cari NIM
cari=input('Masukkan NIM Mahasiswa yang dicari:')
if cari not in nim:
    print('Data mahasiswa tidak ditemukan')
else:
    print('NIM\t:',cari)
    Q=nim.index(cari)
    print('Nama\t:',nama[Q])
    print('Alamat\t:',alamat[Q])
    
