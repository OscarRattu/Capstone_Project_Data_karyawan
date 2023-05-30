

listkaryawan = [
    {   'NIK' : '23001',
        'Nama' : 'Cecep Gorbancep',
        'Posisi' : 'data science',
        'Usia' : 28,
        'Gender' : 'L',
        'Alamat' : 'Jl. Sukamulya no.52'
    },
    
    {   'NIK' : '23002',
        'Nama' : 'Samsudin si udin',
        'Posisi' : 'Office Boy',
        'Usia' : 23,
        'Gender' : 'L',
        'Alamat' : 'Jl. Dago Pakar II no.31'
    },

    {   'NIK' : '23003',
        'Nama' : 'Ayu Serayu',
        'Posisi' : 'Sekretaris',
        'Usia' : 28,
        'Gender' : 'P',
        'Alamat' : 'Jl. Cihampelas no.231'
    },
    {   'NIK' : '23004',
        'Nama' : 'Kari Ayam',
        'Posisi' : 'Security',
        'Usia' : 27,
        'Gender' : 'L',
        'Alamat' : 'Jl. Setra Duta IV no.46'
    }]


def datakaryawan():
    print('List Data Karyawan : ')
    for j, i in enumerate (listkaryawan):
        print(f"{j+1}|{i['NIK'] :<7}|{i['Nama']:<25}|{i['Posisi']: <20}|{i['Usia'] :<5}|{i['Gender'] :<5}|{i['Alamat'] :<60}")



def main_menu():
        print('''
=====================================================================================
MENU :
1. Tampilkan dan cari data karyawan
2. Masukkan data karyawan baru
3. Update data karyawan
4. Hapus data karyawan
5. Sorting data karyawan
6. keluar program
=====================================================================================
''')
        
        pilihanmenu = input('Pilih menu yang akan dijalankan [1-6] : ')

        if pilihanmenu == '1':
            lihat_cari()
        elif pilihanmenu == '2' :
            masuk()
        elif pilihanmenu == '3' :
            update()
        elif pilihanmenu == '4' :
            hapus()
        elif pilihanmenu == '5':
            sortingkaryawan()
        elif pilihanmenu == '6' :
            print('Terima Kasih sudah mengakses program ini')
            exit()
        else :
            main_menu()


# menu 1
def lihat_cari():
    while True :
        print('''
=====================================================================================
MENU lihat list dan cari data karyawan :
1. Tampilkan data karyawan
2. Cari data karyawan
3. kembali ke menu utama
=====================================================================================
''')
        submenulihat = input('Pilih program yang akan dijalankan : ')

        if submenulihat == '1':
            datakaryawan()
                
        elif submenulihat == '2':
            if len(listkaryawan) == 0:
                print('Data karyawan tidak tersedia!!!')

            elif len(listkaryawan) != 0:
                datakaryawan()
                NIK_karyawan = input('Masukkan NIK karyawan yang dicari (lima digit) : ')
                for i in range (len(listkaryawan)):
                    if NIK_karyawan == listkaryawan[i]['NIK']:
                        print()
                        print('Data karyawan berhasil ditemukan')
                        print(f"NIk : {listkaryawan[i]['NIK']}, Nama : {listkaryawan[i]['Nama']}, Posisi : {listkaryawan[i]['Posisi']}, Usia : {listkaryawan[i]['Usia']}, Gender : {listkaryawan[i]['Gender']}, , Alamat : {listkaryawan[i]['Alamat']} ")
                        break
                else:
                    print(f'Data karyawan {NIK_karyawan} tidak dapat ditemukan')

           
        elif submenulihat == '3':
                main_menu()        
        else :
            print('Pilih menu program yang tepat')
           

    
