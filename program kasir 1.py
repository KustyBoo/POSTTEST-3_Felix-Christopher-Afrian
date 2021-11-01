from datetime import datetime
from typing import Counter
import sys

menu_minuman ={
    "teh es" : 6000,
    "jeruk es" : 8000,
    "teh hangat" : 6000,
    "jeruk hangat" : 8000,
    "air mineral" : 5000
}

menu_makanan = {
    "nasi goreng" : 18000,
    "mie goreng" : 22000,
    "lontong sayur" : 17000
}

keranjang = []
keranjang1 = []
total = []

def kasir () :
    print ("|===============================================================|")
    print ("|---------menu makanan akan ditampilkan terlebih dahulu---------|")
    print ("|===============================================================|")
    print ("|===============================================================|")
    print ("|======Silahkan pilih menu yang telah tersedia di bawah ini=====|")
    print ("|===============================================================|")
    print ("|Menu Makanan :                 Harga :                         |")
    print ("|1. Nasi Goreng                 Rp18.000                        |")
    print ("|2. Mie Goreng                  Rp22.000                        |")
    print ("|3. Lontong Sayur               Rp17.000                        |")
    print ("|===============================================================|")
    masuk = input("|Silahkan pilih makanan yang ingin dipesan = ")
    while masuk != "keluar" :
        if masuk in menu_makanan :
            keranjang.append(masuk)
            masuk = input("|Makanan telah di-input,\n|Silahkan ketik makanan lain untuk lanjut meng-input,\n|atau ketik \"minuman\" untuk lanjut meng-input minuman = ")
        if masuk == "minuman" :
            print ("|====================================================|")
            print ("|Silahkan pilih menu yang telah tersedia di bawah ini|")
            print ("|====================================================|")
            print ("|Menu Minuman :                 Harga :              |")
            print ("|1. Teh es/hangat               Rp 6.000             |")
            print ("|2. Jeruk es/hangat             Rp 8.000             |")
            print ("|3. Air mineral                 Rp 5.000             |")
            print ("|====================================================|")
            masuk2 = input("|Silahkan ketik minuman yang anda ingin pesan disini = ")
            while masuk2 != "keluar" : 
                if masuk2 in menu_minuman :
                    keranjang1.append(masuk2)
                    masuk2 = input("|Minuman telah di-input,\n|Silahkan ketik minuman lain untuk lanjut meng-input,\n|atau ketik \"keluar\" untuk keluar = ")
                    if masuk2 == "keluar" or masuk2 == "Keluar" or masuk2 == "KELUAR" :
                            print ("|===========================================================================================================================|")
                            print ("|===========================================================================================================================|")
                            print ("|Berikut daftar pesanan makanan/minuman yang telah anda pesan = ", keranjang + keranjang1)
                            print ("|===========================================================================================================================|")
                            print ("|===========================================================================================================================|")
                            masuk2 = input("|Apakah anda ingin memesan makanan/minuman lain? jika iya maka ketik YA, tapi jika tidak maka ketik TIDAK = ")
                            print ("|===========================================================================================================================|")
                            if masuk2 == "YA" or masuk2 == "ya" or masuk2 == "Ya" :
                                print ("|Pesanan anda saat ini = ", keranjang + keranjang1)
                                kasir()
                                
                            elif masuk2 == "tidak" or masuk2 == "Tidak" or masuk2 == "TIDAK" :
                                keranjang3 = keranjang + keranjang1
                                for items in keranjang3 :
                                    gabung = Counter(menu_minuman) + Counter(menu_makanan)
                                    total.append(gabung[items])
                                    total_yang_dibayar = sum(total)
                                print ("|Total harga = ", total_yang_dibayar)
                                if len(keranjang1) >= 3 and not len(keranjang) >= 2:
                                    if datetime.today().isoweekday() != 6 and datetime.today().isoweekday() != 7 :
                                        total1 = total_yang_dibayar - ((total_yang_dibayar * 10/100) + (total_yang_dibayar * 10/100))
                                        print ("|Selamat, anda mendapatkan diskon sebesar 20% karena membeli 3 minuman(atau lebih) saat weekday menjadi = ", total1)
                                        duit = input("|Metode pembayaran apa yang ingin anda gunakan? ketik \"C\" untuk cash\n|dan \"E\" untuk e-money = ")
                                        if duit == "E" or duit == "e" :
                                            total2 = total1 - (total1 * 5/100)
                                            print ("|Selamat anda mendapatkan bonus diskon 5% penggunaan e-money menjadi = ", total2)
                                            print ("|Terima kasih, selamat datang kembali!|")
                                            
                                        elif duit == "C" or duit == "c" :
                                            print ("|Terima kasih, selamat datang kembali!|")
                                            
                                    elif datetime.today().isoweekday() == 6 and datetime.today().isoweekday() == 7 :
                                        total1 = total_yang_dibayar - ((total_yang_dibayar * 10/100) + (total_yang_dibayar * 5/100))
                                        print ("|Selamat, anda mendapatkan diskon sebesar 15% karena membeli 3 minuman(atau lebih) saat weekend menjadi = ", total1)
                                        duit = input("|Metode pembayaran apa yang ingin anda gunakan? ketik \"C\" untuk cash\n|dan \"E\" untuk e-money = ")
                                        if duit == "E" or duit == "e" :
                                            total2 = total1 - (total1 * 5/100)
                                            print ("|Selamat anda mendapatkan bonus diskon 5% penggunaan e-money menjadi = ", total2)
                                            print ("|Terima kasih, selamat datang kembali!|")
                                            
                                        elif duit == "C" or duit == "c" :
                                            print ("|Terima kasih, selamat datang kembali!|")
                                            
                                elif len(keranjang) >= 2 and not len(keranjang1) >= 3 :
                                    if datetime.today().isoweekday() != 6 and datetime.today().isoweekday() != 7 :
                                        total1 = total_yang_dibayar - ((total_yang_dibayar *5/100) + (total_yang_dibayar * 10/100))
                                        print ("|Selamat, anda mendapatkan diskon sebesar 15% karena pembelian 2 makanan(atau lebih) saat weekday menjadi = ", total1)
                                        duit = input("|Metode pembayaran apa yang ingin anda gunakan? ketik \"C\" untuk cash\n|dan \"E\" untuk e-money = ")
                                        if duit == "E" or duit == "e" :
                                            total2 = total1 - (total1 * 5/100)
                                            print ("|Selamat anda mendapatkan bonus diskon 5% penggunaan e-money menjadi = ", total2)
                                            print ("|Terima kasih, selamat datang kembali!|")
                                            
                                        elif duit == "C" or duit == "c" :
                                            print ("|Terima kasih, selamat datang kembali!|")
                                            
                                    elif datetime.today().isoweekday() == 6 and datetime.today().isoweekday() == 7 :
                                        total1 = total_yang_dibayar - ((total_yang_dibayar * 5/100) + (total_yang_dibayar * 5/100))
                                        print ("|Selamat, anda mendapatkan diskon sebesar 10% karena pembelian 2 makanan(atau lebih) saat weekend menjadi = ", total1)
                                        duit = input("|Metode pembayaran apa yang ingin anda gunakan? ketik \"C\" untuk cash\n|dan \"E\" untuk e-money = ")
                                        if duit == "E" or duit == "e" :
                                            total2 = total1 - (total1 * 5/100)
                                            print ("|Selamat anda mendapatkan bonus diskon 5% penggunaan e-money menjadi = ", total2)
                                            print ("|Terima kasih, selamat datang kembali!|")
                                            
                                        elif duit == "C" or duit == "c" :
                                            print ("|Terima kasih, selamat datang kembali!|")
                                            
                                elif len(keranjang) >= 2 and len(keranjang1) >= 3 :
                                    if datetime.today().isoweekday() != 6 and datetime.today().isoweekday() != 7 :
                                        total1 = total_yang_dibayar - ((total_yang_dibayar * 15/100) + (total_yang_dibayar * 10/100))
                                        print ("|Selamat, anda mendapatkan diskon sebesar 25% karena pembelian 2 makanan(atau lebih)\n|dan 3 minuman(atau lebih) saat weekday menjadi = ", total1)
                                        duit = input("|Metode pembayaran apa yang ingin anda gunakan? ketik \"C\" untuk cash\n|dan \"E\" untuk e-money = ")
                                        if duit == "E" or duit == "e" :
                                            total2 = total1 - (total1 * 5/100)
                                            print ("|Selamat anda mendapatkan bonus diskon 5% penggunaan e-money menjadi = ", total2)
                                            print ("|Terima kasih, selamat datang kembali!|")
                                            
                                        elif duit == "C" or duit == "c" :
                                            print ("|Terima kasih, selamat datang kembali!|")
                                            
                                    elif datetime.today().isoweekday() == 6 and datetime.today().isoweekday() == 7 :
                                        total1 = total_yang_dibayar - ((total_yang_dibayar * 15/100) + (total_yang_dibayar * 5/100))
                                        print ("|Selamat, anda mendapatkan diskon sebesar 20% karena pembelian 2 makanan(atau lebih)\n|dan 3 minumana(atau lebih) saat weekend menjadi = ", total1)
                                        duit = input("|Metode pembayaran apa yang ingin anda gunakan? ketik \"C\" untuk cash\n|dan \"E\" untuk e-money = ")
                                        if duit == "E" or duit == "e" :
                                            total2 = total1 - (total1 * 5/100)
                                            print ("|Selamat anda mendapatkan bonus diskon 5% penggunaan e-money menjadi = ", total2)
                                            print ("|Terima kasih, selamat datang kembali!|")
                                            
                                        elif duit == "C" or duit == "c" :
                                            print ("|Terima kasih, selamat datang kembali!|")
                                            
                                elif not len(keranjang) >= 2 and not len(keranjang1) >= 3 :
                                    if datetime.today().isoweekday() != 6 and datetime.today().isoweekday() != 7 :
                                        total1 = total_yang_dibayar - (total_yang_dibayar * 10/100)
                                        print ("|Selamat, anda mendapatkan diskon sebesar 10% karena pembelian makanan/minuman saat weekday menjadi = ", total1)
                                        duit = input("|Metode pembayaran apa yang ingin anda gunakan? ketik \"C\" untuk cash\n|dan \"E\" untuk e-money = ")
                                        if duit == "E" or duit == "e" :
                                            total2 = total1 - (total1 * 5/100)
                                            print ("|Selamat anda mendapatkan bonus diskon 5% penggunaan e-money menjadi = ", total2)
                                            print ("|Terima kasih, selamat datang kembali!|")
                                           
                                        elif duit == "C" or duit == "c" :
                                            print ("|Terima kasih, selamat datang kembali!|")
                                            
                                    elif datetime.today().isoweekday() == 6 and datetime.today().isoweekday() == 7 :
                                        total1 = total_yang_dibayar - (total_yang_dibayar * 5/100)
                                        print ("|Selamat, anda mendapatkan diskon sebesar 5% karena pembelian makanan/minuman saat weekend menjadi = ", total1)
                                        duit = input("|Metode pembayaran apa yang ingin anda gunakan? ketik \"C\" untuk cash\n|dan \"E\" untuk e-money = ")
                                        if duit == "E" or duit == "e" :
                                            total2 = total1 - (total1 * 5/100)
                                            print ("|Selamat anda mendapatkan bonus diskon 5% penggunaan e-money menjadi = ", total2)
                                            print ("|Terima kasih, selamat datang kembali!|")
                                            
                                        elif duit == "C" or duit == "c" :
                                            print ("|Terima kasih, selamat datang kembali!|")
                                            
                                elif datetime.today().isoweekday() != 6 and datetime.today().isoweekday() != 7 :
                                    total_beneran = total_yang_dibayar - (total_yang_dibayar * 10/100)
                                    print ("|Total harga = ", total_beneran)
                                    
                                elif datetime.today().isoweekday() == 6 and datetime.today().isoweekday() == 7 :
                                    total_beneran = total_yang_dibayar - (total_yang_dibayar * 5/100)
                                    print ("|Total harga = ", total_beneran)
                                sys.exit()
                            
            
