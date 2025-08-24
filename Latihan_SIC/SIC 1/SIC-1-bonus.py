# Laporan Pendapatan kafe anti korupsi
import os

data = [
    {"Nama": "donut", "Harga": 5000, "Terjual": 5},
    {"Nama": "kopi", "Harga": 10000, "Terjual": 8},
    {"Nama": "croissant", "Harga": 8000, "Terjual": 4},
    {"Nama": "susu", "Harga": 10000, "Terjual": 4},
    {"Nama": "teh", "Harga": 3000, "Terjual": 6}
]


def format_rupiah(n: int) -> str:
    return "Rp " + f"{n:,.0f}".replace(",", ".")

def pause(prompt="Enter untuk kembali ke menu "):
    input(prompt)

def clear():
    pause()
    os.system('cls')


def menu():
    print("Menu:")
    print("1. Lihat laporan")
    print("2. Manipulasi data laporan")
    print("3. Keluar")


def lihat_laporan():
    produk = 15
    harga = 12
    terjual = 8
    total = 15

    print(f"{'Produk':<{produk}} {'Harga':>{harga}} {'Terjual':>{terjual}} {'Total':>{total}}")
    print("-" * (produk + harga + terjual + total + 3))

    total_pendapatan = 0
    for item in data:
        total_item = item["Harga"] * item["Terjual"]
        total_pendapatan += total_item
        print(
            f"{item['Nama']:<{produk}} "
            f"{format_rupiah(item['Harga']):>{harga}} "
            f"{item['Terjual']:>{terjual}} "
            f"{format_rupiah(total_item):>{total}}"
        )

    print("-" * (produk + harga + terjual + total + 3))
    label_total = "TOTAL PENDAPATAN"
    print(f"{label_total:<{produk + harga + terjual}} {format_rupiah(total_pendapatan):>{total}}")


def input_angka(prompt: str, allow_zero_as_back=False) -> int | None:

    while True:
        val = input(prompt).strip()
        if val == "":
            print("Input tidak boleh kosong.")
            continue
        if allow_zero_as_back and val == "0":
            return None
        if not val.isdigit():
            print("Harus angka bulat. Coba lagi.")
            continue
        angka = int(val)
        if angka < 0:
            print("Tidak boleh negatif. Coba lagi.")
            continue
        return angka

def pilih_produk() -> int | None:
    while True:
        print("\nPilih produk yang ingin diubah:")
        for i, item in enumerate(data, start=1):
            print(f"{i}. {item['Nama']} ({format_rupiah(item['Harga'])}, terjual {item['Terjual']})")
        print("0. Kembali")

        pilihan = input("Masukkan nomor: ").strip()
        if pilihan == "0":
            return None
        if pilihan.isdigit():
            idx = int(pilihan) - 1
            if 0 <= idx < len(data):
                return idx
        print("Pilihan tidak valid. Coba lagi.")

def menu_edit_bidang(nama_produk: str) -> str | None:
    while True:
        print(f"\nProduk: {nama_produk}")
        print("Apa yang ingin diubah?")
        print("1. Nama")
        print("2. Harga")
        print("0. Kembali")
        pilihan = input("Masukkan pilihan: ").strip()
        if pilihan == "0":
            return None
        if pilihan == "1":
            return "nama"
        if pilihan == "2":
            return "harga"
        print("Pilihan tidak valid. Coba lagi.")



def edit_data():
    while True:
        idx = pilih_produk()
        if idx is None:
            return

        item = data[idx]
        while True:
            bidang = menu_edit_bidang(item["Nama"])
            if bidang is None:  
                break

            if bidang == "nama":
                print("\nUbah Nama (kosongkan untuk cancel):")
                new_name = input("Nama baru: ").strip()
                if new_name == "":
                    print("Dibatalkan. Nama tidak diubah.")
                    continue
                lama = item["Nama"]
                item["Nama"] = new_name
                print(f"Berhasil: Nama '{lama}' diubah menjadi '{new_name}'.")
            elif bidang == "harga":
                print("\nUbah Harga (0 untuk kembali):")
                angka = input_angka("Harga baru (Rp): ", allow_zero_as_back=True)
                if angka is None:
                    print("Dibatalkan. Harga tidak diubah.")
                    continue
                lama = item["Harga"]
                item["Harga"] = angka
                print(f"Berhasil: Harga {format_rupiah(lama)} diubah menjadi {format_rupiah(angka)}.")

            while True:
                lanjut = input("Edit bidang lain untuk produk ini? (y/n): ").strip().lower()
                if lanjut in ("y", "n"):
                    break
                print("Jawab 'y' atau 'n'.")
            if lanjut == "n":
                break

def main():
    while True:
        menu()
        pilihan = input("Pilih menu (1-3): ").strip()

        if pilihan == "1":
            lihat_laporan()
            clear()
        elif pilihan == "2":
            edit_data()
            clear()
        elif pilihan == "3":
            print("Sampai jumpa!")
            break
        else:
            print("Menu tidak tersedia.")
            clear()

if __name__ == "__main__":
    main()