# Menu 2
def masuk ():
    while True:
        print('''
=====================================================================================
MENU tambah data karyawan :
1. Tambah Data Karyawan
2. kembali ke menu utama
=====================================================================================
''')
        submenumasuk = input('Pilih program yang akan dijalankan : ')
        if submenumasuk == '1':
            NIK_karyawan_baru = input('Masukkan NIK karyawan (lima digit) : ')
            if len(NIK_karyawan_baru) != 5:
                print('NIK yang anda input tidak boleh kurang/lebih dari 5 digit')
            elif len(NIK_karyawan_baru) == 5:
                for i in listkaryawan :
                    if NIK_karyawan_baru == i['NIK'] :
                        print('NIK yang di input sudah terpakai')
                        masuk()
                        
                else:
                    namabaru = input('Masukkan nama karyawan : ').capitalize()
                    posisibaru = input('Masukkan posisi karyawan : ').capitalize()
                    usiabaru = input ('Masukkan usia karyawan : ')
                    genderbaru = input('Masukkan Gender karyawan : ').capitalize()
                    alamatbaru = input('Masukkan alamat karyawan : ')
            
                    konfirmasi_input = input('Apakah data akan disimpan (Y/N) : ').capitalize()
                        
                    if konfirmasi_input == 'Y':
                        databaru = ({
                            'NIK': NIK_karyawan_baru, 
                            'Nama': namabaru, 
                            'Posisi': posisibaru, 
                            'Usia': usiabaru, 
                            'Gender': genderbaru,
                            'Alamat': alamatbaru})
                        
                        listkaryawan.append(databaru)
                       
                        datakaryawan()
                        print('Data baru karyawan berhasil disimpan')
                        masuk()
                        break
                

                    elif konfirmasi_input == 'N':
                        print('Data karyawan tidak jadi disimpan')
                                
                    else :
                        print('masukkan hanya Y/N saja')
                                   

        elif submenumasuk == '2':
            main_menu()
        else:
           print('Masukkan pilihan dengan benar')


# menu 3   
def update():
    while True:
        print('''
=====================================================================================
MENU ubah data karyawan :
1. Ubah Data Karyawan
2. kembali ke menu utama
=====================================================================================
''')
        submenuupdate = input('Pilih program yang akan dijalankan : ')

        if submenuupdate == '1':
            datakaryawan() 
            inputNIK = input('masukkan NIK karyawan : ')
            for i in range (len(listkaryawan)) :
                if inputNIK == listkaryawan [i]['NIK']:
                    print('Data karyawan ditemukan')
                    ganti = input('Apakah anda ingin melakukan update (Y/N) : ').capitalize()
                    if ganti == 'Y':

                        updateketerangan = input ('''
                         pilih data informasi yang ingin anda update :
                         1. Nomor Induk Karyawan
                         2. Nama Karyawan
                         3. Posisi karyawan
                         4. Usia karyawan
                         5. Gender karyawan
                         6. Alamat karyawan 
                         
                         Masukkan pilihan yang akan dilakukan :''')
                        
                        if updateketerangan == '1':
                            nikkaryawanbaru = input('Masukkan NIK karyawan (lima digit) : ')
                            kondisinew = input('Apakah anda ingin rubah data karyawan (Y/N) : ').capitalize() 
                            if kondisinew == 'Y':
                                listkaryawan[i]['NIK'] = nikkaryawanbaru
                                datakaryawan()
                                print('Data karyawan "berhasil" dirubah')
                            elif kondisinew == 'N':
                                print('Data karyawan tidak jadi dirubah')
                                update()
                            else:
                                print('masukkan pilihan yang benar')
                                break

                        elif updateketerangan == '2':
                            newnama = input('Masukkan nama karyawan yang baru : ')
                            kondisinew = input('Apakah anda ingin rubah data karyawan (Y/N) : ').capitalize()
                            if kondisinew == 'Y':
                                listkaryawan[i]['Nama'] = newnama
                                datakaryawan()
                                print('Data karyawan "berhasil" dirubah')
                            elif kondisinew == 'N':
                                print('Data karyawan tidak jadi dirubah')
                                update()
                            else:
                                print('masukkan pilihan yang benar')
                                break
                        
                        elif updateketerangan == '3':
                            newposisi = input('Masukkan posisi karyawan yang baru : ')
                            kondisinew = input('Apakah anda ingin rubah data karyawan (Y/N) : ').capitalize()
                            if kondisinew == 'Y':
                                listkaryawan[i]['Posisi'] = newposisi
                                datakaryawan()
                                print('Data karyawan "berhasil" dirubah')
                            elif kondisinew == 'N':
                                print('Data karyawan tidak jadi dirubah')
                                update()
                            else:
                                print('masukkan pilihan yang benar')
                                break

                        elif updateketerangan == '4':
                            newusia = input('Masukkan usia karyawan yang baru : ')
                            kondisinew = input('Apakah anda ingin rubah data karyawan (Y/N) : ').capitalize()
                            if kondisinew == 'Y':
                                listkaryawan[i]['Usia'] = newusia
                                datakaryawan()
                                print('Data karyawan "berhasil" dirubah')
                            elif kondisinew == 'N':
                                print('Data karyawan tidak jadi dirubah')
                                update()
                            else:
                                print('masukkan pilihan yang benar')
                                break

                        elif updateketerangan == '5':
                            newgender = input('Masukkan gender karyawan yang baru : ')
                            kondisinew = input('Apakah anda ingin rubah data karyawan (Y/N) : ').capitalize()
                            if kondisinew == 'Y':
                                listkaryawan[i]['Gender'] = newgender
                                print('Data karyawan "berhasil" dirubah')
                                datakaryawan()
                            elif kondisinew == 'N':
                                print('Data karyawan tidak jadi dirubah')
                                update()
                            else:
                                print('masukkan pilihan yang benar')
                                break
                        
                        elif updateketerangan == '6':
                            newalamat = input('Masukkan alamat karyawan yang baru : ')
                            kondisinew = input('Apakah anda ingin rubah data karyawan (Y/N) : ').capitalize()
                            if kondisinew == 'Y':
                                listkaryawan[i]['Posisi'] = newalamat
                                datakaryawan()
                                print('Data karyawan "berhasil" dirubah')
                            elif kondisinew == 'N':
                                print('Data karyawan tidak jadi dirubah')
                                update()
                            else:
                                print('masukkan pilihan yang benar')
                                break
                    elif ganti == 'N':
                        print('Data tidak jadi di update')
                        main_menu()
                    
                    else:
                        print('Masukkan pilihan yang benar')
        elif submenuupdate == '2':
            main_menu()
        else :
            print('Masukkan pilihan yang benar')


