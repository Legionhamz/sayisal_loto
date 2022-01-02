# sayisal_loto
from random import randint

a = 0
x = 1
liste = []

while x < 9:  #### buradaki döngü listeyi 8 tane yazdırır 1,başlayıp 8'e kadar gider
    x += 1
    a += 1
    liste = []

    for i in range(1, 8):  #### bu döngüde 6 tane rakam rastgele seçer ve alt alta 8 tane yazdırır

        sayi = randint(1, 49)  #### burada sayiya 1 ve 49 arası rastgele sayı seçer

        if i == 7:  ### i 7'ye eşit olduğunda durur
            break

        else:
            liste.append(sayi)  #### burada listeye sayiyi ekler

    print("KOLON", a, liste)  #### a 1'den başlayıp her defasında 1 artarak 8 'e kadar gider