from modules.kategori import (
    list_kategori, add_kategori, update_kategori,
    delete_kategori, get_kategori
)
from modules.pemasukan import (
    list_pemasukan, add_pemasukan, update_pemasukan,
    delete_pemasukan, get_pemasukan
)
from modules.pengeluaran import (
    list_pengeluaran, add_pengeluaran, update_pengeluaran,
    delete_pengeluaran, get_pengeluaran
)
from modules.laporan import (
    hitung_total_pemasukan,
    hitung_total_pengeluaran,
    hitung_saldo,
    laporan_bulanan,
    laporan_mingguan,
    tampilkan_tabel
)
from modules.fitur import (
    budget_alert_monthly,
    cari_transaksi,
    sort_transaksi
)



def menu_kategori():
    while True:
        print("\n=== MENU KATEGORI ===")
        print("1. Lihat semua kategori")
        print("2. Tambah kategori")
        print("3. Edit kategori")
        print("4. Hapus kategori")
        print("0. Kembali")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            data = list_kategori()
            print("\n--- DAFTAR KATEGORI ---")
            if not data:
                print("Belum ada kategori.")
            else:
                for k in data:
                    print(f"{k['id']}. {k['nama']} - {k['deskripsi']}")

        elif pilih == "2":
            nama = input("Nama kategori: ")
            desk = input("Deskripsi: ")
            try:
                add_kategori(nama, desk)
                print("Kategori ditambahkan!")
            except Exception as e:
                print("ERROR:", e)

        elif pilih == "3":
            try:
                id_edit = int(input("ID kategori yang ingin diubah: "))
                k = get_kategori(id_edit)
                if not k:
                    print("Kategori tidak ditemukan.")
                    continue

                nama_baru = input("Nama baru (kosong = tidak diubah): ")
                desk_baru = input("Deskripsi baru (kosong = tidak diubah): ")

                update_kategori(
                    id_edit,
                    nama=nama_baru if nama_baru else None,
                    deskripsi=desk_baru if desk_baru else None
                )
                print("Kategori berhasil diupdate.")
            except Exception as e:
                print("ERROR:", e)

        elif pilih == "4":
            try:
                id_hps = int(input("ID kategori yang ingin dihapus: "))
                delete_kategori(id_hps)
                print("Kategori berhasil dihapus!")
            except Exception as e:
                print("ERROR:", e)

        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")


def menu_pemasukan():
    while True:
        print("\n=== MENU PEMASUKAN ===")
        print("1. Lihat pemasukan")
        print("2. Tambah pemasukan")
        print("3. Edit pemasukan")
        print("4. Hapus pemasukan")
        print("0. Kembali")


        pilih = input("Pilih menu: ")

        if pilih == "1":
            data = list_pemasukan()
            print("\n--- DAFTAR PEMASUKAN ---")
            if not data:
                print("Belum ada pemasukan.")
            else:
                for p in data:
                    print(f"{p['id']}. {p.get('tanggal','-')} | Rp{p['jumlah']} | Kategori {p['kategori_id']} | {p['catatan']}")

        elif pilih == "2":
            try:
                tanggal = input("Tanggal (YYYY-MM-DD): ")
                jml = int(input("Jumlah pemasukan: "))
                kat = int(input("ID kategori: "))
                ctt = input("Catatan: ")

                add_pemasukan(jml, kat, ctt, tanggal=tanggal)
                print("Pemasukan ditambahkan!")
            except Exception as e:
                print("ERROR:", e)

        elif pilih == "3":
            try:
                id_edit = int(input("ID pemasukan yang ingin diubah: "))
                item = get_pemasukan(id_edit)
                if not item:
                    print("Data tidak ditemukan.")
                    continue

                tanggal_baru = input("Tanggal baru (kosong=skip): ")
                jumlah_baru = input("Jumlah baru (kosong=skip): ")
                kategori_baru = input("Kategori baru (kosong=skip): ")
                catatan_baru = input("Catatan baru (kosong=skip): ")

                update_pemasukan(
                    id_edit,
                    tanggal=tanggal_baru if tanggal_baru else None,
                    jumlah=int(jumlah_baru) if jumlah_baru else None,
                    kategori_id=int(kategori_baru) if kategori_baru else None,
                    catatan=catatan_baru if catatan_baru else None
                )

                print("Pemasukan berhasil diupdate.")

            except Exception as e:
                print("ERROR:", e)

        elif pilih == "4":
            id_hps = int(input("ID pemasukan yang ingin dihapus: "))
            delete_pemasukan(id_hps)
            print("Pemasukan berhasil dihapus!")

        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")

