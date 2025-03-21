"""

def listeyi_ters_cevir_ve_cift_yap(liste):
    liste.reverse()
    for i in range(len(liste)):
        liste[i] = liste[i] * 2
    return liste

sayilar = []
while True:
    try:
        adet = int(input("kaç sayı gireceksin"))
        if adet > 0:
            break
        else:
            print("lütfen 1 veya daha büyük bir sayı girin.")
    except ValueError:
        print("geçersiz giriş! lütfen tam bir sayı girin.")
for i in range(adet):
    while True:
        try:
            sayi = float(input(f"{i+1}. sayıyı gir:"))
            sayilar.append(sayi)
            break
        except ValueError:
            print("geçersiz giriş lütfen bir sayı girin.")

sonuc = listeyi_ters_cevir_ve_cift_yap(sayilar)

#dosyaya yazma işlemi
with open("sayilar.txt","w") as dosya:
    for sayi in sonuc:
        dosya.write(str(sayi)+"\n")#sayıları satır satır dosyaya yaz
print("listeyi ters çevirdik ve her ögesini iki katına çıkardık:",sonuc)
print("sayılar başarıyla 'sayilar.txt' dosyasına kaydedildi. ")

#dosyadan sayıları okuma seçeneği
secim = input("dosyadaki sayıları görmek ister misin? (E/H):").strip().lower()

if secim == "e":
    with open("sayilar.txt","r") as dosya:
        print("dosyadaki sayılar:")
        print(dosya.read())#dosyadaki tüm içeriği oku ve yazdır

"""
"""
def listeyi_ters_cevir_ve_cift_yap(liste):
    liste.reverse() #listeyi ters cevir
    for i in range(len(liste)):
        liste[i] = liste[i] * 2 #her ögeyi iki katına çıkar
    return liste #işlenmiş listeyi döndür
def sayi_ekle(dosya_adı,sayilar):
    with open(dosya_adı,"a") as dosya: # "a" append yani eklelme
        for sayi in sayilar:
            dosya.write(str(sayi) + "\n")
    print(f"sayılar {dosya_adı} dosyasına eklendi.")

def dosyayi_temizle(dosya_adı):
    with open(dosya_adı,"w") as dosya: #"w" yazma modunda dosyayı aç, içerik silinir
        dosya.truncate(0) #dosyayı tamamen temizler
    print(f"{dosya_adı} dosyası temizlendi")

def dosyadaki_sayilari_sirala(dosya_adı, ters= False):
    with open(dosya_adı,"r") as dosya:
        sayilar=[float(sayi.strip()) for sayi in dosya.readlines()]

    sayilar.sort(reverse=ters) # küçükten büyüğe sıralama ters = True büyükten küçüğe sıralar
    with open(dosya_adı,"w") as dosya:
        for sayi in sayilar:
            dosya.write(str(sayi) + "\n")
    print(f"sayılar sıralandı: {sayilar}")

#Kullanıcıdan sayılar alma ve dosyaya yazma işlemi
sayilar =[]
adet = int(input("kaç sayı gireceksin ?"))
for i in range(adet):
    sayi= float(input(f"{i+1}. sayıyı gir"))
    sayilar.append(sayi)
sonuc = listeyi_ters_cevir_ve_cift_yap(sayilar)

#sayıları dosyaya kaydetme
with open("sayilar.txt","w") as dosya:
    for sayi in sonuc:
        dosya.write(str(sayi) + "\n")
print("liste başarıyla 'sayilar.txt' dosyasına kaydedildi.")

# Kullanıcıdan işlem seçmesi
secim= input("dosya işlemi yapmak ister misin? (E/H):").strip().lower()

if secim == "e":
    print("1. dosyaya yeni sayılar ekle")
    print("2. dosyadaki sayıları sil")
    print("3. dosyadaki sayıları sıralama")
    secim2 = input("yapmak istediğiniz işlemi seçin (1/2/3):").strip()

    if secim2 == "1":
        yeni_adet = int(input("kaç yeni sayı eklemek istersiniz?"))
        yeni_sayilar = []
        for i in range(yeni_adet):
            sayi=float(input(f"{i+1}. yeni sayıyı gir:"))
            yeni_sayilar.append(sayi)
        sayi_ekle("sayilar.txt", yeni_sayilar)

    elif secim2== "2":
        onay = input("dosyadaki sayıları silmek istediğinizden emin misiniz? (E/H)").strip().lower()
        if onay == "e":
            dosyayi_temizle("sayilar.txt")

    elif secim2 == "3":
        sıralama = input("sayıları küçükten büyüğe mi sıralasın(K/B)?").strip().lower()
        if sıralama =="k":
            dosyadaki_sayilari_sirala("sayilar.txt",ters=False)
        elif sıralama == "b":
            dosyadaki_sayilari_sirala("sayilar.txt", ters=True)
"""


