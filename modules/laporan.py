from datetime import datetime
from .utils import load_data

def hitung_total_pemasukan():
    """Menghitung total pemasukan dari data.json"""
    data = load_data()
    total = sum(item["jumlah"] for item in data["pemasukan"])
    return total


def hitung_total_pengeluaran():
    """Menghitung total pengeluaran dari data.json"""
    data = load_data()
    total = sum(item["jumlah"] for item in data["pengeluaran"])
    return total


def hitung_saldo():
    """Menghitung saldo akhir (pemasukan - pengeluaran)"""
    pemasukan = hitung_total_pemasukan()
    pengeluaran = hitung_total_pengeluaran()
    return pemasukan - pengeluaran


def filter_bulanan(bulan: int, tahun: int):
    """Mengambil transaksi pemasukan dan pengeluaran untuk bulan tertentu"""
    from datetime import datetime
    data = load_data()
    pemasukan = []
    pengeluaran = []

    for item in data.get("pemasukan", []):
        tanggal_str = item.get("tanggal") or item.get("created_at", "")[:10]
        try:
            dt = datetime.strptime(tanggal_str, "%Y-%m-%d")
        except Exception:
            continue
        if dt.month == bulan and dt.year == tahun:
            pemasukan.append(item)

    for item in data.get("pengeluaran", []):
        tanggal_str = item.get("tanggal") or item.get("created_at", "")[:10]
        try:
            dt = datetime.strptime(tanggal_str, "%Y-%m-%d")
        except Exception:
            continue
        if dt.month == bulan and dt.year == tahun:
            pengeluaran.append(item)

    return pemasukan, pengeluaran

def filter_mingguan(week: int, tahun: int):
    """Mengambil transaksi berdasarkan minggu ke-berapa dalam tahun tertentu"""
    from datetime import datetime
    data = load_data()

    pemasukan = []
    pengeluaran = []

    for item in data.get("pemasukan", []):
        tanggal_str = item.get("tanggal") or item.get("created_at", "")[:10]
        try:
            dt = datetime.strptime(tanggal_str, "%Y-%m-%d")
        except Exception:
            continue
        if dt.isocalendar().week == week and dt.year == tahun:
            pemasukan.append(item)

    for item in data.get("pengeluaran", []):
        tanggal_str = item.get("tanggal") or item.get("created_at", "")[:10]
        try:
            dt = datetime.strptime(tanggal_str, "%Y-%m-%d")
        except Exception:
            continue
        if dt.isocalendar().week == week and dt.year == tahun:
            pengeluaran.append(item)

    return pemasukan, pengeluaran

def laporan_bulanan(bulan: int, tahun: int):
    """Menghasilkan laporan lengkap per bulan"""
    pemasukan, pengeluaran = filter_bulanan(bulan, tahun)

    total_pemasukan = sum(item["jumlah"] for item in pemasukan)
    total_pengeluaran = sum(item["jumlah"] for item in pengeluaran)
    saldo = total_pemasukan - total_pengeluaran

    return {
        "bulan": bulan,
        "tahun": tahun,
        "pemasukan": pemasukan,
        "pengeluaran": pengeluaran,
        "total_pemasukan": total_pemasukan,
        "total_pengeluaran": total_pengeluaran,
        "saldo": saldo,
    }


def laporan_mingguan(week: int, tahun: int):
    """Menghasilkan laporan mingguan"""
    pemasukan, pengeluaran = filter_mingguan(week, tahun)

    total_pemasukan = sum(item["jumlah"] for item in pemasukan)
    total_pengeluaran = sum(item["jumlah"] for item in pengeluaran)
    saldo = total_pemasukan - total_pengeluaran

    return {
        "minggu": week,
        "tahun": tahun,
        "pemasukan": pemasukan,
        "pengeluaran": pengeluaran,
        "total_pemasukan": total_pemasukan,
        "total_pengeluaran": total_pengeluaran,
        "saldo": saldo,
    }


def tampilkan_tabel(data_list):
    """Menampilkan data dalam bentuk tabel sederhana di terminal"""
    if not data_list:
        print("Tidak ada data untuk ditampilkan.")
        return

    print("-" * 50)
    print(f"{'Tanggal':<12} | {'Nama/Deskripsi':<25} | {'Jumlah':<10}")
    print("-" * 50)

    for item in data_list:
        tanggal = item.get("tanggal") or item.get("created_at", "")[:10] or "-"
        nama = item.get("nama") or item.get("catatan") or f"Kategori:{item.get('kategori_id')}" or "-"
        jumlah = item.get("jumlah", 0)
        print(f"{tanggal:<12} | {nama:<25} | {jumlah:<10}")

    print("-" * 50)
