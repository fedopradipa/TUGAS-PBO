print("Program menghitung luas permukaan dan volume limas segitiga")

# Atur nilai variabel
panjang_alas_segitiga = float(input("Masukkan panjang alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
tinggi_limas = float(input("Masukkan tinggi limas: "))
# Menghitung luas alas segitiga
luas_alas_segitiga = panjang_alas_segitiga * tinggi_limas /2


# Menghitung luas permukaan limas segitiga
luas_permukaan = luas_alas_segitiga + 3 * (panjang_alas_segitiga * tinggi_segitiga/2)

# Menghitung volume limas segitiga
volume = (panjang_alas_segitiga * tinggi_segitiga/2) * tinggi_limas/3

# Output hasil perhitungan
print("----Hasil perhitungan----")
print(f"Luas permukaan limas segitiga adalah: {luas_permukaan}")
print(f"Volume limas segitiga adalah: {volume}")
