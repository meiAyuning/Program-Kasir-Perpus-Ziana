print("==========")
print("Program Kasir Peminjaman Buku")
print("Selamat Datang Di Perpustakaan Ziana")
print("Masukkan identitas anda")
keranjang = []
nama = input('Nama Panjang :')
nik = int(input('NIK :'))
hp = int(input('No.HP/WA :'))
while True:
    menu_pilihan = input(' Masukkan kategori utama 1-4: \n 1.Karya Tulis Ilmiah\n 2.Novel\n 3.Komik\n 4.Buku Pelajaran\n ')
    if menu_pilihan == "1":
        print("==========")
        print("Anda memilih kategori nomor 1 : Menu Karya Tulis Ilmiah")
        print("Pilih Kategori Karya Tulis Ilmiah Anda :")
        kti = ["Skripsi", "Tesis", "Literasi Digital","Kesehatan"]
        while True:
            for a in range(0, len(kti)):
                print(f'{a + 1}.{kti[a]}')
            list_kti = int(input(f"Masukkan menu karya tulis ilmiah yang diinginkan? [1-{len(kti)}] : \n"))
            if list_kti <= len(kti):
                keranjang.append(kti[list_kti-1])
                for b in range(0,len(keranjang)):
                    print(f'{b+1}.{keranjang[b]} ')
                break
            else:
                print("Silakan Masukkan Menu Karya Tulis Ilmiah Yang Benar")
                continue
    elif menu_pilihan == "2":
        print("==========")
        print("Anda memilih kategori nomor 2 : Menu Novel")
        print("Pilih Kategori Novel Anda :")
        novel = ["Dilan 1990 karya Pidi Baiq","Ketika Cinta Bertasbih karya Habiburrahman El Shirazy","Pergi, Bumi, Pulang karya Tereliye ","Filosofi Kopi, Petir, Supernova karya Dee Lestari"]
        while True:
            for c in range(0, len(novel)):
                print(f'{c + 1}.{novel[c]}')
            list_novel = int(input(f"Masukkan menu novel yang diinginkan? [1-{len(novel)}] : \n"))
            if list_novel <= len(novel):
                keranjang.append(novel[list_novel-1])
                for d in range(0,len(keranjang)):
                    print(f'{d+1}.{keranjang[d]} ')
                break
            else:
                print("Silakan Masukkan Menu Novel Yang Benar")
                continue
    elif menu_pilihan == "3":
        print("==========")
        print("Anda memilih kategori nomor 3 : Menu Komik")
        print("Pilih Kategori Komik Anda :")
        komik = ["Doraemon","Naruto","Tin - Tin","Lupus"]
        while True:
            for e in range(0, len(komik)):
                print(f'{e + 1}.{komik[e]}')
            list_komik = int(input(f"Masukkan menu komik yang diinginkan? [1-{len(komik)}] : \n"))
            if list_komik <= len(komik):
                keranjang.append(komik[list_komik-1])
                for f in range(0,len(keranjang)):
                    print(f'{f+1}.{keranjang[f]} ')
                break
            else:
                print("Silakan Masukkan Menu Komik Yang Benar")
                continue
    elif menu_pilihan == "4":
        print("==========")
        print("Anda memilih kategori nomor 4 : Menu Buku Pelajaran")
        print("Pilih Menu Buku Pelajaran Anda :")
        mapel = ["Buku Fisika","Buku Biologi","Buku Kimia","Buku Astronomi"]
        while True:
            for e in range(0, len(mapel)):
                print(f'{e + 1}.{mapel[e]}')
            list_mapel = int(input(f"Masukkan menu buku pelajaran yang diinginkan? [1-{len(mapel)}] : \n"))
            if list_mapel <= len(mapel):
                keranjang.append(mapel[list_mapel-1])
                for f in range(0,len(keranjang)):
                    print(f'{f+1}.{keranjang[f]} ')
                break
            else:
                print("Silakan Masukkan Menu Buku Pelajaran Yang benar")
                continue
    else:
        print("Menu Kategori Tidak Tersedia")
        continue

    validasi_menu = input('Ada buku yang ingin dipinjam lagi ? Y/n\n')
    if validasi_menu == "Y" or validasi_menu == "y":
        print("==========")
        continue
    else:
        print(f'Nama Panjang : {nama}')
        print(f'NIK : {nik}')
        print(f'No.HP/WA : {hp}\n')
        print('Buku yang anda pinjam adalah :')
        for g in range(0,len(keranjang)):
            print(f'{g+1}.{keranjang[g]}')
        print("Terima Kasih Buku Akan Sedang Disiapkan")
        break