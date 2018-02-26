# latihan modul5 list

# Copy

data1 = {"Nama" : "uis", "umur" :30, "JenisK" : "L", "Status" : "GandaCampuran"}
data2 = {"Nama" : "uisu", "umur" :31, "JenisK" : "P", "Status" : "GandaCampuran"}
data3 = data1.copy()
print(data3)

# Update

data1.update(data2)
print(data1)

# Clear

del data1["JenisK"]
print(data1)
data1.clear()
print(data1)

# Value

data1.values()
print(data1.values())
