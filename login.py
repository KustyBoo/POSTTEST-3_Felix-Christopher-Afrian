import sys

daftaruser = ["chris"]
daftarpass = ["12345"]

def register() :
    print ("|=================================|")
    print ("|Selamat datang di registrasi akun|")
    print ("|=================================|")
    userbaru = str(input("silahkan masukkan username baru = "))
    print ("|=============================|")
    passbaru = str(input("silahkan masukkan password baru = "))
    print ("|=============================|")
    x = 1
    while x > 0  :
        if not userbaru in daftaruser :
                daftaruser.append(userbaru)
                daftarpass.append(passbaru)
                print ("|========================================================================|")
                print ("|Selamat, akun berhasil terdaftar, apakah anda ingin masuk ke dalam akun?|")
                print ("|========================================================================|")
                ingin = input("ketik ya untuk masuk atau tidak untuk membatalkan program = ")
                if ingin == "ya" or ingin == "Ya" or ingin == "YA" :
                    masuk()
                    
                elif ingin == "tidak" or ingin == "Tidak" or ingin == "TIDAK" :
                    print ("|=============================|")
                    print ("|Terima kasih, selamat tinggal|")
                    print ("|=============================|")

        elif userbaru in daftaruser :
            print ("|====================================|")
            print ("|Mohon maaf, username sudah terdaftar|")
            print ("|====================================|")
            userbaru = str(input("silahkan masukkan username baru = "))
            print ("|=======================================|")
            passbaru = str(input("silahkan masukkan password baru = "))
            print ("|=======================================|")
        break
    return



def masuk() :
    print ("|===================HALO=====================|")
    usermasuk = str(input("|Silahkan masukkan username = "))
    passmasuk = str(input("|Silahkan masukkan password = "))
    print ("|============================================|")
    coba = 0
    while coba < 3 :
        if usermasuk in daftaruser :
            if passmasuk in daftarpass :
                print ("|==================HALO==================|")
                print ("|-------------selamat datang-------------|")
                print ("|========================================|")
                sys.exit()
            else :
                print ("|=============================================|")
                print ("|Mohon maaf, password yang anda masukkan salah|")
                print ("|=============================================|")
        elif not usermasuk in daftaruser :
            print ("|===================================================================|")
            print ("|mohon maaf, username/password yang telah dimasukkan tidak terdaftar|")
            print ("|===================================================================|")
            baru = input("ingin membuat akun baru ?(type \"ya\" untuk membuat akun atau \"tidak\" untuk membatalkan) = ")
            if baru == "ya" or baru == "YA" or baru == "Ya" :
                register()
            elif baru == "tidak" :
                print ("|===================HALO=====================|")
                usermasuk = str(input("|Silahkan masukkan username = "))
                passmasuk = str(input("|Silahkan masukkan password = "))
                print ("|============================================|")
                coba += 1
                if coba >= 2 :
                    print ("|================================================================|")
                    print ("|Mohon maaf, anda telah gagal masuk 3 kali, mohon restart program|")
                    print ("|================================================================|")
                    sys.exit()

        

      

            

    
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
    print("======================Halo======================")
    print("ingin membuat akun atau masuk ke yang sudah ada?")
    mulai = input("ketik \"masuk\" untuk masuk ke akun,\nketik \"buat\" untuk membuat akun baru = ")
    if mulai == "masuk" or mulai == "Masuk" or mulai == "MASUK" :
        masuk()
    else :
        register()
else :
    print ("error, restart program to continue")