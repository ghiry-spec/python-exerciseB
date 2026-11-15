import random 

m = 3
n = 4
MA = [0] * m

print (MA)
print (len(MA))
for baris in range(m):
    MA[baris] = [0] * n
    MA[baris][0] = random.randrange(1, 10)
    MA[baris][1] = random.randrange(1, 10)
    MA[baris][2] = random.randrange(1, 10)
    MA[baris][3] = random.randrange(1, 10)

print (MA)
print (MA[1][2])

for baris in range(len(MA)):
    for kolom in range (len(MA[baris])):
        print (MA[baris][kolom],"\t",end = " ")
    print()


