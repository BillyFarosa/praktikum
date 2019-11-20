#Latihan
#Akses List

list_a = [10, 20, 30, 40, 50]
print(list_a)
print(list_a[2])
print(list_a[1:4])
print(list_a[-1])

#Ubah Element List

list_a[3] = 45
print(list_a[3])
list_a[3:4] = 48, 55
print(list_a[3:5])

#Tambah ELement List

list_b = list_a[0:2]
print(list_b)
list_b.append(25)
print(list_b)
list_b.extend([35, 45, 55])
print(list_b)
list_c = list_a + list_b
print(list_c)
