liste = [ 'Ahmet Mehmet' , 'Ali Veli' , 'Ayşe Fatma' ]
#1
def isimSoyisimleOgreciGirisi(isim,soyIsim):
    liste.append(isim+' '+soyIsim)
#2
def isimSoyisimleOgrenciSil():
    silinecekIsimSoyisim = input("Silinecek Öğrenci İsmini Soyismini arada boşlukla Giriniz")
    for ogrenci in liste:
        if silinecekIsimSoyisim==ogrenci:
            liste.pop(ogrenci)
        else:
            None
#3
def birdenFazlaOgrenciEkleme():
    eklenecekOgrenciSayisi = input("Kaç adet öğrenci ekleneceğini giriniz:")
    if eklenecekOgrenciSayisi.isdigit():
        print("Lütfen sayı giriniz")
    else:
        for sayi in range(int(eklenecekOgrenciSayisi)):
            isim = input("Öğrenci İsmini Giriniz")
            soyIsim = input("Öğrenci Soy İsmini Giriniz")
            liste.append(isim+' '+soyIsim)
#4
def tumOgrencileriGoster():
    for ogrenci in liste:
        print(ogrenci+'\n')
#5
def ogrencileriNumaraylaSorgula():
    ogrenciNumarasi = input("Öğrenci numarası giriniz")
    print('{} numaralı öğrenci:'.format(ogrenciNumarasi)+' '+liste[ogrenciNumarasi])
#6
def birdenFazlaOgrenciSilme():
    silinecekOgrencilerListesi = [input("Silinecek Öğrencileri giriniz\nÖRNEK:Ayşe Fatma,Ali Veli:")]
    for silinecekOgrenci in silinecekOgrencilerListesi:
        for ogrenci in liste:
            if silinecekOgrenci == ogrenci:
                liste.pop(ogrenci.index)
                
secim = input("\n1) İsim-Soyisim ile Öğrenci Ekleme\n2) İsim-Soyisim ile Öğrenci silme\n3) Birden Fazla Öğrenci Ekleme\n4) Tüm Öğrencileri Gösterme\n5) Öğrenci Numarası ile İsim-Soyisim Sorgulama\n6) Birden Fazla Öğrenci Ekleme\n\nLütfen Yapmak istediğiniz İşlemi Giriniz:")
def secenekAl():
    while secim=='4':
        tumOgrencileriGoster()
        break
    while secim=='1':
        isim = input("Öğrenci İsmini Giriniz")
        soyIsim = input("Öğrenci Soy İsmini Giriniz")
        isimSoyisimleOgreciGirisi(isim,soyIsim)
        break
    while secim=='2':
        isimSoyisimleOgrenciSil()
        break
    while secim=='3':
        birdenFazlaOgrenciEkleme()     
        break  
    while secim=='5':
        ogrencileriNumaraylaSorgula
        break
    while secim=='6':
        birdenFazlaOgrenciSilme()
        break

secenekAl()
