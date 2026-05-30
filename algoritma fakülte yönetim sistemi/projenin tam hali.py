ogrenciler = []
MAX_OGRENCI = 100


def ogrenci_ekle():
    if len(ogrenciler) >= MAX_OGRENCI:
        print("Maksimum öğrenci sayısına ulaşıldı")
        return

    ad = input("Ad: ")
    soyad = input("Soyad: ")
    numara = input("Numara: ")
    bolum = input("Bölüm: ")
    sinif = input("Sınıf: ")

    print("Vize Notları")
    a_vize = int(input("A dersi: "))
    b_vize = int(input("B dersi: "))
    c_vize = int(input("C dersi: "))

    print("Final Notları")
    a_final = int(input("A dersi: "))
    b_final = int(input("B dersi: "))
    c_final = int(input("C dersi: "))

    ogrenci = {
        "ad": ad,
        "soyad": soyad,
        "numara": numara,
        "bolum": bolum,
        "sinif": sinif,
        "vize": {"A": a_vize, "B": b_vize, "C": c_vize},
        "final": {"A": a_final, "B": b_final, "C": c_final}
    }

    ogrenciler.append(ogrenci)
    print("Öğrenci eklendi")


def ogrenci_guncelle():
    numara = input("Güncellenecek öğrenci no: ")

    for ogr in ogrenciler:
        if ogr["numara"] == numara:

            ogr["sinif"] = input("Yeni sınıf: ")

            print("Yeni vize notları")
            ogr["vize"]["A"] = int(input("A: "))
            ogr["vize"]["B"] = int(input("B: "))
            ogr["vize"]["C"] = int(input("C: "))

            print("Yeni final notları")
            ogr["final"]["A"] = int(input("A: "))
            ogr["final"]["B"] = int(input("B: "))
            ogr["final"]["C"] = int(input("C: "))

            print("Güncellendi")
            return

    print("Öğrenci bulunamadı")


def ogrenci_ara():
    aranan = input("Aranacak bilgi: ")

    for ogr in ogrenciler:
        if aranan.lower() in ogr["ad"].lower() or aranan == ogr["numara"]:
            print(ogr["ad"], ogr["soyad"], "-", ogr["numara"], "-", ogr["bolum"])


def ogrenci_listele():
    i = 1
    for ogr in ogrenciler:
        print(i, ")", ogr["ad"], ogr["soyad"], "-", ogr["numara"], "-", ogr["bolum"], "-", ogr["sinif"], ".Sınıf")
        i += 1


def ogrenci_sil():
    numara = input("Silinecek öğrenci numarası: ")

    for ogr in ogrenciler:
        if ogr["numara"] == numara:
            ogrenciler.remove(ogr)
            print("Öğrenci silindi")
            return

    print("Öğrenci bulunamadı")


def grup_olustur():
    kisi = int(input("Her grupta kaç öğrenci olsun: "))

    grup = 1
    sayac = 0

    for ogr in ogrenciler:

        if sayac % kisi == 0:
            print("\nGrup", grup)
            grup += 1

        print(ogr["ad"], ogr["soyad"])
        sayac += 1


def istatistik():
    print("Toplam Öğrenci:", len(ogrenciler))

    bolumler = {}
    siniflar = {}

    for ogr in ogrenciler:

        bolum = ogr["bolum"]
        sinif = ogr["sinif"]

        bolumler[bolum] = bolumler.get(bolum, 0) + 1
        siniflar[sinif] = siniflar.get(sinif, 0) + 1

    print("\nBölümlere göre")
    for b in bolumler:
        print(b, ":", bolumler[b])

    print("\nSınıflara göre")
    for s in siniflar:
        print(s, ".Sınıf:", siniflar[s])


def notlarim(numara):

    for ogr in ogrenciler:
        if ogr["numara"] == numara:

            print("\n--- NOTLARIM ---")
            print("A dersi:", ogr["vize"]["A"], "/", ogr["final"]["A"])
            print("B dersi:", ogr["vize"]["B"], "/", ogr["final"]["B"])
            print("C dersi:", ogr["vize"]["C"], "/", ogr["final"]["C"])
            return

    print("Öğrenci bulunamadı")


def ogrenci_bilgileri(numara):

    for ogr in ogrenciler:
        if ogr["numara"] == numara:

            print("Ad:", ogr["ad"])
            print("Soyad:", ogr["soyad"])
            print("Numara:", ogr["numara"])
            print("Bölüm:", ogr["bolum"])
            print("Sınıf:", ogr["sinif"])
            return


while True:

    print("\nGİRİŞ MENÜ")
    print("1 Yönetici")
    print("2 Öğrenci")
    print("3 Çıkış")

    secim = input("Seçim: ")

    if secim == "1":

        kullanici = input("Kullanıcı adı: ")
        sifre = input("Şifre: ")

        if kullanici == "admin" and sifre == "1234":

            while True:

                print("\nYÖNETİCİ MENÜ")
                print("1 Öğrenci ekle")
                print("2 Öğrenci güncelle")
                print("3 Öğrenci ara")
                print("4 Öğrenci listele")
                print("5 Gruplara ayır")
                print("6 Öğrenci sil")
                print("7 İstatistik")
                print("8 Çıkış")

                sec = input("Seçim: ")

                if sec == "1":
                    ogrenci_ekle()

                elif sec == "2":
                    ogrenci_guncelle()

                elif sec == "3":
                    ogrenci_ara()

                elif sec == "4":
                    ogrenci_listele()

                elif sec == "5":
                    grup_olustur()

                elif sec == "6":
                    ogrenci_sil()

                elif sec == "7":
                    istatistik()

                elif sec == "8":
                    break

        else:
            print("Hatalı giriş")

    elif secim == "2":

        numara = input("Öğrenci numarası: ")

        while True:

            print("\nÖĞRENCİ MENÜ")
            print("1 Bilgilerimi gör")
            print("2 Notlarım")
            print("3 Çıkış")

            sec = input("Seçim: ")

            if sec == "1":
                ogrenci_bilgileri(numara)

            elif sec == "2":
                notlarim(numara)

            elif sec == "3":
                break

    elif secim == "3":
        break