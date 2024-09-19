import pyinputplus as pyip
from tabulate import tabulate

# Menu Definitions
menu = ['1. Tampilkan Daftar Mobil',
        '2. Tambahkan Daftar Mobil',
        '3. Hapus Daftar Mobil',
        '4. Ubah Daftar Mobil',
        '5. Keluar']

read_menu = ['1. Tampilkan Seluruh Daftar Mobil',
             '2. Tampilkan Daftar Mobil Berdasarkan ID',
             '3. Tampilkan Daftar Mobil Berdasarkan Status Pengembalian',
             '4. Kembali ke Menu Utama']

create_menu = ['1. Tambah Data Mobil',
               '2. Kembali ke Menu Utama']

delete_menu = ['1. Hapus Data Mobil Berdasarkan ID',
               '2. Hapus Seluruh Data Mobil',
               '3. Kembali ke Menu Utama']

update_menu = ['1. Ubah Data Mobil Secara Keseluruhan',
               '2. Ubah Hanya Kategori Tertentu',
               '3. Kembali ke Menu Utama']

jenis_MPV = ['Toyota Innova', 'Wuling Confero', 'Toyota Avanza']
jenis_SUV = ['Mitsubishi Pajero', 'Toyota Fortuner', 'Honda CRV']

data_mobil = [
    {'rentId': 'TOIN0509', 'jenis_mobil': 'MPV', 'merk': 'Toyota Innova', 'rentDate': "05/09/2024", 'rentalPrice': 350000, 'returned': 'Belum dikembalikan'},
    {'rentId': 'TOAV0609', 'jenis_mobil': 'MPV', 'merk': 'Toyota Avanza', 'rentDate': '06/09/2024', 'rentalPrice': 500000, 'returned': 'Belum dikembalikan'},
    {'rentId': 'MIPA0209', 'jenis_mobil': 'SUV', 'merk': 'Mitsubishi Pajero', 'rentDate': '02/09/2024', 'rentalPrice': 700000, 'returned': 'Sudah dikembalikan'},
    {'rentId': 'HOCR0309', 'jenis_mobil': 'SUV', 'merk': 'Honda CRV', 'rentDate': '03/09/2024', 'rentalPrice': 330000, 'returned': 'Belum dikembalikan'},
    {'rentId': 'WUCO1009', 'jenis_mobil': 'MPV', 'merk': 'Wuling Confero', 'rentDate': '10/09/2024', 'rentalPrice': 350000, 'returned': 'Belum dikembalikan'}
]

headers = ["Rental ID", "Jenis Mobil", "Merek", "Tanggal Rental", "Harga Rental", "Status Pengembalian"]

# Helper function to generate the table
def generate_table(data):
    return tabulate([(mobil['rentId'], mobil['jenis_mobil'], mobil['merk'], mobil['rentDate'], mobil['rentalPrice'], mobil['returned']) for mobil in data], headers, tablefmt='grid')

# function to read data
def read_data():
    while True:
        print("="*55)
        print("     Sub Menu Read Data Daud's Family Car Rentals     ")
        print("="*55)
        for i in read_menu:
            print(i)
        read = pyip.inputNum(prompt="\nSilahkan pilih Sub Menu Read Data [1-4]: ", min=1, max=4)
        if read == 1:
            print("\nBerikut merupakan seluruh daftar mobil yang tersedia :\n{}".format(generate_table(data_mobil)))
        elif read == 2:
            print(generate_table(data_mobil))
            rentId_choice = pyip.inputMenu(prompt="Masukkan Rental ID yang ingin dilihat:\n", choices=[mobil['rentId'] for mobil in data_mobil], numbered=True)
            filtered_mobil = [mobil for mobil in data_mobil if mobil['rentId'] == rentId_choice]
            if filtered_mobil:
                filtered_table = generate_table(filtered_mobil)
                print("\nBerikut merupakan detail mobil dengan Rental ID {}:\n{}".format(rentId_choice, filtered_table))
        elif read == 3:
            status_choice = pyip.inputMenu(prompt="\nTampilkan mobil berdasarkan status pengembalian:\n", choices=['Belum dikembalikan', 'Sudah dikembalikan'], numbered=True)
            filtered_by_status = [mobil for mobil in data_mobil if mobil['returned'] == status_choice]
            if filtered_by_status:
                print("\nMobil dengan status {}:\n{}".format(status_choice, generate_table(filtered_by_status)))
            else:
                print("\nTidak ada mobil dengan status {}.".format(status_choice))
        else:
            return  # Hentikan fungsi dan kembali ke menu utama

