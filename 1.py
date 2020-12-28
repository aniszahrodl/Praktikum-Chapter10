#membuka file teks
a= input('Masukkan nama file:')
file = open(a, 'r')
data=list(file.readlines())

#memecah data dan memasukkannya ke dalam List
List=[]
for i in range(len(data)):
    Split=(data[i]).split()
    List.append(Split[0])

#mengelompokkan bilangan genap dan ganjil menggunakan list
genap=[]
ganjil=[]
for i in range(len(List)):
    x=int(List[i])
    if x%2==0:
        genap.append(x)
    else:
        ganjil.append(x)

print('Banyaknya bilangan genap\t:',len(genap))
print('Banyaknya bilangan ganjil\t:',len(ganjil))

