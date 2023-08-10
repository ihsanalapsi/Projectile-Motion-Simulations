import matplotlib.pyplot as plt
import math
import random

# Atışın yörüngesini çiz
def plot_trajectory(hiz, aci, okul_numarasi_yukseklik, atis_sayisi):
    g = 10  # yerçekimi ivmesi (m/s^2)
    Vx = yatay_hiz(hiz, aci)  # x eksenindeki hız (m/s)
    Vy0 = dikey_hiz(hiz, aci)  # y eksenindeki başlangıç hızı (m/s)
    Tu = ucus_suresi(Vy0)  # uçuş süresi (s)
    time_steps = 1000  # zaman adımlarının sayısı
    delta_t = Tu / time_steps  # her zaman adımı için süre (s)

    x = []  # x koordinatları
    y = []  # y koordinatları

    # Her zaman adımı için x ve y koordinatlarını hesapla
    for t in range(time_steps + 1):
        t = t * delta_t
        xt = Vx * t
        yt = Vy0 * t - (1 / 2) * g * t**2 + okul_numarasi_yukseklik
        x.append(xt)
        y.append(yt)

    # Atışın yörüngesini çiz
    plt.plot(x, y, label=f"Atış {atis_sayisi}")

# Yatay hızı hesapla
def yatay_hiz(hiz, aci):
    return hiz * math.cos(math.radians(aci))

# Dikey hızı hesapla
def dikey_hiz(hiz, aci):
    return hiz * math.sin(math.radians(aci))

# Uçuş süresini hesapla
def ucus_suresi(dikey_hiz):
    g = 10  # yerçekimi ivmesi (m/s^2)
    return 2 * dikey_hiz / g

# Menzili hesapla
def menzil(yatay_hiz, ucus_suresi):
    return yatay_hiz * ucus_suresi

# Hedefin vurulduğunu kontrol et
def hedef_vuruldu(hedef_genislik_baslangic, hedef_genislik_bitis, menzil):
    return hedef_genislik_baslangic <= menzil <= hedef_genislik_bitis

# Atış yap ve menzili hesapla
def atis_yap(hiz, aci, okul_numarasi_yukseklik):
    Vx = yatay_hiz(hiz, aci)
    Vy0 = dikey_hiz(hiz, aci)
    Tu = ucus_suresi(Vy0)
    X = menzil(Vx, Tu)
    return X

# Top atışlarını gerçekleştir
def top_atislari(son_iki_hane):
    hiz_alt_sinir = 330  # alt hız sınırı (m/s)
    hiz_ust_sinir = 1800  # üst hız sınırı (m/s)
    aci = 30  # atış açısı (derece)
    hedef_genislik = 1000  # hedefin genişliği (m)

    # Hedefin uzaklığını ve genişliğini belirle
    hedef_uzaklik = 20000 + 200 * random.randint(-10, 10)
    hedef_genislik_baslangic = hedef_uzaklik
    hedef_genislik_bitis = hedef_uzaklik + hedef_genislik + 100 * random.randint(-2, 2)

    atis_sayisi = 0  # atış sayısı
    vuruldu = False  # hedef vuruldu mu

    # Hedef vurulana kadar atış yapmaya devam et
    while not vuruldu:
        atis_sayisi += 1
        hiz = (hiz_alt_sinir + hiz_ust_sinir) / 2
        menzil = atis_yap(hiz, aci, son_iki_hane)

        # Atışın yörüngesini çiz
        plot_trajectory(hiz, aci, son_iki_hane, atis_sayisi)

        # Hedefin vurulup vurulmadığını kontrol et
        if hedef_vuruldu(hedef_genislik_baslangic, hedef_genislik_bitis, menzil):
            vuruldu = True
            print("Hedefi vurdun")
            print(f"{atis_sayisi}. seferde vuruş gerçekleşmiştir. Hedefi vurmak için gerekli hız: {hiz} m/s")
        else:
            # Menzil hedefin başlangıcından küçükse hızı artır
            if menzil < hedef_genislik_baslangic:
                hiz_alt_sinir = hiz
                print("Önüne düştü")
            # Menzil hedefin bitişinden büyükse hızı azalt
            else:
                hiz_ust_sinir = hiz
                print("Uzağına düştü")

    # Grafik özelliklerini ayarla ve göster
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Top Mermisi Atışları')
    plt.legend()
    plt.show()

    return atis_sayisi

son_iki_hane = 30
atis_sayisi = top_atislari(son_iki_hane)