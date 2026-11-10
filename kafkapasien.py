class RumahSakit:
    def __init__(self):
        # 10 data pasien opname (Nama, Penyakit, Tipe Kamar, Tarif per Hari)
        self.data_pasien = [
            {"nama": "Andi", "penyakit": "Demam Berdarah", "kamar": "VIP", "tarif": 750000},
            {"nama": "Budi", "penyakit": "Tipes", "kamar": "Kelas 1", "tarif": 500000},
            {"nama": "Citra", "penyakit": "Asma", "kamar": "Kelas 2", "tarif": 300000},
            {"nama": "Dewi", "penyakit": "Fraktur Tulang", "kamar": "VIP", "tarif": 750000},
            {"nama": "Eko", "penyakit": "Hipertensi", "kamar": "Kelas 3", "tarif": 150000},
            {"nama": "Fajar", "penyakit": "Gastroenteritis", "kamar": "Kelas 1", "tarif": 500000},
            {"nama": "Gita", "penyakit": "Pneumonia", "kamar": "ICU", "tarif": 1200000},
            {"nama": "Hadi", "penyakit": "Diabetes", "kamar": "Kelas 2", "tarif": 300000},
            {"nama": "Intan", "penyakit": "Vertigo", "kamar": "Kelas 3", "tarif": 150000},
            {"nama": "Joko", "penyakit": "Apendisitis", "kamar": "VIP", "tarif": 750000}
        ]

    def kelola_pasien(self):
        print("=== PROGRAM ADMINISTRASI PASIEN RUMAH SAKIT ===")
        print("Daftar 10 Pasien Opname:")
        for idx, p in enumerate(self.data_pasien):
            print(f"{idx + 1}. Nama: {p['nama']} | Penyakit: {p['penyakit']} | Kamar: {p['kamar']}")
        
        # Meminta input pilihan pasien dan lama menginap
        pilihan_idx = int(input("\nMasukkan nomor pasien yang ingin diproses (1-10): ")) - 1
        lama_hari = int(input("Masukkan lama menginap (dalam hari): "))
        
        if 0 <= pilihan_idx < len(self.data_pasien):
            pasien = self.data_pasien[pilihan_idx]
            
            # Menerapkan Operator Ternary satu baris (A if kondisi else B)
            menu_makanan = "Menu Diet Khusus & Bubur" if lama_hari > 3 else "Menu Makanan Biasa/Lunak"
            aturan_besuk = "Jam besuk fleksibel (Khusus penunggu)" if pasien['kamar'] == "ICU" or lama_hari > 5 else "Jam besuk standar (16.00 - 18.00)"
            
            # Menghitung total biaya (Tarif per hari * lama hari) dengan diskon jika > 7 hari
            total_biaya = (pasien['tarif'] * lama_hari * 0.9) if lama_hari > 7 else (pasien['tarif'] * lama_hari)
            
            # Output Hasil
            print(f"\n--- HASIL ANALISIS UNTUK PASIEN: {pasien['nama']} ---")
            print(f"Penyakit       : {pasien['penyakit']}")
            print(f"Tipe Kamar     : {pasien['kamar']}")
            print(f"Lama Menginap  : {lama_hari} hari")
            print(f"Menu Makanan   : {menu_makanan}")
            print(f"Aturan Besuk   : {aturan_besuk}")
            print(f"Total Biaya    : Rp {total_biaya:,.0f}")
        else:
            print("Pilihan nomor pasien tidak valid!")

# Menjalankan Program 2
if __name__ == "__main__":
    rs = RumahSakit()
    rs.kelola_pasien()