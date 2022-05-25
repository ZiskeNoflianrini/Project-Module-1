daftarNilai = [{
        'ID Siswa' : 1901,
        'Nama' : 'Ziske',
        'Nilai Module 1': 70,
        'Nilai Module 2': 80,
        'Nilai Module 3': 90
    },{
        'ID Siswa' : 1902,
        'Nama' : 'Ghea',
        'Nilai Module 1': 70,
        'Nilai Module 2': 80,
        'Nilai Module 3': 90
    },{
        'ID Siswa' : 1903,
        'Nama' : 'Ana',
        'Nilai Module 1': 70,
        'Nilai Module 2': 80,
        'Nilai Module 3': 90
    }]

def menampilkanDaftarnilai():
    while True:
        print(f""" {'='*30}PROGRAM DATA NILAI SISWA PURWADHIKA{'='*30}""")
        pilihanMenu= input("""
        Input data nilai siswa purwadhika
        1. Tampilkan data nilai
        2. Tambahkan nilai
        3. Mengubah data
        4. Menghapus data
        5. Selesai
        Masukkan angka Menu yang ingin dijalankan : """)

        if(pilihanMenu=='1'):
            menampilkanDatanilai()
        elif(pilihanMenu=='2'):
            menambahkanDatanilai()
        elif(pilihanMenu=='3'):
            mengubahDatanilai()
        elif(pilihanMenu=='4'):
            menghapusDatasiswa()
        elif(pilihanMenu=='5'):
            keluar()
            break
        else:
            print('Pilihan yang anda masukkan salah!')
                
def menampilkanDatanilai():
        while True:
            print(f"""
            {('='*8)}Data Siswa{('='*8)}
            1. Tampilkan seluruh data
            2. Tampilkan data tertentu
            3. Kembali ke menu utama
            """)
            pilihsubMenu = input('Silahkan pilih sub menu tampilkan data: ')
            if pilihsubMenu == '1':
                if len(daftarNilai)>0:
                    print('ID Siswa\t Nama\t Nilai Module 1\t Nilai Module 2\t Nilai module 3\t',end='\n')
                    print('='*71)
                    for i in range(len(daftarNilai)):
                        print(f"""{daftarNilai[i]['ID Siswa']}\t\t {daftarNilai[i]['Nama']}\t {daftarNilai[i]['Nilai Module 1']}\t\t {daftarNilai[i]['Nilai Module 2']}\t\t {daftarNilai[i]['Nilai Module 3']}\t\t
                        """)
                elif len(daftarNilai)==0:
                    print('Tidak ada data!')

            elif pilihsubMenu == '2':
                idSiswa=int(input('Masukkan ID Siswa: '))
                ketemu = False

                for i in range(len(daftarNilai)):
                    if daftarNilai[i]['ID Siswa'] == idSiswa:
                        print('ID Siswa\t Nama\t Nilai Module 1\t Nilai Module 2\t Nilai module 3\t',end='\n')
                        print('='*71)
                        print(f"""{daftarNilai[i]['ID Siswa']}\t\t {daftarNilai[i]['Nama']}\t {daftarNilai[i]['Nilai Module 1']}\t\t {daftarNilai[i]['Nilai Module 2']}\t\t {daftarNilai[i]['Nilai Module 3']}\t\t
                    """)
                        ketemu=True
                        break

                if ketemu == False:
                    print('Data yang dimasukkan tidak ada!')
            elif pilihsubMenu == '3':
                break

def menambahkanDatanilai():
        while True:
            print(f"""
            {('='*8)}Menambah Data Siswa{('='*8)}
            1. Tambahkan data siswa
            2. Kembali ke menu utama
            """)
            pilihsubMenu= input('Silahkan pilih sub menu tampilkan data: ')
            if pilihsubMenu == '1':
                idSiswa= int(input('Masukkan ID Siswa: '))
                ketemu = False
                for i in range(len(daftarNilai)):
                    if daftarNilai[i]['ID Siswa'] == idSiswa:
                        print('Data sudah ada!')
                        ketemu = True
                if ketemu== False:
                    nama= (input('Masukkan Nama: '))
                    module1= int(input('Masukkan Nilai Module 1: '))
                    module2= int(input('Masukkan Nilai Module 2: '))
                    module3= int(input('Masukkan Nilai Module 3: '))
                    tanya= (input('Apakah data akan disimpan?(Y/N) '))
                    if tanya == 'Y':
                        print('Data tersimpan')
                        daftarNilai.append({
                        'ID Siswa' : idSiswa,
                        'Nama' : nama,
                        'Nilai Module 1': module1,
                        'Nilai Module 2': module2,
                        'Nilai Module 3': module3
                        })
                        break
                    elif tanya == 'N':
                        print('Data tidak tersimpan')
                        
            if pilihsubMenu == '2':
                break
        
