
def hitung_kubus(rusuk):
    luas_permukaan = 6 * rusuk**2
    volume = rusuk**3
    return luas_permukaan, volume


def hitung_balok(panjang, tinggi, lebar):
    luas_permukaan = 2 * (panjang*tinggi + panjang*lebar + tinggi*lebar)
    volume = panjang * tinggi * lebar
    return luas_permukaan, volume


def hitung_bola(jari_jari):
    luas_permukaan = 4*3.14*jari_jari**2
    volume = (4/3)*3.14*jari_jari**3
    return luas_permukaan, volume


def hitung_kerucut(jari_jari, garis_pelukis, tinggi):
    luas_permukaan = (3.14*jari_jari*garis_pelukis)+(3.14*jari_jari**2)
    volume = 3.14*jari_jari**2*tinggi
    return luas_permukaan, volume


def hitung_limas_segiempat(panjang_alas_limas, tinggi_limas, lebar_alas_limas):
    luas_permukaan = (panjang_alas_limas*lebar_alas_limas)+2 * \
        (panjang_alas_limas*tinggi_limas/2)+2*(lebar_alas_limas*tinggi_limas/2)
    volume = (panjang_alas_limas*lebar_alas_limas)*tinggi_limas/3
    return luas_permukaan, volume


def hitung_limas_segitiga(panjang_alas_segitiga, tinggi_segitiga, tinggi_limas):
    luas_permukaan = panjang_alas_segitiga+3 * \
        (panjang_alas_segitiga*tinggi_segitiga/2)
    volume = (panjang_alas_segitiga*tinggi_segitiga/2)*tinggi_limas/3
    return luas_permukaan, volume


def hitung_silinder(jari_jari, tinggi):
    luas_permukaan = (2*3.14*jari_jari*tinggi)+(2*3.14*jari_jari**2)
    volume = 3.14*jari_jari**2*tinggi
    return luas_permukaan, volume


def hitung_prisma_segitiga(s1, s2, s3, alas, tinggi_prisma, tinggi):
    luas_permukaan = (s1+s2+s3)*tinggi_prisma*alas*tinggi
    volume = alas*tinggi*tinggi_prisma/2
    return luas_permukaan, volume
