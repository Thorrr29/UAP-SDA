import csv

class Pasien:
    def __init__(self, id_pasien, nama, umur, alamat):
        self.id_pasien = id_pasien
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

class Dokter:
    def __init__(self, id_dokter, nama, spesialisasi):
        self.id_dokter = id_dokter
        self.nama = nama
        self.spesialisasi = spesialisasi

class Jadwal:
    def __init__(self, id_jadwal, id_pasien, id_dokter, tanggal):
        self.id_jadwal = id_jadwal
        self.id_pasien = id_pasien
        self.id_dokter = id_dokter
        self.tanggal = tanggal

class ManajemenRumahSakit:
    def __init__(self):
        self.pasien = []
        self.dokter = []
        self.jadwal = []

    def tambah_pasien(self, pasien):
        self.pasien.append(pasien)

    def tambah_dokter(self, dokter):
        self.dokter.append(dokter)

    def tambah_jadwal(self, jadwal):
        self.jadwal.append(jadwal)

    def perbarui_pasien(self, id_pasien, pasien_baru):
        for i, pasien in enumerate(self.pasien):
            if pasien.id_pasien == id_pasien:
                self.pasien[i] = pasien_baru
                return True
        return False

    def perbarui_dokter(self, id_dokter, dokter_baru):
        for i, dokter in enumerate(self.dokter):
            if dokter.id_dokter == id_dokter:
                self.dokter[i] = dokter_baru
                return True
        return False

    def hapus_pasien(self, id_pasien):
        self.pasien = [pasien for pasien in self.pasien if pasien.id_pasien != id_pasien]

    def hapus_dokter(self, id_dokter):
        self.dokter = [dokter for dokter in self.dokter if dokter.id_dokter != id_dokter]

    def urutkan_pasien_berdasarkan_nama(self):
        self.pasien.sort(key=lambda x: x.nama)

    def urutkan_dokter_berdasarkan_nama(self):
        self.dokter.sort(key=lambda x: x.nama)

    def cari_pasien_berdasarkan_nama(self, nama):
        return [pasien for pasien in self.pasien if nama.lower() in pasien.nama.lower()]

    def cari_dokter_berdasarkan_nama(self, nama):
        return [dokter for dokter in self.dokter if nama.lower() in dokter.nama.lower()]

    def impor_pasien_dari_csv(self, file_path):
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                pasien = Pasien(row['id_pasien'], row['nama'], row['umur'], row['alamat'])
                self.tambah_pasien(pasien)

    def impor_dokter_dari_csv(self, file_path):
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                dokter = Dokter(row['id_dokter'], row['nama'], row['spesialisasi'])
                self.tambah_dokter(dokter)

    def tampilkan_pasien(self):
        for pasien in self.pasien:
            print(f"ID: {pasien.id_pasien}, Nama: {pasien.nama}, Umur: {pasien.umur}, Alamat: {pasien.alamat}")

    def tampilkan_dokter(self):
        for dokter in self.dokter:
            print(f"ID: {dokter.id_dokter}, Nama: {dokter.nama}, Spesialisasi: {dokter.spesialisasi}")

