print("Program menghitung luas permukaan dan volume bola")
# Atur nilai variabel
PHI = 3.14
jari_jari = float(input("Masukan nilai jari-jari bola: "))

# Menghitung luas permukaan bola
luas_permukaan = 4 * PHI * jari_jari**2
# Menghitung volume bola
volume = (4/3) * PHI * jari_jari**3

# Output hasil perhitungan
print("---Hasil perhitungan----")
print(f"Luas permukaan bola adalah: {luas_permukaan} ")
print(f"volume bola adalah: {volume}")