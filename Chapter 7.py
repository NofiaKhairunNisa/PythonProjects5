#Praktikum satu

#nomor empat
file=open("d:/myfile.txt","r")
print(file.read())

print()

#Praktikum dua
#nomor lima
try:
    file=open("d:/data.txt","r")
    bil1=int(file.readline())
    bil2=int(file.readline())
    hasil=bil1/bil2
    print(bil1,'dibagi',bil2,'sama dengan',hasil)
except FileNotFoundError:
    print("File tidak ditemukan")
except ZeroDivisionError:
    print("Tidak boleh pembagian dengan nol")

print()

#Praktikum tiga
#nomor lima
file=open("d:/data2.txt","r")
try:
    sum=0
    for data2 in file:
        sum=sum+int(data2)
    print(sum)
except ValueError:
    print("Input data tidak valid")

print()

#Latihan
#nomor satu
file=open("d:/anyfile.txt","r")
print("Isi File d:/anyfile.txt adalah",file.read())

print()

#nomor dua
file=open("d:/dataMhs.txt","a")
file.write("XXXX")
file.write("XXXX")
file.close()

print()
    
#nomor tiga
print("------------------------")
print("PROGRAM HITUNG RATA-RATA")
print("------------------------")

try:
    while True:
        bil=int(input("Masukkan bilangan bulat:"))
        print("Ulangi lagi (y/n)?:")
        jawab=input()
        if jawab=='n':
            break
except ValueError:
    print("Bukan bilangan bulat")

def rerata (*myData):
    sum=0
    i=0
    for data in myData:
        sum+=data
        i+=1
    rata2=sum/i
    print("Rata-ratanya:",rata2)
    