# function to create data
def create_data():
    while True:
        print("="*55)
        print("     Sub Menu Create Data Daud's Family Car Rentals     ")
        print("="*55)
        for i in create_menu:
            print(i)
        create = pyip.inputNum(prompt="\nSilahkan pilih Sub Menu Create Data [1-2]: ", min=1, max=2)
        if create == 1:
            addJenis = pyip.inputMenu(prompt="Masukkan jenis mobil :\n", choices=['MPV', 'SUV'], numbered=True)
            if addJenis == 'MPV':
                addMerk = pyip.inputMenu(prompt="Masukkan merk mobil :\n", choices=jenis_MPV, numbered=True)
            else:
                addMerk = pyip.inputMenu(prompt="Masukkan merk mobil :\n", choices=jenis_SUV, numbered=True)
            addDate = pyip.inputDate(prompt="Masukkan tanggal rental (dd/mm/yyyy): ", formats=['%d/%m/%Y'])
            addHarga = pyip.inputNum(prompt="Masukkan harga sewa harian [300000-1000000]: ", min=300000, max=1000000)
            addReturned = 'Belum dikembalikan'
            addRentId = ''.join([word[:2].upper() for word in addMerk.split()]) + addDate.strftime("%d%m")
            data_mobil.append({'rentId': addRentId, 'jenis_mobil': addJenis, 'merk': addMerk, 'rentDate': addDate.strftime('%d/%m/%Y'), 'rentalPrice': addHarga, 'returned': addReturned})
            print("\nMobil baru berhasil ditambahkan ke daftar!")
            print(generate_table(data_mobil))
        else:
            return  # Hentikan fungsi dan kembali ke menu utama

# function to delete data
def delete_data():
    while True:
        print("="*55)
        print("     Sub Menu Delete Data Daud's Family Car Rentals     ")
        print("="*55)
        for i in delete_menu:
            print(i)
        delete = pyip.inputNum(prompt="\nSilahkan pilih Sub Menu Delete Data [1-3]: ", min=1, max=3)
        if delete == 1:
            print(generate_table(data_mobil))
            deleteRentId = pyip.inputMenu(prompt="Masukkan Rental ID yang akan dihapus:\n", choices=[mobil['rentId'] for mobil in data_mobil], numbered=True)
            deleteValidation = pyip.inputChoice(prompt="Yakin untuk menghapus mobil? [Y/N] ", choices=['Y', 'N']).upper()
            if deleteValidation == 'Y':
                data_mobil[:] = [mobil for mobil in data_mobil if mobil['rentId'] != deleteRentId]
                print("\nMobil berhasil dihapus dari daftar!")
                print(generate_table(data_mobil))
            else:
                print("\nPenghapusan mobil dibatalkan!")
        elif delete == 2:
            deleteAllValidation = pyip.inputChoice(prompt="Yakin untuk menghapus semua mobil? [Y/N] ", choices=['Y', 'N']).upper()
            if deleteAllValidation == 'Y':
                data_mobil.clear()  # Hapus semua data mobil
                print("\nSemua mobil berhasil dihapus dari daftar!")
                print(generate_table(data_mobil))
            else:
                print("\nPenghapusan semua mobil dibatalkan!")
        else:
            return  # Hentikan fungsi dan kembali ke menu utama

