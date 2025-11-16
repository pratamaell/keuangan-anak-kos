from typing import Optional, List
from .utils import load_data, save_data, next_id, now


def list_pemasukan() -> List[dict]:
    data = load_data()
    return data["pemasukan"]


def add_pemasukan(jumlah: int, kategori_id: int, catatan: str = "", tanggal: str = None) -> dict:
    data = load_data()

    item = {
        "id": next_id(data["pemasukan"]),
        "jumlah": jumlah,
        "kategori_id": kategori_id,
        "catatan": catatan,
        "tanggal": tanggal if tanggal else now()[:10],   # ✅ YYYY-MM-DD
        "created_at": now()
    }

    data["pemasukan"].append(item)
    save_data(data)
    return item


def get_pemasukan(id_item: int) -> Optional[dict]:
    data = load_data()
    for p in data["pemasukan"]:
        if p["id"] == id_item:
            return p
    return None


def update_pemasukan(
    id_item: int,
    jumlah: int = None,
    kategori_id: int = None,
    catatan: str = None,
    tanggal: str = None
):
    data = load_data()

    for p in data["pemasukan"]:
        if p["id"] == id_item:
            if jumlah is not None:
                p["jumlah"] = jumlah
            if kategori_id is not None:
                p["kategori_id"] = kategori_id
            if catatan is not None:
                p["catatan"] = catatan
            if tanggal is not None:
                p["tanggal"] = tanggal   # ✅ update tanggal

            save_data(data)
            return p

    raise ValueError("Data pemasukan tidak ditemukan")


def delete_pemasukan(id_item: int) -> bool:
    data = load_data()
    for i, p in enumerate(data["pemasukan"]):
        if p["id"] == id_item:
            data["pemasukan"].pop(i)
            save_data(data)
            return True

    raise ValueError("Data pemasukan tidak ditemukan")
