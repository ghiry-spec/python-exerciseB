MA = [
    [3, 7],
    [5, 2],
]

MB = [
    [1, 4],
    [6, 8],
]

MC = []

for i in range(0, len(MA)):
    hasiljumlah = 0
    baris = []
    for j in range(0, len(MA[i])):
        hasiljumlah = MA[i][j] + MB[i][j]
        baris.append(hasiljumlah)

    MC.append(baris)

print (MC)

