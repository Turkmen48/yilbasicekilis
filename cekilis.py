import random
import pandas as pd
kisiler = ["enes", "ebru", "hatice", "dicle", "şeyda", "ufuk", "akın", "ergün"]  #kaç isim ekleyeceksen buraya tek tek gir
hediyealdi = []  # birine hediye alan
hediyegeldi = []  # birine hediye veren
def cekilis():

    random1 = random.choice(kisiler)
    random2 = random.choice(kisiler)
    if random1==random2:
        cekilis()
    elif random1 not in hediyealdi and random2 not in hediyegeldi:
        print("{} Adlı şanslı kişi {}'a hediye alacak.".format(random1,random2))
        hediyealdi.append(random1)
        hediyegeldi.append(random2)
        print(hediyealdi,hediyegeldi)
    else:
        cekilis()



    # else:
    #     print("{} Adlı şanslı kişi {}'a hediye alacak.".format(random1,random2))
    #     hediyealdi.append(random1)
    #     hediyegeldi.append(random2)
n=[1,2,3,4,5,6,7,8]#kaç kişi eklediysen o kadar rakam veya sayı yaz şu an default 8 kişi var sırayla 1'den 8'e kadar yazdım.

for a in n:
    t=input("Çekmek için ç yaz")
    if t=="ç":
        cekilis()



data = {'Hediye Alacaklar':hediyealdi,
        'Hediye Sahipleri':hediyegeldi}

df=pd.DataFrame(data)
df.index+=1
print(df)



