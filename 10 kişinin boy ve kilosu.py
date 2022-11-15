# importing package
import matplotlib.pyplot as plt
import numpy as np
  
# create data
i = 0
boylar=[0,0,0,0,0,0,0,0,0,0]
kilolar=[0,0,0,0,0,0,0,0,0,0]
grupsayısı = 10
while i<10:
    x = int(input("{}. kişinin boyunu giriniz".format(i+1)))
    boylar[i]=x
    y = int(input("{}. kişinin kilosunu giriniz".format(i+1)))
    kilolar[i]=y
    i += 1
width = 0.4
  
# plot data in grouped manner of bar type
print (boylar)
print (kilolar)
fig, ax = plt.subplots()
index = np.arange(grupsayısı)

opacity = 0.8

rects1 = plt.bar(index, boylar, 0.35,
alpha=opacity,
color='b',
label='Boylar')

rects2 = plt.bar(index + 0.35, kilolar, 0.35,
alpha=opacity,
color='g',
label='Kilolar')

plt.xlabel('Kişiler')
plt.ylabel('boy ve kilolar')
plt.title('Boy ve kilolar')
plt.xticks(index + 0.35, ('1', '2', '3', '4','5', '6', '7', '8','9','10'))
plt.legend()

plt.tight_layout()
plt.show()
