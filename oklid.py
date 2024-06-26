import math

# demetleri tanımlıyoruz
points = [(4, 8), (7, 8), (2, 3), (6, 1), (9, 5), (1, 9)]

# öklid hesaplama fonksiyonu
# euclideanDistance için nokta1 ve nokta2 adında iki parametre aldık
def euclideanDistance(nokta1, nokta2):
    # x1 nokta1'in x eksenini, y1 ise nokta1'in y eksenini sağlıyor
    x1, y1 = nokta1
    x2, y2 = nokta2
    # öklid förmülü
    # karekök x2 - x1'in karesi + y2 - y1'in karesi
    # sqrt karekök hesaplamamızı sağlıyor
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # return ile değer döndürülür, return olmazsa mesafe sonucu boş çıkar

# mesafelerin distances içinde saklanması istenmişti, bu sebeple distances listesi oluşturuldu
distances  = []

# minimum mesafenin hangi demetlerde olduğunu bulma
# float infinity float değerde sonsuzluğa eşit
# başlangıçta minimum değer belli olmadığı için sahte bir sonsuz değer vermiş olduk minimum mesafeye
min_mesafe = float('inf')
# internette güzel örnek bulamadım
# ama bu yazılar açıklayıcı olmuş bence:
# https://www.quora.com/How-can-I-store-an-infinity-value-in-a-Python-variable
# https://stackoverflow.com/questions/34264710/what-is-the-point-of-floatinf-in-python
# chat gpt örneği;
#   x = float('inf')
#   print(x > 1000)  # True
#   print(x + 1)     # Sonuç olarak yine sonsuz (inf) döner

# en küçük değeri saklamak için min_points değişkenini kullandık, başlangıç değeri doğal olarak none
min_points = None

# her demet için points'ten gelen mesafeyi hesaplayan for döngüsü
# points listesindeki her elemanı döndürmek için len() kullandık, 6 elemanımız var range(6) ile aynı şey
# ancak daha sonra listeye eleman eklenirse kodu tekrar güncellememek için len daha iyi
for i in range(len(points)):
    # iç içe döngü ile listenin tüm elemanları dönüldü
    # *** az çarpım tablosu yazdırmadı Buse :) *** #
    for j in range(i + 1, len(points)):
        nokta1 = points[i]
        nokta2 = points[j]
        # euclideanDistance fonksiyonunu parametreleri ile çağırıp mesafeyi alıyoruz
        mesafe = euclideanDistance(nokta1, nokta2)
        # append ile distances listesine eleman ekliyoruz
        distances .append(((nokta1, nokta2), mesafe))
        # başlangıçta sonsuz olan minimum mesafe değerini değiştiriyoruz
        if mesafe < min_mesafe:
            min_mesafe = mesafe
            # nokta1, nokta2'yi içeren min_points adında bir değişken oluşturduk
            min_points = (nokta1, nokta2)

# distances'i yazdırıyoruz
# !! gerekli değilse burayı kaldırmayı unutma
print("mesafeler (distances list):")
# for demetler ile distances içindeki her iki nokta (bir demet) için for oluşturduk
for demetler, mesafe in distances :
    # noktaları ve mesafeyi ekrana yazdırdık
    # demetler ve mesafeyi yazdırmak için tip dönüşümü gerekli çünkü float bir ifade
    # (veya yeni öğrendiğim bir şey var aşağıda kullandım (f-stirng) onu kullanabiliriz)
    print(str(demetler) + ": " + str(mesafe))

# en kısa mesafe ve bu mesafelerin hangi demette olduğunu ekrana yazdırma
# f harfi (f-string deniyormuş) + operatörünün yerine geçiyormuş
print(f"\nminimum öklid mesafesi: {min_mesafe}")
print(f"en kısa mesafeye sahip points: {min_points}")
