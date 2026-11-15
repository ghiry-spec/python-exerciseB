
m = 3
n = 4
MB = [0] * m
for i in range(m):
    MB[i] = [0] * n

print(MB)

for baris in range(0,m):
    for kolom in range(0,n):
        MB[baris][kolom] = baris + kolom

print(MB)
