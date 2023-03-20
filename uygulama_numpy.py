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