# menu 4
def hapus():
    while True:
        print('''
=====================================================================================
MENU Hapus data karyawan :
1. Hapus Data Karyawan
2. kembali ke menu utama
=====================================================================================
''')
        submenuhapus = input('Pilih program yang akan dijalankan : ')
        if submenuhapus == '1':
            if len(listkaryawan) == 0:
                print ('Data karyawan tidak tersedia!!!')
            elif len(listkaryawan) != 0:
                datakaryawan()
                hapusdata = input('Masukkan NIK yang akan dihapus : ')

                list_NIK = []
                for i in range (len(listkaryawan)):
                    list_NIK.append(listkaryawan[i]['NIK'])
                if hapusdata in list_NIK:
                    setuju = input('apakah data karyawan ingin dihapus : (Y/N)').capitalize()
                    if setuju == 'Y':
                        del listkaryawan[list_NIK.index(hapusdata)]
                        datakaryawan()
                        print('Data berhasil dihapus')
                    elif setuju == 'N':
                        print('Data tidak jadi dihapus')
                    else:
                        print(f"NIK {hapusdata} tidak ada")
        
        elif submenuhapus == '2':
            main_menu()
        else:
            continue
    

# menu 5

def sortingkaryawan():
    while True:
        print('''
=====================================================================================
MENU sorting data karyawan berdasarkan:
1. Nama karyawan
2. Posisi karyawan
3. Usia karyawan
4. Gender karyawan
5. Alamat karyawan
6. kembali ke menu utama
=====================================================================================
''')
        inputsort = input('Pilih program yang akan dijalankan : ')
        if inputsort == '1':
            def listnama(element):
                return element['Nama']
            listkaryawan.sort(key=listnama)
            datakaryawan()

        elif inputsort == '2':
            def listposisi(element):
                return element['Posisi']
            listkaryawan.sort(key=listposisi)
            datakaryawan()

        elif inputsort == '3':
            def listusia(element):
                return element['Usia']
            listkaryawan.sort(key=listusia)
            datakaryawan()
            
        elif inputsort == '4':
            def listgender(element):
                return element['Gender']
            listkaryawan.sort(key=listgender)
            datakaryawan()

        elif inputsort == '5':
            def listalamat(element):
                return element['Alamat']
            listkaryawan.sort(key=listalamat)
            datakaryawan()
            
           
        elif inputsort == '6':
            main_menu()  
            break

        else: 

            print()
            print('Masukkan pilihan yang benar')

            continue

