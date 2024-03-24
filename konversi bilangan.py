def biner_ke_desimal(biner):
    return int(biner, 2)

def oktal_ke_desimal(oktal):
    return int(oktal, 8)

def heksa_ke_desimal(heksa):
    return int(heksa, 16)

def desimal_ke_biner(desimal):
    return bin(desimal)[2:]

def desimal_ke_oktal(desimal):
    return oct(desimal)[2:]

def desimal_ke_heksa(desimal):
    return hex(desimal)[2:]

def main():
    while True:
        print("\nPilih jenis konversi:")
        print("1. Biner ke Desimal")
        print("2. Oktal ke Desimal")
        print("3. Heksadesimal ke Desimal")
        print("4. Desimal ke Biner")
        print("5. Desimal ke Oktal")
        print("6. Desimal ke Heksadesimal")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '0':
            print("Terima kasih!")
            break
        elif pilihan == '1':
            bilangan_biner = input("Masukkan bilangan biner: ")
            print("Hasil konversi:", biner_ke_desimal(bilangan_biner))
        elif pilihan == '2':
            bilangan_oktal = input("Masukkan bilangan oktal: ")
            print("Hasil konversi:", oktal_ke_desimal(bilangan_oktal))
        elif pilihan == '3':
            bilangan_heksa = input("Masukkan bilangan heksadesimal: ")
            print("Hasil konversi:", heksa_ke_desimal(bilangan_heksa))
        elif pilihan == '4':
            bilangan_desimal = int(input("Masukkan bilangan desimal: "))
            print("Hasil konversi:", desimal_ke_biner(bilangan_desimal))
        elif pilihan == '5':
            bilangan_desimal = int(input("Masukkan bilangan desimal: "))
            print("Hasil konversi:", desimal_ke_oktal(bilangan_desimal))
        elif pilihan == '6':
            bilangan_desimal = int(input("Masukkan bilangan desimal: "))
            print("Hasil konversi:", desimal_ke_heksa(bilangan_desimal))
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
