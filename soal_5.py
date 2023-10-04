from collections import deque

class AntrianBank:
    def __init__(self):
        self.antrian = deque()

    def masuk(self, pelanggan):
        self.antrian.append(pelanggan)

    def keluar(self):
        if not self.isEmpty():
            return self.antrian.popleft()
        else:
            print("Antrian kosong. Tidak ada pelanggan yang keluar.")
            return None

    def isEmpty(self):
        return len(self.antrian) == 0

    def ukuran(self):
        return len(self.antrian)

# Contoh penggunaan
antrian_bank = AntrianBank()
antrian_bank.masuk("Pelanggan 1")
antrian_bank.masuk("Pelanggan 2")
antrian_bank.masuk("Pelanggan 3")

print("Ukuran antrian:", antrian_bank.ukuran())

pelanggan_keluar = antrian_bank.keluar()
if pelanggan_keluar:
    print(pelanggan_keluar, "telah keluar dari antrian.")

print("Ukuran antrian setelah pelanggan keluar:", antrian_bank.ukuran())