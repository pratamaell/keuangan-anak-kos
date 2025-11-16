from typing import Optional, List
from .utils import load_data, save_data, next_id, now


def list_kategori() -> List[dict]:
    data = load_data()
    return data["kategori"]


def add_kategori(nama: str, deskripsi: str = "") -> dict:
    data = load_data()

    if not nama.strip():
        raise ValueError("Nama kategori tidak boleh kosong")

    # Cek duplikat
    for k in data["kategori"]:
        if k["nama"].lower() == nama.lower():
            raise ValueError("Kategori sudah ada")

    new_item = {
        "id": next_id(data["kategori"]),
        "nama": nama,
        "deskripsi": deskripsi,
        "created_at": now()
    }

    data["kategori"].append(new_item)
    save_data(data)
    return new_item


def get_kategori(id_kategori: int) -> Optional[dict]:
    data = load_data()
    for k in data["kategori"]:
        if k["id"] == id_kategori:
            return k
    return None


def update_kategori(id_kategori: int, nama: str = None, deskripsi: str = None):
    data = load_data()

    for k in data["kategori"]:
        if k["id"] == id_kategori:

            if nama is not None:
                if not nama.strip():
                    raise ValueError("Nama tidak boleh kosong")
                k["nama"] = nama.strip()

            if deskripsi is not None:
                k["deskripsi"] = deskripsi

            save_data(data)
            return k

    raise ValueError("Kategori tidak ditemukan")


def delete_kategori(id_kategori: int) -> bool:
    data = load_data()

    for i, k in enumerate(data["kategori"]):
        if k["id"] == id_kategori:
            data["kategori"].pop(i)
            save_data(data)
            return True

    raise ValueError("Kategori tidak ditemukan")
