"""
GİRİLEN ÜÇ SAYIYI BÜYÜKTEN KÜÇÜĞE SIRALAMA

a = int(input("1.sayıyı giriniz."))
b = int(input("2.sayıyı giriniz."))
c = int(input("3.sayıyı giriniz."))

liste = [a,b,c]
liste.sort(reverse=True)

print(liste)
"""


"""
4000'E KADAR OLAN FİBONACCİ DİZİSİ

fibo = [1,1]

for i in fibo:
    sont = fibo[-1] + fibo[-2]
    fibo += [sont]
    if sont >= 4000:
        break

print(fibo)
"""


"""
KULLANICININ İSTEDİĞİ KADAR SAYININ ORTALAMASINI ALMA


adet = int(input("kaç tane sayının ortalamasını almak istiyorsunuz?"))

toplam = 0

for i in range(1,adet+1):
    sayı = int(input(f"{i}. sayı:"))
    toplam += sayı 

ortalama = toplam/adet

print(ortalama)
"""