import matplotlib.pyplot as plt
# Kullanıcının girdiği sayıları dosyaya yazan fonksiyon
def dosyaya_sayi_ekle(dosya_adı):
    with open(dosya_adı,"a") as dosya:
        while True:
            sayi = input("bir sayı girin( çıkmak için 'q' tuşuna basın:").strip()
            if sayi.lower()== 'q':
                break
            try:
                dosya.write(sayi + "\n")
            except Exception as e:
                print(f"Hata oluştu: {e}")

#dosyadan sayıları okuyup ekrana yazdıran fonksiyon
def dosyadan_sayilari_oku(dosya_adı):
    try:
        with open(dosya_adı, "r") as dosya:
            sayilar = dosya.readlines()
            if not sayilar:
                print("dosya boş!")
                return
            print("dosyadaki sayılar:")
            for sayi in sayilar:
                print(sayi.strip())
    except FileNotFoundError:
        print("dosya bulunamadı!")

# dosyadaki sayıların tamamını hesaplayan fonksiyon (önceki kodlarımızdan)
def dosya_toplam_hesaplama(dosya_adı):
    with open(dosya_adı,"r") as dosya:
        sayilar = [float(sayi.strip()) for sayi in dosya.readlines()]

    if len(sayilar) == 0:
        print("dosyada hiç sayı yok!")
        return

    toplam =sum(sayilar)
    print(f"dosyadaki sayıların toplamı: {toplam}")

# dosyadaki sayıların ortalamasını hesaplayan fonksiyon
def dosya_ortalama_hesapla(dosya_adı):
    with open(dosya_adı,"r") as dosya:
        sayilar = [float(sayi.strip()) for sayi in dosya.readlines()]

    if len(sayilar) == 0:
        print("dosyada hiç sayı yok!")
        return

    ortalama = sum(sayilar) / len(sayilar)
    print(f"dosyadaki sayıların ortalaması: {ortalama:.2f}")

# dosyadaki en büyük ve en küçük sayıyı bulan fonksiyon
def dosyadaki_min_max(dosya_adı):
    with open(dosya_adı,"r") as dosya:
        sayilar = [float(sayi.strip()) for sayi in dosya.readlines()]

    if len(sayilar) == 0:
        print("dosyada hiç sayı yok!")
        return
    en_kucuk = min(sayilar)
    en_buyuk = max(sayilar)
    print(f"en küçük sayı: {en_kucuk}")
    print(f"en büyük sayı: {en_buyuk}")

#dosyadaki sayıları grafik olarak gösteren fonksiyon
def dosya_grafik_ciz(dosya_adı):
    with open(dosya_adı,"r") as dosya:
        sayilar = [float(sayi.strip()) for sayi in dosya.readlines()]

    if len(sayilar)== 0 :
        print("dosyada hiç sayı yok!")
        return

    plt.plot(sayilar,marker ="o",linestyle="-", color="b", label="sayısal veriler")
    plt.xlabel("veri sırası")
    plt.ylabel("sayı değeri")
    plt.title("dosyadaki sayıların grafiği")
    plt.legend()
    plt.grid()
    plt.show()

# histogram çizme fonksiyonu
import matplotlib.pyplot as plt