def menu_pengeluaran():
    while True:
        print("\n=== MENU PENGELUARAN ===")
        print("1. Lihat pengeluaran")
        print("2. Tambah pengeluaran")
        print("3. Edit pengeluaran")
        print("4. Hapus pengeluaran")
        print("0. Kembali")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            data = list_pengeluaran()
            print("\n--- DAFTAR PENGELUARAN ---")
            if not data:
                print("Belum ada pengeluaran.")
            else:
                for p in data:
                    print(f"{p['id']}. {p.get('tanggal','-')} | Rp{p['jumlah']} | Kategori {p['kategori_id']} | {p['catatan']}")

        elif pilih == "2":
            try:
                tanggal = input("Tanggal (YYYY-MM-DD): ")
                jml = int(input("Jumlah pengeluaran: "))
                kat = int(input("ID kategori: "))
                ctt = input("Catatan: ")

                add_pengeluaran(jml, kat, ctt, tanggal=tanggal)
                print("Pengeluaran ditambahkan!")
            except Exception as e:
                print("ERROR:", e)

        elif pilih == "3":
            try:
                id_edit = int(input("ID pengeluaran yang ingin diubah: "))
                item = get_pengeluaran(id_edit)
                if not item:
                    print("Data tidak ditemukan.")
                    continue

                tanggal_baru = input("Tanggal baru (kosong=skip): ")
                jumlah_baru = input("Jumlah baru (kosong=skip): ")
                kategori_baru = input("Kategori baru (kosong=skip): ")
                catatan_baru = input("Catatan baru (kosong=skip): ")

                update_pengeluaran(
                    id_edit,
                    tanggal=tanggal_baru if tanggal_baru else None,
                    jumlah=int(jumlah_baru) if jumlah_baru else None,
                    kategori_id=int(kategori_baru) if kategori_baru else None,
                    catatan=catatan_baru if catatan_baru else None
                )

                print("Pengeluaran berhasil diupdate.")

            except Exception as e:
                print("ERROR:", e)

        elif pilih == "4":
            id_hps = int(input("ID pengeluaran yang ingin dihapus: "))
            delete_pengeluaran(id_hps)
            print("Pengeluaran berhasil dihapus!")

        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")

def menu_laporan():
    while True:
        print("\n=== Laporan Keuangan ===")
        print("1. Total Pemasukan")
        print("2. Total Pengeluaran")
        print("3. Saldo Akhir")
        print("4. Laporan Bulanan")
        print("5. Laporan Mingguan")
        print("6. Kembali")
        
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            total = hitung_total_pemasukan()
            print(f"\nTotal Pemasukan: Rp {total}")

        elif pilihan == "2":
            total = hitung_total_pengeluaran()
            print(f"\nTotal Pengeluaran: Rp {total}")

        elif pilihan == "3":
            saldo = hitung_saldo()
            print(f"\nSaldo Akhir: Rp {saldo}")

        elif pilihan == "4":
            bulan = int(input("Masukkan Bulan (1-12): "))
            tahun = int(input("Masukkan Tahun: "))
            laporan = laporan_bulanan(bulan, tahun)

            print("\n=== LAPORAN PEMASUKAN BULANAN ===")
            tampilkan_tabel(laporan["pemasukan"])
            print(f"Total Pemasukan: Rp {laporan['total_pemasukan']}")

            print("\n=== LAPORAN PENGELUARAN BULANAN ===")
            tampilkan_tabel(laporan["pengeluaran"])
            print(f"Total Pengeluaran: Rp {laporan['total_pengeluaran']}")

            print(f"\nSaldo Bulanan: Rp {laporan['saldo']}")

        elif pilihan == "5":
            minggu = int(input("Masukkan Minggu ke berapa (1-52): "))
            tahun = int(input("Masukkan Tahun: "))
            laporan = laporan_mingguan(minggu, tahun)

            print("\n=== LAPORAN PEMASUKAN MINGGUAN ===")
            tampilkan_tabel(laporan["pemasukan"])
            print(f"Total Pemasukan: Rp {laporan['total_pemasukan']}")

            print("\n=== LAPORAN PENGELUARAN MINGGUAN ===")
            tampilkan_tabel(laporan["pengeluaran"])
            print(f"Total Pengeluaran: Rp {laporan['total_pengeluaran']}")

            print(f"\nSaldo Mingguan: Rp {laporan['saldo']}")

        elif pilihan == "6":
            break

        else:
            print("Pilihan tidak valid.")

def menu_fitur():
    while True:
        print("\n=== FITUR TAMBAHAN ===")
        print("1. Budget alert (cek anggaran bulanan)")
        print("2. Pencarian transaksi")
        print("3. Sortir transaksi")
        print("0. Kembali")

        pilih = input("Pilih fitur: ")

        if pilih == "1":
            limit = int(input("Masukkan batas anggaran bulanan (Rp): "))
            msg = budget_alert_monthly(limit)
            print(msg)

        elif pilih == "2":
            q = input("Masukkan kata kunci / ID: ")
            results = cari_transaksi(q)
            print("\n--- Hasil Pencarian ---")
            if not results:
                print("Tidak ada transaksi ditemukan.")
            else:
                for r in results:
                    print(f"{r['type']} {r['id']}: {r.get('tanggal','-')} | Rp{r['jumlah']} | Kategori {r['kategori_id']} | {r.get('catatan','')}")
            
        elif pilih == "3":
            print("Field untuk diurutkan: tanggal, jumlah, kategori_id, id, type")
            by = input("Urut berdasarkan (default 'tanggal'): ") or "tanggal"
            order = input("Urutkan (asc/desc, default asc): ") or "asc"
            rev = True if order.lower().startswith("d") else False
            try:
                hasil = sort_transaksi(by=by, reverse=rev)
                if not hasil:
                    print("Tidak ada transaksi.")
                else:
                    for r in hasil:
                        print(f"{r['type']} {r.get('id','-')}: {r.get('tanggal','-')} | Rp{r.get('jumlah','-')} | Kategori {r.get('kategori_id','-')} | {r.get('catatan','')}")
            except Exception as e:
                print("ERROR:", e)

        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")


def main():
    while True:
        print("\n=== SISTEM KEUANGAN ANAK KOST ===")
        print("1. Kelola Kategori")
        print("2. Kelola Pemasukan")
        print("3. Kelola Pengeluaran")
        print("4. Laporan Keuangan")
        print("5. Fitur Tambahan")
        print("0. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            menu_kategori()
        elif pilih == "2":
            menu_pemasukan()
        elif pilih == "3":
            menu_pengeluaran()
        elif pilih == "4":
            menu_laporan()
        elif pilih == "5":
            menu_fitur()
        elif pilih == "0":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()