main_menu()




































































        #     datakaryawan()
        #     NIK_karyawan_baru = input('masukan NIK (Lima Digit Angka) : ')

        #     if len(NIK_karyawan_baru) != 5:
        #         print('NIK karyawan tidak boleh kurang/lebih dari lima digit')

        #     elif len(NIK_karyawan_baru) == 5:




        #             print(f"NIK : {i['NIK']}, Nama : {i['Nama']}, Posisi : {i['Posisi']}, Usia : {i['Usia']}, Gender : {i['Gender']}, Alamat : {i['Alamat']}")
        #             while True:
        #                 ubah = input('Apakah data karywan akan dirubah : (Y/N)')
        #                 if ubah == 'Y':
        #                     ubahdata = input('Pilih kolom yang akan dirubah (NIK,Nama,Posisi,Usia,Gender dan Alamat) : ')
        #                     if ubahdata == 'nik':
        #                         ubahdata = ubahdata.upper()
        #                     else:
        #                         ubahdata = ubahdata.capitalize()
        #                     ubahisi = input(f"Masukkan {ubahdata} baru").capitalize()
        #                     while True:
        #                         ubah2 = input('Apakah data akan disimpan : (Y/N)')
        #                         if ubah2 == 'Y':
        #                             i[ubahdata] = ubahisi
        #                             print('Data berhasil dirubah') 
        #                             datakaryawan()
        #                             update()
        #                         else:
        #                             print('Masukkan hanya Y/N saja')
        #                 elif ubah == 'N':
        #                     update()
        #                 else:
        #                     print('Masukkan hanya Y/N saja')
        #         else:
        #             print('NIK tidak tersedia')
        # elif submenuupdate == '2':
        #     main_menu()
        # else:
        #     print('Pilih menu yang akan dilaksanakan')
        #     continue





                     


    
#     while True:
#         tampilan_menu()

#         pilihan = input('Pilihan Menu Yang Diinginkan : ')

#         if pilihan == '1' :
            
#             luas_segitiga()
#         elif pilihan == '2' :
#             luas_persegi()
#         elif pilihan == '3' :
#             exit()
#             break
#         else :
#             print("Masukkan Inputan Yang Benar")

# main_app()


# def luas_segitiga():
#     tinggi = float(input("Masukan Tinggi Segitiga : "))
#     alas = float(input("Masukan Alas Segitiga : "))
#     luas = alas * tinggi / 2
#     print(f'Luas segitiga tersebut adalah {luas}')
#     print()

# def luas_persegi():
#     sisi = float(input("Masukan Sisi Dari Persegi : "))
#     luas = sisi ** 2
#     print(f'Luas persegi tersebut adalah {luas}')
#     print()

# def exit():
#     print("Terima Kasih Sudah Menggunakan Aplikasi Kami")
#     print()


# def main_app():
    
#     while True:
#         tampilan_menu()

#         pilihan = input('Pilihan Menu Yang Diinginkan : ')

#         if pilihan == '1' :
#             luas_segitiga()
#         elif pilihan == '2' :
#             luas_persegi()
#         elif pilihan == '3' :
#             exit()
#             break
#         else :
#             print("Masukkan Inputan Yang Benar")

# main_app()


#     print('''List Data Karyawan
# NIK\t| Nama  \t| Posisi              \t\t\t\t| Usia \t\t| Gender\t| Alamat''')

# nama = 'saladin'
# umur = 24
# kelas = 'data science'
# print(f'{nama :<30} {umur :<8} {kelas: <15}')
 # list_NIK = []
                # for i in range (len(listkaryawan)):
                #         list_NIK.append(listkaryawan[i]['NIK'])

                # if NIK_karyawan in list_NIK :
                #         print(f"{NIK_karyawan} Nama : {listkaryawan[list_NIK.index(NIK_karyawan)]['Nama']}, Posisi : {listkaryawan[list_NIK.index(NIK_karyawan)]['Posisi']}, Usia : {listkaryawan[list_NIK.index(NIK_karyawan)]['Usia']}, Gender : {listkaryawan[list_NIK.index(NIK_karyawan)]['Gender']}, Alamat : {listkaryawan[list_NIK.index(NIK_karyawan)]['Alamat']}")
                        
                # else :
                #         print(f' Data karyawan dengan NIK {NIK_karyawan} tidak tersedia!')