print("Program menghitung luas permukaan dan volume limas segiempat")
# Atur nilai variabel
panjang_alas = float(input("Masukkan panjang alas limas: "))
lebar_alas = float(input("Masukkan lebar alas limas: "))
tinggi_limas = float(input("Masukkan tinggi limas: "))

# Menghitung luas alas Limas segiempat
luas_alas = panjang_alas * lebar_alas
# Menghitung luas permukaan segiempat
luas_permukaan = luas_alas + 2 * (panjang_alas * tinggi_limas/2) + 2 * (lebar_alas * tinggi_limas/2)
# Menghitung volume limas segi empat
volume = luas_alas * tinggi_limas/3

# output hasil perhitungan
print("---Hasil perhitungan----")
print(f"Luas permukaan limas segi empat adalah: {luas_permukaan}")
print(f"Volume limas segi empat adalah: {volume}")
