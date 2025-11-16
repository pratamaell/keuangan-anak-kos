import json
import os
from datetime import datetime

DATA_FILE = "data.json"


def init_data():
    """Buat file json jika belum ada"""
    if not os.path.exists(DATA_FILE):
        data = {
            "kategori": [],
            "pemasukan": [],
            "pengeluaran": []
        }
        save_data(data)


def load_data():
    init_data()
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def next_id(items: list) -> int:
    if not items:
        return 1
    return max(item["id"] for item in items) + 1


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
