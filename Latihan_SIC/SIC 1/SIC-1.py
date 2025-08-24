import os


def menu():
    print("=== SIC 7 part 1 ===")
    print("1. Soal 1")
    print("2. Soal 2")
    print("3. Soal 3")
    print("4. Soal 4")
    print("5. Soal 5")
    print("6. Keluar")

def clear():
    input("Enter untuk kembali ke menu ")
    os.system('cls')

def main():
    while True:
        menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            print("Selamat Datang di Analisis Data Coffee Shop")
            print("Menu Favorit: Ayam Geprek wkwkkwk")
            print("Income Today = 20000")
            clear()
        elif pilihan == "2":
            print("Kopi","Donat","Croissant",sep="-")
            print("Laporan Pendapatan", end=" ")
            print("Sudah Selesai")
            clear()
        elif pilihan == "3":
            if 5000>1000:
                print("Hidup Jokowi")#Hidup juga Nepotismenya
                print("1 Pria lolos SIC stage 1")#19 juta lainnya menunggu lapangan pekerjaan
                clear()
        elif pilihan == "4":
            print("skip, harus error wok")
            clear()
        elif pilihan == "5":
            print("skip, harus error wok")
            clear()
        elif pilihan == "6":
            break
        else:
            print("gada menunya dongo")
            clear()

if __name__ == "__main__":
    main()