# function to update data
def update_data():
    while True:
        print("="*55)
        print("     Sub Menu Update Data Daud's Family Car Rentals     ")
        print("="*55)
        for i in update_menu:
            print(i)
        update = pyip.inputNum("\nSilahkan pilih Sub Menu Update Data [1-3]: ", min=1, max=3)
        if update == 1:
            print(generate_table(data_mobil))
            changeRentId = pyip.inputMenu(prompt="Masukkan Rental ID yang akan diubah:\n", choices=[mobil['rentId'] for mobil in data_mobil], numbered=True)
            for mobil in data_mobil:
                if mobil['rentId'] == changeRentId:
                    updateJenis = pyip.inputMenu(prompt="Masukkan jenis mobil baru :\n", choices=['MPV', 'SUV'], numbered=True)
                    if updateJenis == 'MPV':
                        updateMerk = pyip.inputMenu(prompt="Masukkan merek mobil baru :\n", choices=jenis_MPV, numbered=True)
                    else:
                        updateMerk = pyip.inputMenu(prompt="Masukkan merek mobil baru :\n", choices=jenis_SUV, numbered=True)
                    updateDate = pyip.inputDate(prompt="Masukkan tanggal rental baru (dd/mm/yyyy): ", formats=['%d/%m/%Y'])
                    updateHarga = pyip.inputNum(prompt="Masukkan harga rental harian baru [300000-1000000]: ", min=300000, max=1000000)
                    updateReturned = pyip.inputMenu(prompt="Masukkan status pengembalian baru :\n", choices=['Belum dikembalikan', 'Sudah dikembalikan'], numbered=True)
                    mobil.update({'jenis_mobil': updateJenis, 'merk': updateMerk, 'rentDate': updateDate.strftime('%d/%m/%Y'), 'rentalPrice': updateHarga, 'returned': updateReturned})
                    print("\nData mobil berhasil diubah!")
                    print(generate_table(data_mobil))
                    break
        elif update == 2:
            print(generate_table(data_mobil))
            changeRentId = pyip.inputMenu(prompt="Masukkan Rental ID yang akan diubah:\n", choices=[mobil['rentId'] for mobil in data_mobil], numbered=True)
            for mobil in data_mobil:
                if mobil['rentId'] == changeRentId:
                    field = pyip.inputMenu(prompt="Pilih kategori yang ingin diubah:\n", choices=["Jenis Mobil", "Merek", "Tanggal Rental", "Harga Rental", "Status Pengembalian"], numbered=True)
                    if field == "Jenis Mobil":
                        updateJenis = pyip.inputMenu(prompt="Masukkan jenis mobil baru :\n", choices=['MPV', 'SUV'], numbered=True)
                        if updateJenis == 'MPV':
                            updateMerk = pyip.inputMenu(prompt="Masukkan merek mobil baru :\n", choices=jenis_MPV, numbered=True)
                        else:
                            updateMerk = pyip.inputMenu(prompt="Masukkan merek mobil baru :\n", choices=jenis_SUV, numbered=True)
                        mobil.update({'jenis_mobil': updateJenis, 'merk': updateMerk})
                    elif field == "Merek":
                        updateMerk = pyip.inputMenu(prompt="Masukkan merek mobil baru :\n", choices=jenis_MPV if mobil['jenis_mobil'] == 'MPV' else jenis_SUV, numbered=True)
                        mobil.update({'merk': updateMerk})
                    elif field == "Tanggal Rental":
                        updateDate = pyip.inputDate(prompt="Masukkan tanggal rental baru (dd/mm/yyyy): ", formats=['%d/%m/%Y'])
                        mobil.update({'rentDate': updateDate.strftime('%d/%m/%Y')})
                    elif field == "Harga Rental":
                        updateHarga = pyip.inputNum(prompt="Masukkan harga rental harian baru [300000-1000000]: ", min=300000, max=1000000)
                        mobil.update({'rentalPrice': updateHarga})
                    elif field == "Status Pengembalian":
                        updateReturned = pyip.inputMenu(prompt="Masukkan status pengembalian baru :\n", choices=['Belum dikembalikan', 'Sudah dikembalikan'], numbered=True)
                        mobil.update({'returned': updateReturned})
                    print("\nData mobil berhasil diubah!")
                    print(generate_table(data_mobil))
                    break
        else:
            return  # Hentikan fungsi dan kembali ke menu utama

### Main Menu Function ###
def mainMenu():
    while True:
        print("="*55)
        print("          Menu Utama Daud's Family Car Rental     ")
        print("="*55)
        for i in menu:
            print(i)
        pilihan = pyip.inputNum("\nSilahkan pilih Menu Utama [1-5]: ", min=1, max=5)
        if pilihan == 1:
            read_data()
        elif pilihan == 2:
            create_data()
        elif pilihan == 3:
            delete_data()
        elif pilihan == 4:
            update_data()
        else:
            print("Terima Kasih Sudah Menggunakan Program Daud's Family Car Rental.")
            break
    print("Program Selesai")

# Run the main menu
mainMenu()
