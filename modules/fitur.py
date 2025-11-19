from datetime import datetime
import csv
import os

from modules.pemasukan import list_pemasukan
from modules.pengeluaran import list_pengeluaran
from modules.laporan import laporan_bulanan


def export_laporan_txt_csv(bulan, tahun, base_filename="laporan"):
    laporan = laporan_bulanan(bulan, tahun)
    txt_path = f"{base_filename}_{bulan:02d}_{tahun}.txt"
    csv_path = f"{base_filename}_{bulan:02d}_{tahun}.csv"

    # TXT
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"LAPORAN BULANAN {bulan}/{tahun}\n\n")
        f.write("PEMASUKAN\n")
        for p in laporan["pemasukan"]:
            f.write(f"{p.get('id')} | {p.get('tanggal','-')} | Rp{p.get('jumlah')} | {p.get('catatan','')}\n")
        f.write(f"Total Pemasukan: Rp{laporan['total_pemasukan']}\n\n")

        f.write("PENGELUARAN\n")
        for p in laporan["pengeluaran"]:
            f.write(f"{p.get('id')} | {p.get('tanggal','-')} | Rp{p.get('jumlah')} | {p.get('catatan','')}\n")
        f.write(f"Total Pengeluaran: Rp{laporan['total_pengeluaran']}\n\n")
        f.write(f"Saldo: Rp{laporan['saldo']}\n")

    # CSV (gabung pemasukan & pengeluaran dengan kolom type)
    with open(csv_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["type","id","tanggal","jumlah","kategori_id","catatan"])
        for p in laporan["pemasukan"]:
            writer.writerow(["pemasukan", p.get("id"), p.get("tanggal",""), p.get("jumlah"), p.get("kategori_id"), p.get("catatan","")])
        for p in laporan["pengeluaran"]:
            writer.writerow(["pengeluaran", p.get("id"), p.get("tanggal",""), p.get("jumlah"), p.get("kategori_id"), p.get("catatan","")])

    return txt_path, csv_path

def budget_alert_monthly(limit, bulan=None, tahun=None):
    now = datetime.now()
    bulan = bulan or now.month
    tahun = tahun or now.year
    laporan = laporan_bulanan(bulan, tahun)
    pengeluaran = laporan.get("total_pengeluaran", 0)
    if pengeluaran > limit:
        return f"ALERT: Pengeluaran bulan {bulan}/{tahun} Rp{pengeluaran} melebihi limit Rp{limit}"
    else:
        sisa = limit - pengeluaran
        return f"Aman: Pengeluaran Rp{pengeluaran}. Sisa anggaran Rp{sisa}"



def cari_transaksi(query):
    q = str(query).lower()
    results = []
    for it in list_pemasukan():
        if q in str(it.get("catatan","")).lower() or q == str(it.get("id")):
            r = it.copy()
            r["type"] = "Pemasukan"
            results.append(r)
    for it in list_pengeluaran():
        if q in str(it.get("catatan","")).lower() or q == str(it.get("id")):
            r = it.copy()
            r["type"] = "Pengeluaran"
            results.append(r)
    return results

def sort_transaksi(by="tanggal", reverse=False):
    """
    Gabungkan pemasukan & pengeluaran lalu urutkan.
    by: 'tanggal', 'jumlah', 'kategori_id', 'id', atau 'type'
    reverse: True untuk descending
    """
    items = []
    for it in list_pemasukan():
        r = it.copy()
        r["type"] = "Pemasukan"
        items.append(r)
    for it in list_pengeluaran():
        r = it.copy()
        r["type"] = "Pengeluaran"
        items.append(r)

    def key_fn(x):
        v = x.get(by) if by in x or by == "type" else x.get(by)
        if by == "tanggal":
            try:
                return datetime.strptime(str(v), "%Y-%m-%d")
            except Exception:
                # tempatkan tanggal tidak valid di akhir (atau awal jika reverse)
                return datetime.max if not reverse else datetime.min
        if by in ("jumlah", "kategori_id", "id"):
            try:
                return int(v)
            except Exception:
                return float("inf") if not reverse else -float("inf")
        return str(v).lower() if v is not None else ""
    return sorted(items, key=key_fn, reverse=reverse)
