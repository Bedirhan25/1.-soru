while 1:
    x = int(input("Çarpanlarının alınmasını istediğiniz sayıyı giriniz"))
    i = 1
    while i <= x:
        if x % i == 0:
            print(i)

        i += 1
    print("çıkış yapmak için 0 'ı tuşlaynız")
    if x==0:
        break
