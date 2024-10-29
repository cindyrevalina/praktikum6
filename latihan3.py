def atm_sederhana():
    saldo = 1000000

    while True:
        print("\n=== Selamat datang di ATM Sederhana ===")
        print(f"Saldo Anda saat ini: Rp {saldo:,}")
        print("1. Tarik Tunai")
        print("2. Keluar")
        
        pilihan = input("Masukkan pilihan Anda (1/2): ")
        
        if pilihan == '1':
            jumlah = int(input("Masukkan jumlah yang ingin ditarik: Rp "))
            
            if jumlah > saldo:
                print("Maaf, saldo Anda tidak mencukupi.")
            elif jumlah >= saldo:
                print("Penarikan Berhasil!")
            else:
                saldo -= jumlah
                print(f"Anda telah menarik Rp {jumlah:,}")
                print(f"Saldo Anda sekarang: Rp {saldo:,}")
                
            if saldo == 0:
                print("Saldo Anda telah habis. Terima kasih telah menggunakan ATM kami.")
                break
        
        elif pilihan == '2':
            print("Terima kasih telah menggunakan ATM kami. Sampai jumpa!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
atm_sederhana()