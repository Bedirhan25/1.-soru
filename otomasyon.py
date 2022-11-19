class Ogrenci:
    def __init__(self,id, isim, soyisim, sinif, yas, cinsiyet):
        self.id = id
        self.isim = isim
        self.soyisim = soyisim
        self.sinif = sinif
        self.yas = yas
        self.cinsiyet = cinsiyet
        print("a")

    def kayit(self):
        dosya = open("öğrenci.txt",mode='a',encoding='utf-8')
        dosya.write("İd: " + self.id + " İsim: " + self.isim + " Soyisim: " + self.soyisim + " Sinif: " + self.sinif + " Yas: " + self.yas + " Cinsiyet: " + self.cinsiyet + "\n")
        dosya.close()
    def silme(idd):
        dosya = open("öğrenci.txt", mode='r+', encoding='utf-8')
        bilgiler = dosya.readlines()
        dosya.seek(0)
        for bilgi in bilgiler:
            if bilgi.count(idd) == 1:
                continue
            dosya.write(bilgi)
        dosya.truncate()
        dosya.close()
    def bilgi(iddd):
        dosya = open("öğrenci.txt", mode='r+', encoding='utf-8')
        bilgiler = dosya.readlines()
        dosya.seek(0)
        for bilgi in range(len(bilgiler)):
            if bilgiler[bilgi].count(iddd) == 1:
                print(bilgiler[bilgi])

while 1:
    a = int(input("Kayit için 1\nOgrenci silme icin 2\nOgrenci bilgileri icin 3\ncikis icin 0 a basiniz:  "))
    if a==1:
        id = input("id girin ")
        isim = input("isim girin ")
        soyisim = input("soyisim girin ")
        sinif = input("sınıf girin ")
        yas = input("yas girin ")
        cinsiyet = input("cinsiyet girin ")
        ogrenci = Ogrenci(id, isim, soyisim, sinif, yas, cinsiyet)
        ogrenci.kayit()
    if a==2:
        idd = input("silinmesi istediğiniz öğrencinin id'sini girin")
        Ogrenci.silme(idd)
    if a==3:
        iddd = input("bilgilerini istediğiniz öğrencinin id'sini girin")
        Ogrenci.bilgi(iddd)
    if a==0:
        break
