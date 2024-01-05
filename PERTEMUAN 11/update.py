from matakuliah import matakuliah

# Update Data
a = matakuliah()
kodemk = '123243'
a.namamk = "Kalkulus II"
a.sks = "2"
a.updateBykodemk(kodemk)
b = a.getAllData()
print(b)