def dosya_histogram_ciz(dosya_adı):
    try:
        with open(dosya_adı,"r") as dosya:
            sayilar = [float(sayi.strip()) for sayi in dosya.readlines()]

        if not sayilar:
            print("dosyada hiç sayı yok!")
            return

        plt.hist(sayilar, bins=10,color='skyblue', edgecolor='black')
        plt.xlabel("sayı değerleri")
        plt.ylabel("frekans")
        plt.title("sayıların histogramı")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    except FileNotFoundError:
        print("dosya bulunamadı!")
    except ValueError:
        print("dosyada geçersiz veri var!")
def dosyalari_olustur():
    with open("sayilar1.txt","w") as dosya1:
        dosya1.write("10\n20\n30\n40\n50\n")
    with open("sayilar2.txt","w") as dosya2:
        dosya2.write("15\n25\n35\n45\n55\n")

    print("dosyalar oluşturuldu ve sayılar eklendi")
dosyalari_olustur()

def dosya_toplamlarini_karsilastir(dosya1,dosya2):
    def dosya_toplam_hesapla(dosya_adı):
        try:
            with open(dosya_adı,"r") as dosya:
                sayilar = [float(sayi.strip()) for sayi in dosya.readlines()]
            return sum(sayilar)
        except FileNotFoundError:
            print(f"{dosya_adı} bulunamadı!")
            return None
        except ValueError:
            print(f"{dosya_adı} içinde geçersiz veri var")
            return None

    toplam1 = dosya_toplam_hesapla(dosya1)
    toplam2 = dosya_toplam_hesapla(dosya2)

    if toplam1 is None or toplam2 is None:
        return

    print(f"{dosya1} toplamı: {toplam1}")
    print(f"{dosya2} toplamı: {toplam2}")

    if toplam1 > toplam2:
        print(f"{dosya1} daha büyük")
    elif toplam2 > toplam1:
        print(f"{dosya2} daha büyük")
    else:
        print("iki sayının toplamı eşit")




# kullanıcı menüsü
dosya_adı ="sayilar.txt"
dosya1 = "sayilar1.txt"
dosya2 = "sayilar2.txt"
while True:
    print("\n=== MENÜ ===")
    print("1. dosyaya yeni sayı ekle ")
    print("2. dosyadaki sayıları oku ve göster")
    print("3. dosyadaki sayıların toplamını hesapla") #daha önce eklediğimiz toplam fonksiyonu
    print("4.dosyadaki sayıların ortalamasını hesapla")
    print("5. dosyadaki en büyük ve en küçük sayıyı göster")
    print("6. dosyadaki sayıları grafik olarak çiz")
    print("7.dosyadaki sayıların histogramı çiz")
    print("8. dosyalardaki toplamları karşılaştır")
    print("9. çıkış")


    secim = input("yapmak istediğiniz işlemi seçin (1/2/3/4/5/6/7/8/9):").strip()

    if secim == "1":
        dosyaya_sayi_ekle(dosya_adı)

    elif secim =="2":
        dosyadan_sayilari_oku(dosya_adı)

    elif secim =="3":
        dosya_toplam_hesaplama(dosya_adı)

    elif secim =="4":
        dosya_ortalama_hesapla(dosya_adı)

    elif secim =="5":
        dosyadaki_min_max(dosya_adı)

    elif secim =="6":
        dosya_grafik_ciz(dosya_adı)

    elif secim =="7":
        dosya_histogram_ciz(dosya_adı)

    elif secim == "8":
        dosya1= input("karşılaştırmak istediğiniz ilk dosya adını girin:")
        dosya2 = input("karşılaştırmak istediğiniz ikiinci dosya adını girin:")
        dosya_toplamlarini_karsilastir(dosya1,dosya2)

    elif secim =="9":
        print("çıkış yapılıyor...")
        break

    else:
        print("geçersiz seçim, tekrar deneyin")

"""

# DOSYA SEÇME PENCERESİ AÇAN KOD 

import tkinter as tk
from tkinter import filedialog

def dosya_sec():
    root = tk.Tk()
    root.withdraw()
    dosya_yolu = filedialog.askopenfilename(title="bir dosya seçin")
    return dosya_yolu
dosya1 = dosya_sec()
dosya2 = dosya_sec()

print("seçilen dosya 1 ", dosya1)
print("seçilen dosya 2 ",dosya2)

"""