def mengubahDatanilai():
        while True:
            print(f"""
            {('='*8)}Mengubah Data Siswa{('='*8)}
            1. Ubah data siswa
            2. Kembali ke menu utama
            """)
            pilihsubMenu= input('Silahkan pilih sub menu tampilkan data: ')
            if pilihsubMenu=='1':
                idSiswa=int(input('Masukkan ID Siswa: '))
                index=0
                ketemu=False
                for i in range(len(daftarNilai)):
                    if daftarNilai[i]['ID Siswa'] == idSiswa:
                        print('ID Siswa\t Nama\t Nilai Module 1\t Nilai Module 2\t Nilai module 3\t',end='\n')
                        print('='*71)
                        print(f"""{daftarNilai[i]['ID Siswa']}\t\t {daftarNilai[i]['Nama']}\t {daftarNilai[i]['Nilai Module 1']}\t\t {daftarNilai[i]['Nilai Module 2']}\t\t {daftarNilai[i]['Nilai Module 3']}\t\t
                    """)
                        ketemu=True
                        break
                    else:
                        index+=1
                        break
                if ketemu==False:
                    print('Data tidak ada')
                    continue
                tanya1= input('Apakah ada data yang ingin diubah?(Y/N): ')
                if tanya1 == 'Y':
                    kolom= input('Masukkan kolom yang akan diubah: ')
                    if kolom == 'Nama':
                        a=(input('Nama = '))
                        tanya1= input('Apakah data ingin disimpan?(Y/N) ')
                        if tanya1 == 'Y':
                            daftarNilai[index]['Nama']=a
                            print('Data Terupdate')
                        elif tanya1 == 'N':
                            print('Data tidak tersimpan!')
                    elif kolom == 'Nilai Module 1':
                        b=(input('Nilai Module 1 = '))
                        tanya1= input('Apakah data ingin disimpan?(Y/N) ')
                        if tanya1 == 'Y':
                            daftarNilai[index]['Nilai Module 1']=b
                            print('Data Terupdate')
                        elif tanya1 == 'N':
                            print('Data tidak tersimpan!')
                    elif kolom == 'Nilai Module 2':
                        c=(input('Nilai Module 2 = '))
                        tanya1= input('Apakah data ingin disimpan?(Y/N) ')
                        if tanya1 == 'Y':
                            daftarNilai[index]['Nilai Module 2']=c
                            print('Data Terupdate')
                        elif tanya1 == 'N':
                            print('Data tidak tersimpan!')
                    elif kolom == 'Nilai Module 3':
                        d=(input('Nilai Module 3 = '))
                        tanya1= input('Apakah data ingin disimpan?(Y/N) ')
                        if tanya1 == 'Y':
                            daftarNilai[index]['Nilai Module 3']=d
                            print('Data Terupdate')
                        elif tanya1 == 'N':
                            print('Data tidak tersimpan!')
            else:
                break    
            
def menghapusDatasiswa():
        while True:
            print(f"""
            {('='*8)}Menghapus Data Siswa{('='*8)}
            1. Hapus data siswa
            2. Kembali ke menu utama
            """)
            pilihsubMenu= input('Silahkan pilih sub menu tampilkan data: ')
            if pilihsubMenu == '1':
                idSiswa=int(input('Masukkan ID Siswa: '))
                index=0
                ketemu=False
                for i in range(len(daftarNilai)):
                    if daftarNilai[i]['ID Siswa'] == idSiswa:
                        print('ID Siswa\t Nama\t Nilai Module 1\t Nilai Module 2\t Nilai module 3\t',end='\n')
                        print('='*71)
                        print(f"""{daftarNilai[i]['ID Siswa']}\t\t {daftarNilai[i]['Nama']}\t {daftarNilai[i]['Nilai Module 1']}\t\t {daftarNilai[i]['Nilai Module 2']}\t\t {daftarNilai[i]['Nilai Module 3']}\t\t
                    """)
                        ketemu=True
                        break
                    else:
                        index+=1
                        break
                if ketemu==False:
                    print('Data tidak ada')
                    continue
                tanya1= input('Apakah data ini ingin dihapus?(Y/N) ')
                if tanya1 == 'Y':
                    del daftarNilai[index]
                    print('Data Terhapus')
                elif tanya1 == 'N':
                    print('Data tidak tersimpan')
                else:
                    break
            else:
                break

def keluar():
        print('Selesai')
    
menampilkanDaftarnilai()


        


      

        
