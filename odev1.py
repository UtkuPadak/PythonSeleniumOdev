"""

ÖDEV 1:
Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

Ödev linkinizi buraya yorum olarak ekleyiniz.

a)Metin Tipleri:
1)String(str):Metin,harf,noktalama işaretleri içeren veri tipi."iki çift tırnak arasına" ya da 'iki tek tırnak arasına' yazılır.Değişkene değer verilirken "3" şeklinde yazarsak string olarak algılar.ÖRNEK:"S3m", '2'
b)Sayısal Veri Tipleri:
1)Integer(int):Tam sayı içeren veri tipi.Eksi(-)değer alabilir.
2)Float(float):Tam sayı olmayan sayıları içerir.ÖRNEK:1.5,9.7
3)Complex
c)Mantıksal Veri Tipleri:
1)Boolean(bool):True veya False mantıksal değer içeren veri tipi.
Diğer Veri Tipleri:
1)Liste(list):Liste veri tipi.Liste şeklinde karışık harf,sayı,rakam,verileri tutabilir.[]şeklinde gösterilir.Tekrar eden elemanlardan oluşabilir.Elemanlar içinde gezilebilir.Belirli elemanın değerine ulaşılabilir.
ÖRNEK:liste =[1,2,True, 'a', 1],liste[2]==>listedeki 3ncü değere  ya da liste[-1] en son değere ulaşılabilir.
2)Dictionary(dict):Key(anahtar) Value(Değer) çiftlerini içeren veri tipi.{}arasında gösterilir.Tek değerle birden fazla değere erişilebilir.ÖRNEK:{'isim' : 'Utku', 'kurs' : 'Python & Selenium Yazılım Geliştirici Yetiştirme Kampı'}
3)Tuple(tup):Liste veya set benzeri veri tipi.Değerleri sabit,değiştirilemez.() ile gösterilir.ÖRNEK:(1, 2, True)
Range(range):Range liste benzeri veri tipi.Listeye döndürülebilir.ÖRNEK:range(5)==>0 dan 5 e kadar(5 dahil değil)
liste(range(1,6))==>[ 1, 2, 3, 4, 5 ]

Kodlama.io daki veri tipleri:
Kayıt Ol Giriş Ekranında 
Full Name:String
Email::String
Password:String
Giriş yaptıktan sonra e-mail ve şifre nin doğru olup olmadığı dictionary deki kişilerin e-mail ve ona karşılık gelen şifreleri kontrolünün sağlanması.kullanici1,kullanici2... gibi.Bu dictionarylerinde listede bulunması
kullaniciListesi = [kullanici1,kullanici2,kullanici3...]
Kursun tamamlanma yüzdesi:integer
Tüm Kurslar sayfasında:dictionary Anahtarlara karşılık gelen değer çifti.Key(Anahtar):Kategori Eğitmen Values(Değer):Tümü,
Yazılım,Tümü,Engin Demiroğ,Halit Enes Kalaycı.Tümünde ise dict.values() ile.
Ödeme kısmındaki Ülke adları tuple.

"""
#Ödev 2
#Kayıt olurken e mail kontrolü içerisinde 1 adet @ işareti bulunabilirliği,@ den sonra en az 1 nokta işaretinin bulunabilirliği olabilir.
#Kodlama.io ya Kullanıcı girişi
kullanici1 = {'kayitNo':1, 'eMail':'Utku','sifre':'12345'}
kullanici2 = {'kayitNo':2, 'eMail':'Ahmet','sifre':'123456'}
kullanici2 = {'kayitNo':3, 'eMail':'Ayşe','sifre':'98765'}
#Veri tabanında kullanıcı çekildiğini düşünüyorum,şu an buraya bu şekilde hazırladım.
#Kullanıcı kayıt olduktan sonra kullanıcı listesine eklenir.
"""
girilenEmail
eMail
girilenSifre
sifre
"""
kullaniciListesi = [kullanici1,kullanici2]
girilenEmail = input("Mailinizi giriniz")
for kullanici in kullaniciListesi:
    if girilenEmail == kullanici.get("eMail"):
        girilenSifre = input("Şifrenizi giriniz")
        if girilenSifre == kullanici.get("sifre"):
            print("Başarılı giriş yaptınız")
            break
        else:
            girilenSifre = input("Lütfen Şifrenizi kontrol ederek giriniz...1")# 1nci sifre deneme
            if girilenSifre == kullanici.get("sifre"):
                print("Başarılı giriş yaptınız")
                break
            else:
                girilenSifre = input("Lütfen Şifrenizi kontrol ederek giriniz...2")# 2nci sifre deneme
                if girilenSifre == kullanici.get("sifre"):
                    print("Başarılı giriş yaptınız")
                    break
                else:
                    print("Çok fazla deneme yaptınız daha sonra deneyiniz!!!")#Çok fazla deneme uyarısı
    else:
        girilenEmail = input("Lütfen Mailinizi kontrol ederek giriniz...1")# 1nci email deneme
        if girilenEmail == kullanici.get("eMail"):
            girilenSifre = input("Şifrenizi giriniz")
            if girilenSifre == kullanici.get("sifre"):
                print("Başarılı giriş yaptınız")
                break
            else:
                girilenSifre = input("Lütfen Şifrenizi kontrol ederek giriniz...1")# 1nci sifre deneme
                if girilenSifre == kullanici.get("sifre"):
                        print("Başarılı giriş yaptınız")
                        break
                else:
                    girilenSifre = input("Lütfen Şifrenizi kontrol ederek giriniz...2")# 2nci sifre deneme
                    if girilenSifre == kullanici.get("sifre"):
                        print("Başarılı giriş yaptınız")
                        break
                    else:
                        print("Çok fazla deneme yaptınız daha sonra deneyiniz!!!")#Çok fazla deneme uyarısı
                        break
        else:
            girilenEmail = input("Lütfen Mailinizi kontrol ederek giriniz...2")#2nci email deneme
            if girilenEmail == kullanici.get("eMail"):
                girilenSifre = input("Şifrenizi giriniz")
                if girilenSifre == kullanici.get("sifre"):
                    print("Başarılı giriş yaptınız")
                    break
                else:
                    girilenSifre = input("Lütfen Şifrenizi kontrol ederek giriniz...1")# 1nci sifre deneme
                    if girilenSifre == kullanici.get("sifre"):
                        print("Başarılı giriş yaptınız")
                        break
                    else:
                        girilenSifre = input("Lütfen Şifrenizi kontrol ederek giriniz...2")# 2nci sifre deneme
                        if girilenSifre == kullanici.get("sifre"):
                            print("Başarılı giriş yaptınız")
                            break
                        else:
                            print("Çok fazla deneme yaptınız daha sonra deneyiniz!!!")#Çok fazla deneme uyarısı
                            break
            else:
                print("Çok fazla deneme yaptınız daha sonra deneyiniz!!!")
                break
#Kullanıcı güvenliği açısında normalde bu şekilde kontrol olmaz.
#Şu an böyle yapmayı pekiştirmek için uygun gördüm.
#Alternatif kodları aşağıya ekledim.
"""
kullaniciListesi = [kullanici1,kullanici2]
girilenEmail = input("Mailinizi giriniz")
girilenSifre = input("Şifrenizi giriniz")
for kullanici in kullaniciListesi:
    if girilenEmail == kullanici.get("eMail") and girilenSifre == kullanici.get("sifre"):
        print("Başarılı giriş yaptınız")
    elif not girilenEmail == kullanici.get("eMail"):
        print("Böyle bir kayıtlı e-mail adresi yoktur")
    elif not girilenSifre == kullanici.get("sifre"):
        print("Şifrenizi hatalı girdiniz.Lütfen tekrar deneyiniz.")
    else:
        print("E-mail adresiniz ya da şifreniz hatalı,lütfen daha sonra deneyiniz.")
"""
