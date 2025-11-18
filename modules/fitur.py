from datetime import datetime
from modules.pemasukan import list_pemasukan
from modules.pengeluaran import list_pengeluaran
from modules.laporan import laporan_bulanan



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
