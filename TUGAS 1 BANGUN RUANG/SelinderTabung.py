print("Program menghitung luas permukaan dan volume silinder(tabung)")

# Atur nilai variabel
jari_jari = float(input("Masukkan jari-jari silinder: "))
tinggi = float(input("Masukkan tinggi silinder: "))
PHI = 3.14

# Menghitung luas selimut silinder
luas_selimut = 2 * PHI * jari_jari * tinggi
# Menghitung luas permukaan silinder
luas_permukaan = luas_selimut + (2 * PHI * jari_jari**2) 
# Menghitung volume silinder
volume = PHI * jari_jari**2 * tinggi

# Output hasil perhitungan
print("---Hasil perhitungan----")
print(f"Luas permukaan silinder adalah: {luas_permukaan}")
print(f"Volume silinder adalah: {volume}")
