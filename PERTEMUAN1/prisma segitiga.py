print("program Menghitung Luas dan Volume Prisma Segitiga")

# Atur Nilai Variabel
sisi_1 = float(input("masukan nilai Sisi 1= "))
sisi_2 = float(input("masukan nilai Sisi 2= "))
sisi_3 = float(input("masukan nilai Sisi 3= "))
tinggi_prisma = float(input("masukan nilai Tinggi Prisma: "))
alas = float(input("masukan nilai Alas: "))
tinggi = float(input("masukan nilai Tinggi: "))

# menghitung luas segitiga
luas_segitiga = (sisi_1+sisi_2+sisi_3)* tinggi_prisma
# menghitung luas prisma
luas_prisma = (sisi_1+sisi_2+sisi_3) * tinggi_prisma * alas * tinggi
# menghitung volume prisma
volume = alas * tinggi *tinggi_prisma / 2

# Output hasil perhitungan
print("---Hasil Perhitungan---") 
print(f"luas segitiga adalah: {luas_segitiga}")
print(f"luas prisma adalah: {luas_prisma}")
print(f"volume prisma segitiga: {volume}")