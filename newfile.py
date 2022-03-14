print("Hello World")

# tipe data
nama = ("Dolandre Febrianto")
print(nama)
umur = 19
print(umur)
nilai_ipk = 4.95
print(nilai_ipk)
print(12 > 8)
print(12 < 8)

# pembuktian tipe data
nama = ("Dolandre Febrianto")
print(nama,type(nama))
umur = 19
print(umur,type(umur))
nilai_ipk = 4.95
print(nilai_ipk,type(nilai_ipk))
print(12 > 8,type(12 > 8))
print(12 < 8,type(12 < 8))

#operator aritmetika
nilai = 4
nilai2 = 6

print("penjumlahan",nilai + nilai2)
print("pengurangan",nilai-nilai2)
print("perkalian",nilai * nilai2)
print("pembagian",nilai / nilai2)
print("sisa_bagi",nilai % nilai2)
print("pangkat",nilai ** nilai2)
print("pembagian_bulat",nilai // nilai2)

#operasi penugasan 
nilai = 8

nilai += 2
print(nilai)

nilai = 3
print(nilai)

nilai = 4
print(nilai)

nilai /= 4
print(nilai)

nilai %= 3
print(nilai)

nilai **= 2
print(nilai)

nilai //=4
print(nilai)

#Percabangan if
nilai =int(input("Masukkan nilai")) 

if (nilai >=85): 
   print("Nilai A")
   
#percabangan if,else
nilai -int(input("Masukkan nilai"))

if (nilai >=60) : 
    print("LULUS")
else: 
    print("Tidak LULUS")
    
#percabangan if,elif,else
umur = int(input("Masukkan umur"))
if umur >= 1 and umur <= 12:
	print("anak-anak") 
elif umur >= 13 and umur <= 16:
	print(Remaja) 
elif umur >= 17:
	print("Dewasa")
else: 
    print('periksa kembali masukkan anda')
    

   