def main():
    rumah_sakit = ManajemenRumahSakit()

    while True:
        print("\nSistem Manajemen Rumah Sakit")
        print("1. Tambah Pasien")
        print("2. Tambah Dokter")
        print("3. Perbarui Pasien")
        print("4. Perbarui Dokter")
        print("5. Hapus Pasien")
        print("6. Hapus Dokter")
        print("7. Lihat Pasien")
        print("8. Lihat Dokter")
        print("9. Impor Pasien dari CSV")
        print("10. Impor Dokter dari CSV")
        print("11. Urutkan Pasien berdasarkan Nama")
        print("12. Urutkan Dokter berdasarkan Nama")
        print("13. Cari Pasien berdasarkan Nama")
        print("14. Cari Dokter berdasarkan Nama")
        print("15. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            id_pasien = input("Masukkan ID Pasien: ")
            nama = input("Masukkan Nama Pasien: ")
            umur = input("Masukkan Umur Pasien: ")
            alamat = input("Masukkan Alamat Pasien: ")
            pasien = Pasien(id_pasien, nama, umur, alamat)
            rumah_sakit.tambah_pasien(pasien)
        elif pilihan == '2':
            id_dokter = input("Masukkan ID Dokter: ")
            nama = input("Masukkan Nama Dokter: ")
            spesialisasi = input("Masukkan Spesialisasi Dokter: ")
            dokter = Dokter(id_dokter, nama, spesialisasi)
            rumah_sakit.tambah_dokter(dokter)
        elif pilihan == '3':
            id_pasien = input("Masukkan ID Pasien untuk Diperbarui: ")
            nama = input("Masukkan Nama Pasien Baru: ")
            umur = input("Masukkan Umur Pasien Baru: ")
            alamat = input("Masukkan Alamat Pasien Baru: ")
            pasien_baru = Pasien(id_pasien, nama, umur, alamat)
            if rumah_sakit.perbarui_pasien(id_pasien, pasien_baru):
                print("Pasien berhasil diperbarui")
            else:
                print("Pasien tidak ditemukan")
        elif pilihan == '4':
            id_dokter = input("Masukkan ID Dokter untuk Diperbarui: ")
            nama = input("Masukkan Nama Dokter Baru: ")
            spesialisasi = input("Masukkan Spesialisasi Dokter Baru: ")
            dokter_baru = Dokter(id_dokter, nama, spesialisasi)
            if rumah_sakit.perbarui_dokter(id_dokter, dokter_baru):
                print("Dokter berhasil diperbarui")
            else:
                print("Dokter tidak ditemukan")
        elif pilihan == '5':
            id_pasien = input("Masukkan ID Pasien untuk Dihapus: ")
            rumah_sakit.hapus_pasien(id_pasien)
            print("Pasien berhasil dihapus")
        elif pilihan == '6':
            id_dokter = input("Masukkan ID Dokter untuk Dihapus: ")
            rumah_sakit.hapus_dokter(id_dokter)
            print("Dokter berhasil dihapus")
        elif pilihan == '7':
            rumah_sakit.tampilkan_pasien()
        elif pilihan == '8':
            rumah_sakit.tampilkan_dokter()
        elif pilihan == '9':
            file_path = input("Masukkan Path File CSV Pasien: ")
            rumah_sakit.impor_pasien_dari_csv(file_path)
            print("Pasien berhasil diimpor")
        elif pilihan == '10':
            file_path = input("Masukkan Path File CSV Dokter: ")
            rumah_sakit.impor_dokter_dari_csv(file_path)
            print("Dokter berhasil diimpor")
        elif pilihan == '11':
            rumah_sakit.urutkan_pasien_berdasarkan_nama()
            print("Pasien diurutkan berdasarkan nama")
        elif pilihan == '12':
            rumah_sakit.urutkan_dokter_berdasarkan_nama()
            print("Dokter diurutkan berdasarkan nama")
        elif pilihan == '13':
            nama = input("Masukkan Nama Pasien untuk Dicari: ")
            hasil = rumah_sakit.cari_pasien_berdasarkan_nama(nama)
            for pasien in hasil:
                print(f"ID: {pasien.id_pasien}, Nama: {pasien.nama}, Umur: {pasien.umur}, Alamat: {pasien.alamat}")
        elif pilihan == '14':
            nama = input("Masukkan Nama Dokter untuk Dicari: ")
            hasil = rumah_sakit.cari_dokter_berdasarkan_nama(nama)
            for dokter in hasil:
                print(f"ID: {dokter.id_dokter}, Nama: {dokter.nama}, Spesialisasi: {dokter.spesialisasi}")
        elif pilihan == '15':
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
