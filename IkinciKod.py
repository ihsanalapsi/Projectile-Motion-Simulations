import matplotlib.pyplot as plt
import math
import random

# Hız ve açıya göre yatay hızı hesaplar
def hesapla_yatay_hiz(hiz, aci):
    return hiz * math.cos(math.radians(aci))

# Hız ve açıya göre dikey hızı hesaplar
def hesapla_dikey_hiz(hiz, aci):
    return hiz * math.sin(math.radians(aci))

# Dikey hıza göre uçuş süresini hesaplar
def ucus_zamani(dikey_hiz):
    g = 10
    return 2 * dikey_hiz / g

# Yatay hız ve uçuş süresine göre menzili hesaplar
def menzil_hesapla(yatay_hiz, ucus_zamani):
    return yatay_hiz * ucus_zamani

# Hedefin vurulup vurulmadığını kontrol eder
def hedef_vuruldu(baslangic_menzil, bitis_menzil, atis_menzil):
    return baslangic_menzil <= atis_menzil <= bitis_menzil

# Atış yaparak menzili hesaplar
def atis_yap(hiz, aci, yukseklik_ofset):
    yatay_hiz = hesapla_yatay_hiz(hiz, aci)
    dikey_hiz = hesapla_dikey_hiz(hiz, aci)
    havada_geciren_zaman = ucus_zamani(dikey_hiz)
    katedilen_mesafe = menzil_hesapla(yatay_hiz, havada_geciren_zaman)
    return katedilen_mesafe

# Atış yörüngesini çizer
def cizim_atis_yolu(hiz, aci, yukseklik_ofset, atis_numarasi):
    g = 10
    yatay_hiz = hesapla_yatay_hiz(hiz, aci)
    dikey_hiz = hesapla_dikey_hiz(hiz, aci)
    havada_geciren_zaman = ucus_zamani(dikey_hiz)
    zaman_adimlari = 1000
    delta_t = havada_geciren_zaman / zaman_adimlari

    x_noktalar = []
    y_noktalar = []

    for t in range(zaman_adimlari + 1):
        t = t * delta_t
        x = yatay_hiz * t
        y = dikey_hiz * t - (1 / 2) * g * t**2 + yukseklik_ofset
        x_noktalar.append(x)
        y_noktalar.append(y)

    plt.plot(x_noktalar, y_noktalar, label=f"Atış {atis_numarasi}")

# Atışları gerçekleştirerek hedefi vurmayı dener
def atislari_gerceklestir_v2(son_iki_hane):
    # Hız sınırlarını tanımla
    alt_hiz_siniri = 330
    ust_hiz_siniri = 1800
    aci = 30
    hedef_genislik = 1000

    # Hedef mesafesini ve menzilini belirle
    hedef_mesafe = 20000 + 200 * random.randint(-10, 10)
    baslangic_menzil = hedef_mesafe
    bitis_menzil = hedef_mesafe + hedef_genislik + 100 * random.randint(-2, 2)

    atis_sayisi = 0
    vuruldu = False

    # Hedef vurulana kadar döngüyü sürdür
    while not vuruldu:
        atis_sayisi += 1
        hiz = (alt_hiz_siniri + ust_hiz_siniri) / 2
        atis_menzil = atis_yap(hiz, aci, son_iki_hane)

        # Atış yörüngesini çiz
        cizim_atis_yolu(hiz, aci, son_iki_hane, atis_sayisi)

        # Hedef vurulduğunda çıktıları yazdır
        if hedef_vuruldu(baslangic_menzil, bitis_menzil, atis_menzil):
            vuruldu = True
            print("Hedefi vurdun")
            print(f"{atis_sayisi}. seferde vuruş gerçekleşmiştir. Hedefi vurmak için gerekli hız: {hiz} m/s")
        else:
            # Menzil durumlarına göre hız sınırlarını güncelle
            if atis_menzil < baslangic_menzil:
                alt_hiz_siniri = hiz
                print("Önüne düştü")
            else:
                ust_hiz_siniri = hiz
                print("Uzağına düştü")

    # Grafik etiketlerini ekle ve göster
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Top Mermisi Atışları')
    plt.legend()
    plt.show()

    return atis_sayisi

# Örnek kullanım
son_iki_hane = 30
atis_sayisi = atislari_gerceklestir_v2(son_iki_hane)
