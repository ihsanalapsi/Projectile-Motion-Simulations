# Gerekli kütüphaneleri içe aktar
import matplotlib.pyplot as plt
import math
import random

# Atış yörüngesini çizen fonksiyon
def ciz_atis_yolu(hiz, aci_derece, yukseklik, deneme_sayisi):
    g = 9.81
    Vx = hiz_x(hiz, aci_derece)
    Vy_baslangic = hiz_y(hiz, aci_derece)
    ucus_zamani = toplam_ucus_suresi(Vy_baslangic)
    adim_sayisi = 1000
    zaman_adimi = ucus_zamani / adim_sayisi

    x_koordinatlari = []
    y_koordinatlari = []

    # Zaman adımları için x ve y koordinatlarını hesapla
    for t_adimi in range(adim_sayisi + 1):
        zaman = t_adimi * zaman_adimi
        x_konumu = Vx * zaman
        y_konumu = Vy_baslangic * zaman - (1 / 2) * g * zaman**2 + yukseklik
        x_koordinatlari.append(x_konumu)
        y_koordinatlari.append(y_konumu)

    # Hesaplanan koordinatlarla atış yörüngesini çiz
    plt.plot(x_koordinatlari, y_koordinatlari, label=f"Deneme {deneme_sayisi}")

# Hız bileşenlerini hesaplayan fonksiyonlar
def hiz_x(hiz, aci_derece):
    return hiz * math.cos(math.radians(aci_derece))


def hiz_y(hiz, aci_derece):
    return hiz * math.sin(math.radians(aci_derece))

# Toplam uçuş süresini hesaplayan fonksiyon
def toplam_ucus_suresi(dikey_hiz_baslangic):
    g = 9.81
    return 2 * dikey_hiz_baslangic / g

# Atış menzilini hesaplayan fonksiyon
def atis_menzili(hiz_x, ucus_zamani):
    return hiz_x * ucus_zamani

# Hedefe isabet durumunu kontrol eden fonksiyon
def hedefe_isabet(hedef_baslangic, hedef_bitis, menzil):
    return hedef_baslangic <= menzil <= hedef_bitis

# Atış yaparak menzili hesaplayan fonksiyon
def yap_atis(hiz, aci_derece, yukseklik):
    Vx = hiz_x(hiz, aci_derece)
    Vy_baslangic = hiz_y(hiz, aci_derece)
    ucus_zamani = toplam_ucus_suresi(Vy_baslangic)
    X = atis_menzili(Vx, ucus_zamani)
    return X

# Atış denemelerini gerçekleştirerek hedefi vurmaya çalışan fonksiyon
def atis_denemeleri(ikinci_haneler):
    # Hız aralıkları ve sabit değerler
    hiz_min = 330
    hiz_max = 1800
    aci_derece = 30
    hedef_genisligi = 1000
    # Hedefin konumunu ve genişliğini belirle
    hedef_menzil = 20000 + 200 * random.randint(-10, 10)
    hedef_baslangic = hedef_menzil
    hedef_bitis = hedef_menzil + hedef_genisligi + 100 * random.randint(-2, 2)

    deneme_sayisi = 0
    isabet = False

    # Hedefi vurana kadar deneme yap
    while not isabet:
        deneme_sayisi += 1
        hiz = (hiz_min + hiz_max) / 2
        menzil = yap_atis(hiz, aci_derece, ikinci_haneler)

        # Atış yörüngesini çiz
        ciz_atis_yolu(hiz, aci_derece, ikinci_haneler, deneme_sayisi)

        # Hedefe isabet kontrolü
        if hedefe_isabet(hedef_baslangic, hedef_bitis, menzil):
            isabet = True
            print("Hedefi vurdun")
            print(f"{deneme_sayisi}. denemede vuruş başarılı. Hedefi vurmak için gerekli hız: {hiz} m/s")
        else:
            # Hedefin önüne veya arkasına düşme durumuna göre hız aralığını güncelle
            if menzil < hedef_baslangic:
                hiz_min = hiz
                print("Önüne düştü")
            else:
                hiz_max = hiz
                print("Uzağına düştü")

    # Grafik özelliklerini belirle ve göster
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Top Atışları')
    plt.legend()
    plt.show()

    return deneme_sayisi
ikinci_haneler = 30
deneme_sayisi = atis_denemeleri(ikinci_haneler)