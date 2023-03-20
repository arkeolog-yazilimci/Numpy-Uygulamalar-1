import numpy as np

result = np.array([10,15,30,45,60])

result = np.arange(5,15) # 5ile 15 arasında np dizisi oluştur

result = np.arange(50,100,5) #5 er 5er artma

result = np.zeros(10)
result = np.ones(10) # 0 ve 1 lerden oluşan diziler

result = np.linspace(0,100,5) # başlangıç ve bitişi 5 eşit parçaya böler

result = np.random.randint(10,30,5) #10 ile 30 arası 5 tane rastgele sayı üret

result = np.random.randn(10) #-1 ile 1 arası 10 tane sayı
result = np.random.rand(10) #0 ile 1 arası 10 tane sayı

result = np.random.randint(10,50,15).reshape(3,5) # 3x5 matrisli 10 ile 50 atası rastgele 15 sayı

matris = np.random.randint(10,50,15).reshape(3,5) #üretilen matrisin satır ve sütunları toplamı
rowTotal = matris.sum(axis = 1)
colTotal = matris.sum(axis = 0)
print(matris)
print(rowTotal)
print(colTotal)
result = matris.max() #matrisin en büyük ve en küçük sayısı
result = matris.min()

result = matris.mean() #ortalaması matrisin

result = matris.argmax() # matrisin en büyük değerinin indeksi
result = matris.argmin() # matrisin en küçük değerinin indeksi

arr = np.arange(10,20) # 10 ile 20 arası dizinin ilk 3 elemanı
result = arr[0:3]

result = arr[::-1] #tersten yazdır

result = matris[0] # matrisin ilk satırı
result = matris[1,2] # 2.satır 3.sütun değeri

result = matris[:,0] # matrisin tüm satırlardaki ilk elemanları
result = matris**2 # matrisin her bir elemanın karesi

result = matris %2 == 0# matris elamanlarının hangisi pozitif çift sayı aralık(-50,50) True False
result = matris[matris %2 == 0] # matris elamanlarının hangisi pozitif çift sayı aralık(-50,50) sayıy gösterir

ciftler = result = matris[matris %2 == 0]
result = ciftler[ciftler>0]
print(result)
