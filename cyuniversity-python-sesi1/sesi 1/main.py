import random

welcome_message = " WELCOME CUYPY PLAY GAME!"
cuypy_position = random.randint(1, 4)

print("*************************")
print(f"** {welcome_message}***")
print("*************************")


nama_user = input("masukan nama Kamu: ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4 # INI TETAP KOSONG

goa = goa_kosong.copy() #INI ADALAH TEMPAT BARU UNTUK SI CUYPY

goa[cuypy_position -1] = "|0_0|"

print(f'''
      Halo {nama_user}! coba perhatikan goa di bawah ini
{goa_kosong}

''')
pilihan_user = int( input("Menurut Kamu  di goa nomor berapa Dimana CUPYPY berada? [1/ 2 / 3 / 4]: "))

confirm_answer = input(f"apakah kamu yakin jawaban nya adalah {pilihan_user}? [y/n]: ")

if confirm_answer == "n":
    print("program dihentikan!")
    exit()
elif confirm_answer == "y":
    if pilihan_user == cuypy_position:
        print(f"{goa}, \n SELAMAT KAMU  MENANG!")

    else:
         print(f"{goa}, \n MAAF KAMU KALAH!")
else:
    print("silahkan ulangi program nya!")
    exit()