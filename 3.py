#membuka file text yang telah dibuat pada nomor 2
file2=open('d:\dataMhs.txt','r')

#membaca file text per baris dan mengubahnya ke bentuk list agar bisa di ekstrak datanya menggunakan split
isi= list(file2.readlines())

#mengekstrak data mengunakan split kemudian menambahkannya ke List1
List1=[]
for i in range(len(isi)):
    ekstrak=(isi[i]).split()
    List1.append(ekstrak[0])

#menghapus '|' menggunakan split dan menambahkannya ke List2
List2=[]
for x in range(len(List1)):
    ekstrak2=List1[x].split('|')
    List2.append(ekstrak2)

#membuat dictionary dan menambahkannya ke dalam list dataMhs=[]
dataMhs=[]
for y in range (len(List2)):
    P=List2[y]
    D=dict(nim=P[0],nama=P[1],alamat=P[2])
    dataMhs.append(D)

print(dataMhs)


