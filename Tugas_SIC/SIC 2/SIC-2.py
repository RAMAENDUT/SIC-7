import os

nama_produk = ["Kopi Pagi", "Roti Cokelat"]
harga_produk = [18000.5, 10000]
stock_roti = True
Jumlah_kopi_str = "0"
Jumlah_roti_str = "0"
Jumlah_kopi_int = 0
Jumlah_roti_int = 0
Harga_kopi = 0
Harga_roti = 0
Total_belanja = 0
uang_bayar = 50000


def menu():
    print("1. Soal 1")
    print("2. Soal 2")
    print("3. Soal 3")
    print("4. Soal 4")
    print("5. Keluar")

def soal_1():
    print("Nama Produk 1            : ", nama_produk[0])
    print("Harga Produk 1           : ", harga_produk[0])
    print("Nama Produk 2            : ", nama_produk[1])
    print("Harga Produk 2           : ", harga_produk[1])
    print("Status ketersediaan roti : ", stock_roti)

def soal_2():
    global Jumlah_kopi_str, Jumlah_roti_str, Jumlah_kopi_int, Jumlah_roti_int
    print("Masukkan jumlah pesanan kopi")
    Jumlah_kopi_str = input("Jumlah pesanan kopi: ")

    print("Masukkan jumlah pesanan roti")
    Jumlah_roti_str = input("Jumlah pesanan roti: ")

    print("Jumlah pesanan kopi: ", Jumlah_kopi_str)
    print("Jumlah pesanan roti: ", Jumlah_roti_str, "\n")

    Jumlah_kopi_int = int(Jumlah_kopi_str)
    Jumlah_roti_int = int(Jumlah_roti_str)

    print("Tipe data awal jumlah kopi: ", type(Jumlah_kopi_str))
    print("Tipe data awal jumlah roti: ", type(Jumlah_roti_str), "\n")
    print("Tipe data awal jumlah kopi: ", type(Jumlah_kopi_int))
    print("Tipe data awal jumlah roti: ", type(Jumlah_roti_int))

def soal_3():
    global Harga_kopi, Harga_roti, Total_belanja, uang_bayar
    Harga_kopi = harga_produk[0] * Jumlah_kopi_int
    Harga_roti = harga_produk[1] * Jumlah_roti_int
    Total_belanja = Harga_kopi + Harga_roti
    print(Harga_kopi, " + ", Harga_roti, " = ", Total_belanja)
    print(uang_bayar, " - ", Total_belanja, " = ", uang_bayar - Total_belanja)
    print("kembalian yang diterima adalah Rp", uang_bayar - Total_belanja)

def soal_4():
    global Harga_kopi, Harga_roti, Total_belanja
    Nama_pelanggan = input("Masukkan nama lu: ")
    Pesan_terima_kasih = "Terima kasih " + Nama_pelanggan + " telah berbelanja di coffee shop sedih "
    print("*" * 25, "\n")
    print(Pesan_terima_kasih, "\n")
    print("*" * 25, "\n")
    print("Total harga kopi pagi: Rp", Harga_kopi)
    print("Total harga roti cokelat: Rp", Harga_roti)
    print("Total belanja: Rp", Total_belanja)

def main():
    while True:
        menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            soal_1()
        elif pilihan == "2":
            soal_2()
        elif pilihan == "3":
            soal_3()
        elif pilihan == "4":
            soal_4()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
        
        input("Enter untuk lanjut")
        os.system('cls')
if __name__ == "__main__":
    main()