Mountains = ["Jaya Wijaya", "Kerinci", "Semeru"]

print(Mountains)

# Mengakses elemen lewat indeks
print(Mountains[0])
print(Mountains[-1])

# Mengubah elemen
Mountains[1] = "Kilimanjaro"
print(Mountains)

# append(): tambah di akhir
Mountains.append("Everest")
print(Mountains)

# insert(): sisipkan di posisi tertentu
Mountains.insert(0, "Kilimanjaro")
print(Mountains)

# len(): jumlah elemen
print(f"Jumlah gunung: {len(Mountains)}")


print(sorted(Mountains))
print(sorted(Mountains, reverse=True))
print(Mountains)


Mountains.reverse()
print(Mountains)


Mountains.sort()
print(Mountains)
Mountains.sort(reverse=True)
print(Mountains)


removed = Mountains.pop()
print(f"Dikeluarkan dengan pop(): {removed}")
print(Mountains )


removed = Mountains.pop(0)
print(f"Dikeluarkan dengan pop(0): {removed}")


del Mountains[0]
print(Mountains)


Mountains.remove("Kilimanjaro")
print(Mountains)