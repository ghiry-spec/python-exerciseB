names = ["Gery", "Bli", "Oji"]

print("Halo, Ternyata saya menemukan meja baru yang lebih besar untuk acara dinner malam ini!")

names.insert(0, "Komang")
names.insert(2, "Agus")
names.append("Dewi")

print(f"\nHalo, {names[0]} Aku mengundangmu untuk datang ke acara dinner malam ini!")
print(f"Halo, {names[1]} Aku mengundangmu untuk datang ke acara dinner malam ini!")
print(f"Halo, {names[2]} Aku mengundangmu untuk datang ke acara dinner malam ini!")
print(f"Halo, {names[3]} Aku mengundangmu untuk datang ke acara dinner malam ini!")
print(f"Halo, {names[4]} Aku mengundangmu untuk datang ke acara dinner malam ini!")
print(f"Halo, {names[5]} Aku mengundangmu untuk datang ke acara dinner malam ini!")

print("\nMaaf, saya hanya bisa mengundang dua orang untuk datang ke acara dinner malam ini.")

removed = names.pop()
print(f"\nMaaf, {removed} saya tidak bisa mengundangmu untuk datang ke acara dinner malam ini.")
removed = names.pop()
print(f"\nMaaf, {removed} saya tidak bisa mengundangmu untuk datang ke acara dinner malam ini.")
removed = names.pop()
print(f"\nMaaf, {removed} saya tidak bisa mengundangmu untuk datang ke acara dinner malam ini.")
removed = names.pop()
print(f"\nMaaf, {removed} saya tidak bisa mengundangmu untuk datang ke acara dinner malam ini.")

print(f"\nHalo, {names[0]} kamu masih diundang untuk datang ke acara dinner malam ini!")
print(f"Halo, {names[1]} kamu masih diundang untuk datang ke acara dinner malam ini!")

del names[0]
del names[0]

print(names)