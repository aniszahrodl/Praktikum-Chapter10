a=input('Masukkan nama file:')
file = open(a, 'r')
isi=list(file.readlines())

List1=[]
for i in range(len(isi)):
    ekstrak1=(isi[i]).split()
    List1.append(ekstrak1[0])

List2=[]
for x in range(len(List1)):
    ekstrak2=List1[x].split('|')
    List2.append(ekstrak2)

fileBaru=open('d:/hasilBilangan2.txt','w')   
for i in range(len(List2)):
    P=List2[i]
    fileBaru.write(str(int(P[0])+int(P[1])))
    fileBaru.write('\n')
fileBaru.close()
buka=open('d:/hasilBilangan2.txt','r') 
print(buka.read())
