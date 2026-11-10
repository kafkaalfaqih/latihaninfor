class Apotek:
    def __init__(self):
        # 10 jenis obat unik
        self.daftar_obat = [
            "Paracetamol", "Amoxicillin", "Ibuprofen", "Antasida", "Vitamin C",
            "Cetirizine", "Omeprazole", "Salep Kulit", "Obat Batuk", "Oralit"
        ]
        self.batas_minimal = 10

    def cek_stok_obat(self):
        print("=== STOK OBAT APOTEK ===")
        print(f"Batas minimal stok mencukupi adalah: {self.batas_minimal}\n")
        
        # Perulangan untuk menginput jumlah stok tiap obat
        for obat in self.daftar_obat:
            # Menerima input dari pengguna
            stok_input = int(input(f"Masukkan jumlah stok untuk obat {obat}: "))
            
            # Menggunakan operator pembanding langsung untuk menghasilkan True/False
            apakah_aman = stok_input >= self.batas_minimal
            apakah_kritis = stok_input < 5
            apakah_pas = stok_input == self.batas_minimal
            
            print(f"--> Hasil Perbandingan untuk {obat}:")
            print(f"    Stok Mencukupi (>= {self.batas_minimal}): {apakah_aman}")
            print(f"    Stok Pas (== {self.batas_minimal}): {apakah_pas}")
            print("-" * 40)

# Menjalankan Program 1
if __name__ == "__main__":
    apotek_pusat = Apotek()
    apotek_pusat.cek_stok_obat()