def main_menu () :
    print ("       /   \                          /  \                          ")
    print ("      /  /\ \                        / /\ \                         ")
    print ("     /  /  \ \                      / /  \ \                        ") 
    print ("    /  /    \ \                    / /    \ \                       ")
    print ("   /  /      \ \                  / /      \ \                      ")
    print ("  /  /        \ \    KustyBoo    / /        \ \                     ")
    print (" /  /          \ \______________/ /          \ \                    ")
    print("|                                               |                   ")
    print("|         000                     000           |                   ")
    print("|        0 | 0                   0 | 0          |                   ")
    print("|        0 | 0                   0 | 0          |                   ")
    print("|        0 | 0          |        0 | 0          |                   ")
    print("|          0           |           0            |                   ")
    print("|                       |                       |                   ")
    print("|                                               |                   ")
    print("|             ||      |||||      ||             |                   ")
    print("|              ||    ||   ||    ||              |                   ")
    print("|               ||||||     ||||||               |                   ")
    print("|                                               |                   ")
    print("|                                               |                   ")
    print("|_______________________________________________|                   ")
    print("|===================== uwu =====================|")
    print ("|-----------------------------------------------|")
    print ("|-----Halo, Selamat Datang di Program login-----|")
    print ("|-------Made by Felix Christopher Afrian--------|")
    print ("|-----------------------------------------------|")
    print ("|------------Type \"mulai\" to enter--------------|")
    x = input("|ketik mulai = ")
    while x == "mulai" or x == "MULAI" or x == "Mulai" :
        if x == "mulai" or x == "Mulai" or x == "MULAI" :
            kasir()
        else :
            print ("system error, please restart the program")
    return


main_menu()                                                           